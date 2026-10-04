from pathlib import Path

from markitdown import MarkItDown

HERE = Path(__file__).resolve().parent
BOOKS_DIR = HERE / "books"
TEXT_DIR = HERE / "books_text"


def main() -> None:
    TEXT_DIR.mkdir(exist_ok=True)
    converter = MarkItDown()

    for pdf in sorted(BOOKS_DIR.glob("*.pdf")):
        dest = TEXT_DIR / f"{pdf.stem}.md"
        print(f"converting {pdf.name}")
        result = converter.convert(str(pdf))
        dest.write_text(result.text_content, encoding="utf-8")
        print(f"saved {dest.name}")


if __name__ == "__main__":
    main()
