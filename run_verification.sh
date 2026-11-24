#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
PYTHON="${PHYSICS_PYTHON:-python3}"
"$PYTHON" verify.py
"$PYTHON" independent_symbolic.py
"$PYTHON" advanced_checks.py
if [[ "${RUN_LEAN:-0}" == "1" ]]; then
  LAKE="${LAKE_BIN:-$(command -v lake || true)}"
  TECTONIC="${TECTONIC_BIN:-$(command -v tectonic || true)}"
  if [[ -z "$LAKE" || -z "$TECTONIC" ]]; then
    echo "RUN_LEAN=1 requires lake and tectonic on PATH, or LAKE_BIN/TECTONIC_BIN overrides." >&2
    exit 2
  fi
  (cd lean && "$LAKE" build > ../outputs/lean-build.out 2>&1)
  "$PYTHON" - <<'PY'
from pathlib import Path
import datetime, hashlib, json
root = Path.cwd()
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
source = root / "lean/AdS2RST.lean"
log = root / "outputs/lean-build.out"
receipt = {
    "schema": "ads2-rst.lean-build-receipt.v1",
    "created_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "source_sha256": sha(source),
    "log_sha256": sha(log),
    "command": "lake build",
    "status": "PASS" if "Build completed successfully" in log.read_text() else "FAIL",
}
(root / "outputs/lean-build.json").write_text(json.dumps(receipt, indent=2) + "\n")
PY
  (cd manuscript && "$TECTONIC" -X compile ads2-rst-one-sided-flux.tex --outdir . > ../outputs/tectonic-build.out 2>&1)
  "$PYTHON" - <<'PY'
from pathlib import Path
import datetime, hashlib, json
root = Path.cwd()
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
tex = root / "manuscript/ads2-rst-one-sided-flux.tex"
pdf = root / "manuscript/ads2-rst-one-sided-flux.pdf"
log = root / "outputs/tectonic-build.out"
receipt = {
    "schema": "ads2-rst.tectonic-build-receipt.v1",
    "created_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "tex_sha256": sha(tex),
    "pdf_sha256": sha(pdf),
    "pdf_bytes": pdf.stat().st_size,
    "log_sha256": sha(log),
    "command": "tectonic -X compile ads2-rst-one-sided-flux.tex --outdir .",
    "status": "PASS" if "Writing `./ads2-rst-one-sided-flux.pdf`" in log.read_text() else "FAIL",
}
(root / "outputs/tectonic-build.json").write_text(json.dumps(receipt, indent=2) + "\n")
PY
fi
SKIP_PRODUCERS=1 "$PYTHON" validate_package.py
