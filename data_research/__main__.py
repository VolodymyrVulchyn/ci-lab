from pathlib import Path
from datetime import datetime

def main():
    out_dir = Path("artifacts") / "data_research"
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "summary.md").write_text(
        f"# Data research\n\nGenerated at {datetime.now()}\n",
        encoding="utf-8"
    )

if __name__ == "__main__":
    main()