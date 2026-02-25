from datetime import datetime
from pathlib import Path

def main():
    out_dir = Path("artifacts") / "data_load"
    out_dir.mkdir(parents=True, exist_ok=True)

    # лог запуску
    (out_dir / "run.log").write_text(
        f"[data_load] OK at {datetime.now()}\n",
        encoding="utf-8"
    )

    # приклад "даних" для наступних модулів
    (out_dir / "data.csv").write_text(
        "id,value\n1,10\n2,20\n",
        encoding="utf-8"
    )
# тест на виконання одного модуля
if __name__ == "__main__":
    main()