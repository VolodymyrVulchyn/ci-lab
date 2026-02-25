from pathlib import Path
from datetime import datetime

def main():
    out_dir = Path("artifacts") / "visualization"
    out_dir.mkdir(parents=True, exist_ok=True)

    html = f"""
    <html>
      <body>
        <h1>Visualization</h1>
        <p>Generated at {datetime.now()}</p>
      </body>
    </html>
    """.strip()

    (out_dir / "index.html").write_text(html, encoding="utf-8")

if __name__ == "__main__":
    main()