"""Inventura skutečných polí CASMI parquetů bez načítání celého train do RAM."""
import argparse, json
from collections import Counter
from pathlib import Path
import pyarrow.parquet as pq
import pandas as pd

def inspect(path, batch_size=50000):
    pf = pq.ParquetFile(path)
    report = {
        "file": str(path),
        "rows_metadata": pf.metadata.num_rows,
        "row_groups": pf.metadata.num_row_groups,
        "columns": [{"name": f.name, "type": str(f.type), "nullable": f.nullable}
                    for f in pf.schema_arrow],
        "null_counts": Counter(),
        "distinct": {},
        "rows_scanned": 0,
        "peak_count": {"n": 0, "min": None, "median_sample": None, "max": None},
    }
    distinct_cols = [c for c in [
        "molecule_id", "spectrum_id", "normalized_smiles", "adduct",
        "ionization_mode", "ingest_lib"
    ] if c in pf.schema_arrow.names]
    sets = {c: set() for c in distinct_cols}
    peak_lengths = []
    for batch in pf.iter_batches(batch_size=batch_size):
        df = batch.to_pandas()
        report["rows_scanned"] += len(df)
        for c in df.columns:
            report["null_counts"][c] += int(df[c].isna().sum())
        for c in distinct_cols:
            vals = df[c].dropna().astype(str).unique()
            sets[c].update(vals.tolist())
        if "ms2_mzs" in df.columns:
            peak_lengths.extend(df["ms2_mzs"].dropna().map(len).tolist())
    report["null_counts"] = dict(report["null_counts"])
    report["distinct"] = {k: len(v) for k, v in sets.items()}
    if peak_lengths:
        s = pd.Series(peak_lengths)
        report["peak_count"] = {
            "n": len(peak_lengths), "min": int(s.min()),
            "median_sample": float(s.median()), "max": int(s.max())
        }
    for c in ["adduct", "ionization_mode", "ingest_lib"]:
        if c in pf.schema_arrow.names:
            counts = Counter()
            for batch in pf.iter_batches(batch_size=batch_size, columns=[c]):
                counts.update(str(v) for v in batch.column(0).to_pylist() if v is not None)
            report[c + "_counts"] = dict(counts.most_common())
    return report

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--data-dir", required=True)
    ap.add_argument("--out", default="data_inventory.json")
    args=ap.parse_args()
    root=Path(args.data_dir)
    reports={}
    for name in ["train.parquet","test.parquet"]:
        p=root/name
        if p.exists():
            reports[name]=inspect(p)
        else:
            reports[name]={"missing":True,"path":str(p)}
    sample=root/"sample_submission.csv"
    if sample.exists():
        df=pd.read_csv(sample,dtype={"molecule_id":str})
        reports["sample_submission"]={
            "rows":len(df),"columns":list(df.columns),
            "unique_molecule_ids":int(df.molecule_id.nunique())
            if "molecule_id" in df else None
        }
    Path(args.out).write_text(json.dumps(reports,indent=2,ensure_ascii=False),encoding="utf-8")
    print(json.dumps(reports,indent=2,ensure_ascii=False))
if __name__=="__main__": main()
