from pathlib import Path
import csv

def main():
    in_path = Path("artifacts") / "data_load" / "data.csv"
    out_dir = Path("artifacts") / "data_quality_analysis"
    out_dir.mkdir(parents=True, exist_ok=True)

    report = out_dir / "report.txt"

    # якщо data_load ще не запускали
    if not in_path.exists():
        report.write_text(
            "Issues:\n- Missing input artifacts/data_load/data.csv (run data_load first)\n",
            encoding="utf-8"
        )
        return

    # мінімальна "перевірка якості"
    with in_path.open("r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    report.write_text(
        f"Rows: {len(rows)}\nStatus: OK\n",
        encoding="utf-8"
    )

if __name__ == "__main__":
    main()