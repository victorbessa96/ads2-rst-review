#!/usr/bin/env python3
"""Validate or generate package receipts.

Normal mode executes producers, performs a fresh relocated-copy reproduction,
and writes manifest.json/validation.json. READ_ONLY=1 performs no writes and
uses the existing receipts.
"""
from pathlib import Path
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "manifest.json"
VALIDATION = ROOT / "validation.json"
ARCHIVE_SHA = ROOT / "Archive.zip.sha256"
LINK_RE = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\s]+)(?:\s+['\"][^)'\"]*['\"])?\)")
SKIP_SCHEMES = ("http://", "https://", "mailto:", "data:")
# Pinned acceptance contract, not a claim of independent derivations.
EXPECTED_SCIENCE = {"verify": 138, "independent": 39, "advanced": 32}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def excluded(path, archive):
    if path in (MANIFEST, VALIDATION, archive, ARCHIVE_SHA):
        return True
    rel = path.relative_to(ROOT).as_posix()
    return "__pycache__" in path.parts or rel.startswith("lean/.lake/") or rel.startswith(".git/")


def role(path):
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith("sources/"):
        return "primary-source"
    if rel.startswith("legacy/"):
        return "legacy-evidence"
    if rel.startswith("reviews/"):
        return "review-evidence"
    if rel.startswith("outputs/"):
        return "execution-receipt"
    if rel.endswith(".py"):
        return "verification-producer"
    if rel.endswith(".md"):
        return "review-document"
    return "package-artifact"


def markdown_links():
    unresolved = []
    links = 0
    per_note = {}
    for note in sorted(ROOT.rglob("*.md")):
        if note.relative_to(ROOT).as_posix().startswith("lean/.lake/"):
            continue
        text = note.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        count = 0
        for match in LINK_RE.finditer(text):
            target = match.group(1).split("#", 1)[0]
            if not target or target.startswith(SKIP_SCHEMES):
                continue
            count += 1
            links += 1
            resolved = (note.parent / target).resolve()
            if not resolved.exists():
                # These two generated files are allowed to be absent on the first pass.
                if target in ("manifest.json", "validation.json"):
                    continue
                unresolved.append(f"{note.relative_to(ROOT)} -> {target}")
        per_note[note.relative_to(ROOT).as_posix()] = count
    return links, per_note, unresolved


def main():
    read_only = os.environ.get("READ_ONLY", "0") == "1"
    python = os.environ.get("PHYSICS_PYTHON", sys.executable)
    if not read_only and os.environ.get("SKIP_PRODUCERS", "0") != "1":
        for producer in ("verify.py", "independent_symbolic.py", "advanced_checks.py"):
            proc = subprocess.run([python, str(ROOT / producer)], cwd=ROOT, capture_output=True, text=True, timeout=240)
            if proc.returncode != 0:
                print(proc.stdout)
                print(proc.stderr)
                raise SystemExit(f"producer failed: {producer}: exit {proc.returncode}")
    archive = ROOT / "Archive.zip"
    required = [
        "00-index.md", "01-executive-claim.md", "02-source-and-derivation.md", "12-signed-net-focusing.md", "13-breakthrough-program.md", "14-state-pulse-phase-diagram.md", "15-physical-boundary-injection.md", "16-conformal-matter-realization.md", "17-observables-and-universality.md", "18-close-out.md",
        "03-sustained-flux-theorem.md", "04-horizon-and-causal-structure.md",
        "05-state-frame-and-novelty.md", "06-finite-pulse.md",
        "07-evidence-and-reproduction.md", "08-review-adjudication.md",
        "09-independent-reviews.md", "10-formal-signoff.md", "11-cumulative-flux-generalization.md", "README.md",
        "verify.py", "independent_symbolic.py", "advanced_checks.py", "run_verification.sh", "requirements.txt",
        "sources/wormholeRST_jhep.tex", "sources/gr-qc-0404098.tar", "outputs/verify.out",
        "outputs/verification-summary.json", "outputs/independent_symbolic.out", "outputs/advanced-checks.out", "outputs/advanced-checks-summary.json",
        "outputs/independent-symbolic-summary.json", "outputs/lean-build.out", "outputs/lean-build.json",
        "outputs/tectonic-build.out", "outputs/tectonic-build.json", "lean/AdS2RST.lean", "lean/lakefile.toml",
        "lean/lean-toolchain", "lean/README.md", "manuscript/ads2-rst-one-sided-flux.tex",
        "manuscript/ads2-rst-one-sided-flux.pdf",
    ]
    external_source = not (ROOT / "sources" / "wormholeRST_jhep.tex").is_file()
    if external_source:
        required = [name for name in required if name not in ("sources/wormholeRST_jhep.tex", "sources/gr-qc-0404098.tar")]
        required.append("sources/source-anchors.txt")
    missing = [name for name in required if not (ROOT / name).is_file()]
    links, per_note, unresolved = markdown_links()
    science = json.loads((ROOT / "outputs/verification-summary.json").read_text())
    independent = json.loads((ROOT / "outputs/independent-symbolic-summary.json").read_text())
    advanced = json.loads((ROOT / "outputs/advanced-checks-summary.json").read_text())
    if external_source:
        source_note = (ROOT / "sources" / "README.md").read_text(encoding="utf-8")
        source_ok = ("https://arxiv.org/abs/gr-qc/0404098v2" in source_note
                     and "8906ec46e685404da151c8b7d52a325c4053ee8c8f17964df7264c69baf58872" in source_note)
        source_sha = None
    else:
        with tarfile.open(ROOT / "sources/gr-qc-0404098.tar") as bundle:
            member = bundle.extractfile("wormholeRST_jhep.tex").read()
        source_ok = member == (ROOT / "sources/wormholeRST_jhep.tex").read_bytes()
        source_sha = hashlib.sha256(member).hexdigest()
    # Normal mode performs a fresh relocation, not just a receipt comparison.
    portability = {}
    if not read_only:
        receipt_path = ROOT / "outputs/portability-receipt.json"
        try:
            with tempfile.TemporaryDirectory(prefix="ads2-validate-relocation-") as temp:
                copy = Path(temp) / "package"
                shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns("__pycache__", ".lake", "Archive.zip", "Archive.zip.sha256", "manifest.json", "validation.json"))
                results = {}
                for producer in ("verify.py", "independent_symbolic.py", "advanced_checks.py"):
                    proc = subprocess.run([python, str(copy / producer)], cwd=copy, capture_output=True, text=True, timeout=240)
                    results[producer] = proc
                copied_main = json.loads((copy / "outputs/verification-summary.json").read_text())
                copied_independent = json.loads((copy / "outputs/independent-symbolic-summary.json").read_text())
                copied_advanced = json.loads((copy / "outputs/advanced-checks-summary.json").read_text())
                main_ok = results["verify.py"].returncode == 0 and (copied_main["checks_total"], copied_main["checks_passed"], copied_main["checks_failed"]) == (EXPECTED_SCIENCE["verify"], EXPECTED_SCIENCE["verify"], 0)
                independent_ok = results["independent_symbolic.py"].returncode == 0 and (copied_independent["checks_total"], copied_independent["checks_passed"], copied_independent["checks_failed"]) == (EXPECTED_SCIENCE["independent"], EXPECTED_SCIENCE["independent"], 0)
                advanced_ok = results["advanced_checks.py"].returncode == 0 and (copied_advanced["checks_total"], copied_advanced["checks_passed"], copied_advanced["checks_failed"]) == (EXPECTED_SCIENCE["advanced"], EXPECTED_SCIENCE["advanced"], 0)
                identical = (copy / "outputs/verify.out").read_bytes() == (ROOT / "outputs/verify.out").read_bytes()
                portability = {
                    "status": "PASS" if main_ok and independent_ok and advanced_ok and identical else "FAIL",
                    "verify_exit": results["verify.py"].returncode,
                    "independent_exit": results["independent_symbolic.py"].returncode,
                    "advanced_exit": results["advanced_checks.py"].returncode,
                    "main_checks": f"{copied_main['checks_passed']}/{copied_main['checks_total']}",
                    "independent_checks": f"{copied_independent['checks_passed']}/{copied_independent['checks_total']}",
                    "advanced_checks": f"{copied_advanced['checks_passed']}/{copied_advanced['checks_total']}",
                    "main_output_byte_identical": identical,
                    "main_output_sha256": sha(copy / "outputs/verify.out"),
                }
        except Exception as exc:
            portability = {"status": "FAIL", "error": str(exc)}
        receipt_path.write_text(json.dumps(portability, indent=2) + "\n", encoding="utf-8")
    else:
        portability = json.loads((ROOT / "outputs/portability-receipt.json").read_text())
    artifacts = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or excluded(path, archive):
            continue
        artifacts.append({
            "path": path.relative_to(ROOT).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha(path),
            "role": role(path),
        })
    manifest = {
        "schema": "ads2-rst.review-package.manifest.v1",
        "created_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "file_count": len(artifacts),
        "artifacts": artifacts,
        "exclusions": ["manifest.json (self)", "validation.json (final receipt)", "Archive.zip and Archive.zip.sha256 (self-containing distribution)", "__pycache__/", "lean/.lake/ (downloaded dependencies)"],
        "source_tex_sha256": source_sha,
        "source_reference_sha256": "8906ec46e685404da151c8b7d52a325c4053ee8c8f17964df7264c69baf58872",
        "source_mode": "external-links" if external_source else "bundled-source",
        "linked_markdown": {"links": links, "unresolved": unresolved, "per_note": per_note},
    }
    if not read_only:
        MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    loaded = json.loads(MANIFEST.read_text())
    actual_files = [p for p in ROOT.rglob("*") if p.is_file() and not excluded(p, archive)]
    mismatches = []
    for row in loaded["artifacts"]:
        path = ROOT / row["path"]
        if path.stat().st_size != row["bytes"] or sha(path) != row["sha256"]:
            mismatches.append(row["path"])
    checks = []
    def record(name, ok, evidence):
        checks.append({"check": name, "pass": bool(ok), "evidence": str(evidence)})
    archive_missing = []
    archive_current = True
    archive_sha_ok = True
    archive_present = archive.is_file()
    if archive_present:
        with zipfile.ZipFile(archive) as bundle:
            names = set(bundle.namelist())
            for name in ("11-cumulative-flux-generalization.md", "lean/AdS2RST.lean", "manuscript/ads2-rst-one-sided-flux.tex", "manuscript/ads2-rst-one-sided-flux.pdf"):
                member_name = "To review/" + name
                if member_name not in names:
                    archive_missing.append(member_name)
                elif name != "manuscript/ads2-rst-one-sided-flux.pdf" and bundle.read(member_name) != (ROOT / name).read_bytes():
                    archive_current = False
        archive_sha_ok = ARCHIVE_SHA.is_file() and ARCHIVE_SHA.read_text().split()[0] == sha(archive)
    archive_ok = not archive_present or (not archive_missing and archive_current and archive_sha_ok)
    archive_status = "verified" if archive_present and archive_ok else ("failed" if archive_present else "not-present-not-claimed")
    record("required_artifacts", not missing and archive_ok,
           f"missing={missing}; archive_status={archive_status}; archive_missing={archive_missing}; archive_current={archive_current}; archive_sha_ok={archive_sha_ok}")
    record("relative_markdown_links", not unresolved, f"links={links}; unresolved={unresolved}")
    record("main_science_counts", (science["checks_total"], science["checks_passed"], science["checks_failed"]) == (EXPECTED_SCIENCE["verify"], EXPECTED_SCIENCE["verify"], 0),
           f"{science['checks_passed']}/{science['checks_total']} PASS; failed={science['checks_failed']}")
    record("independent_science_counts", (independent["checks_total"], independent["checks_passed"], independent["checks_failed"]) == (EXPECTED_SCIENCE["independent"], EXPECTED_SCIENCE["independent"], 0),
           f"{independent['checks_passed']}/{independent['checks_total']} PASS; failed={independent['checks_failed']}")
    record("advanced_science_counts", (advanced["checks_total"], advanced["checks_passed"], advanced["checks_failed"]) == (EXPECTED_SCIENCE["advanced"], EXPECTED_SCIENCE["advanced"], 0),
           f"{advanced['checks_passed']}/{advanced['checks_total']} PASS; failed={advanced['checks_failed']}")
    record("source_tar_identity", source_ok and (external_source or source_sha == "8906ec46e685404da151c8b7d52a325c4053ee8c8f17964df7264c69baf58872"),
           "external-source-links; original tar not redistributed" if external_source else source_sha)
    red_first = json.loads((ROOT / "outputs/red-first-summary.json").read_text())
    red_second = json.loads((ROOT / "outputs/red-second-summary.json").read_text())
    red_first_ok = (ROOT / "outputs/red-first.out").is_file() and (red_first["checks_total"], red_first["checks_passed"], red_first["checks_failed"]) == (129, 125, 4)
    red_second_ok = (ROOT / "outputs/red-second.out").is_file() and (red_second["checks_total"], red_second["checks_passed"], red_second["checks_failed"]) == (129, 128, 1)
    record("red_first_preserved", red_first_ok,
           f"{red_first['checks_passed']}/{red_first['checks_total']} red-first artifacts present; failed={red_first['checks_failed']}")
    record("red_second_preserved", red_second_ok,
           f"{red_second['checks_passed']}/{red_second['checks_total']} red-second artifacts present; failed={red_second['checks_failed']}")
    portable_hash_ok = portability.get("main_output_sha256") == sha(ROOT / "outputs/verify.out")
    record("relocated_reproduction", portability.get("status") == "PASS" and portability.get("main_output_byte_identical") is True and portable_hash_ok,
           f"fresh={not read_only}; status={portability.get('status')}; byte_identical={portability.get('main_output_byte_identical')}; receipt_hash_matches={portable_hash_ok}")
    lean_source = ROOT / "lean/AdS2RST.lean"
    lean_log = ROOT / "outputs/lean-build.out"
    lean_text = lean_log.read_text()
    lean_code = re.sub(r"/-.*?-/", "", lean_source.read_text(), flags=re.S)
    lean_code = re.sub(r"--.*", "", lean_code)
    no_placeholders = not re.search(r"\b(sorry|admit|axiom)\b", lean_code) and "declaration uses 'sorry'" not in lean_text
    lean_receipt = json.loads((ROOT / "outputs/lean-build.json").read_text())
    lean_fresh = (lean_receipt.get("source_sha256") == sha(lean_source)
                  and lean_receipt.get("log_sha256") == sha(lean_log)
                  and lean_receipt.get("status") == "PASS")
    record("lean_build_receipt", "Build completed successfully" in lean_text and "sorryAx" not in lean_text and no_placeholders and lean_fresh,
           f"Lean algebraic-core build; no placeholders={no_placeholders}; receipt_fresh={lean_fresh}")
    pdf = ROOT / "manuscript/ads2-rst-one-sided-flux.pdf"
    tex = ROOT / "manuscript/ads2-rst-one-sided-flux.tex"
    tectonic_log = ROOT / "outputs/tectonic-build.out"
    pdf_receipt = json.loads((ROOT / "outputs/tectonic-build.json").read_text())
    pdf_fresh = (pdf.is_file()
                 and pdf_receipt.get("tex_sha256") == sha(tex)
                 and pdf_receipt.get("pdf_sha256") == sha(pdf)
                 and pdf_receipt.get("log_sha256") == sha(tectonic_log)
                 and pdf_receipt.get("pdf_bytes") == pdf.stat().st_size
                 and pdf_receipt.get("status") == "PASS")
    record("manuscript_pdf_receipt", pdf.is_file() and pdf.stat().st_size > 10000 and "Writing `./ads2-rst-one-sided-flux.pdf`" in tectonic_log.read_text() and pdf_fresh,
           f"pdf_bytes={pdf.stat().st_size if pdf.exists() else 0}; receipt_fresh={pdf_fresh}")
    record("manifest_readback", len(actual_files) == len(artifacts) and not mismatches,
           f"mode={'read-only' if read_only else 'regenerated'}; disk_files={len(actual_files)}; manifest_files={len(artifacts)}; mismatches={mismatches}")
    failures = [row for row in checks if not row["pass"]]
    validation = {
        "schema": "ads2-rst.review-package.final-validation.v1",
        "captured_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "manifest_sha256": sha(MANIFEST),
        "checks": checks,
        "totals": {"checks": len(checks), "passed": sum(row["pass"] for row in checks), "failed": len(failures)},
        "failures": failures,
        "warnings": [
            "External human scientific review is not performed.",
            "Literature finding is bounded absence of evidence, not exhaustive priority.",
            "Interior observer proper time is not a future-asymptotic boundary-observer theorem.",
        ],
        "status": "PASS" if not failures else "FAIL",
        "archive_status": archive_status,
        "archive_verified": archive_status == "verified",
        "external_formal_review_performed": False,
    }
    if not read_only:
        VALIDATION.write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(validation, indent=2))
    print(f"MANIFEST_ARTIFACTS {len(artifacts)}")
    print(f"MANIFEST_MISMATCHES {mismatches}")
    print(f"RELATIVE_LINKS {links}; UNRESOLVED {len(unresolved)}")
    raise SystemExit(1 if failures or mismatches else 0)


if __name__ == "__main__":
    main()
