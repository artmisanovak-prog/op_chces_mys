#!/usr/bin/env python3
"""Download and validate the public ARC-AGI-2 dataset; keep splits separate."""
import argparse, json, shutil, urllib.request, zipfile
from pathlib import Path

URL = "https://github.com/arcprize/ARC-AGI-2/archive/refs/heads/main.zip"
UPSTREAM = "ARC-AGI-2-main"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", default="data/arc-agi-2")
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args()
    root = Path(args.workspace).resolve()
    source = root / "source"
    if args.refresh and source.exists():
        shutil.rmtree(source)
    if not (source / "data" / "training").exists():
        root.mkdir(parents=True, exist_ok=True)
        archive = root / "arc-agi-2.zip"
        req = urllib.request.Request(URL, headers={"User-Agent":"MOUSE-ARC-Lab/1.0"})
        print("Downloading official ARC-AGI-2 repository...")
        with urllib.request.urlopen(req, timeout=180) as response, archive.open("wb") as out:
            shutil.copyfileobj(response, out)
        temp = root / "_extract"
        if temp.exists(): shutil.rmtree(temp)
        temp.mkdir()
        with zipfile.ZipFile(archive) as zf: zf.extractall(temp)
        extracted = temp / UPSTREAM
        if not extracted.exists(): raise RuntimeError("Upstream archive layout changed.")
        if source.exists(): shutil.rmtree(source)
        shutil.move(str(extracted), str(source))
        shutil.rmtree(temp)
        archive.unlink(missing_ok=True)
    manifest = {"source":"https://github.com/arcprize/ARC-AGI-2",
                "revision":"main at download time",
                "training_dir":"source/data/training",
                "evaluation_dir":"source/data/evaluation"}
    for split in ("training","evaluation"):
        folder = source / "data" / split
        files = sorted(folder.glob("*.json"))
        valid, invalid = 0, []
        for p in files:
            try:
                obj = json.loads(p.read_text(encoding="utf-8"))
                assert isinstance(obj.get("train"), list) and isinstance(obj.get("test"), list)
                valid += 1
            except Exception as exc: invalid.append({"file":p.name,"error":str(exc)})
        manifest[split] = {"json_files":len(files),"valid":valid,"invalid":invalid}
    (root / "manifest.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
    print(json.dumps(manifest,indent=2))
    if not manifest["training"]["valid"]: raise SystemExit("No valid training tasks found.")

if __name__ == "__main__": main()
