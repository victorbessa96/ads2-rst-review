#!/usr/bin/env python3
"""Rebuild Archive.zip from the current manifest and write Archive.zip.sha256.

The archive holds every manifest artifact plus manifest.json and validation.json
under the folder "To review/".  run_verification.sh calls this around the
validator, because the validator both writes the manifest and checks the archive.
"""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parent
names = [row["path"] for row in json.loads((ROOT / "manifest.json").read_text())["artifacts"]]
names += ["manifest.json", "validation.json"]
archive = ROOT / "Archive.zip"
with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as bundle:
    for name in sorted(names):
        bundle.write(ROOT / name, "To review/" + name)
digest = hashlib.sha256(archive.read_bytes()).hexdigest()
(ROOT / "Archive.zip.sha256").write_text(f"{digest}  Archive.zip\n")
print(f"Archive.zip: {len(names)} members, sha256 {digest}")
