import csv
from pathlib import Path
from urllib.request import urlretrieve

HERE = Path(__file__).resolve().parent
CSV_PATH = HERE / "books.csv"
BOOKS_DIR = HERE / "books"


def pdf_name(title: str, pdf_url: str) -> str:
    name = title.strip() or Path(pdf_url).name
    safe = "".join(c if c.isalnum() or c in " -_+" else "_" for c in name).strip()
    if not safe.lower().endswith(".pdf"):
        safe += ".pdf"
    return safe


def main() -> None:
    BOOKS_DIR.mkdir(exist_ok=True)
    with CSV_PATH.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            print("row: ", row)
            url = row["pdf_url"].strip()
            print("url: ", url)
            dest = BOOKS_DIR / pdf_name(row["title"], url)
            print("dest: ", dest)
            if dest.exists():
                print(f"already have {dest.name}")
                continue
            #print(f"downloading {dest.name}")
            #urlretrieve(url, dest)
            #print(f"saved {dest}")


if __name__ == "__main__":
    main()
