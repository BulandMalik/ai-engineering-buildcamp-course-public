import os
import urllib.request
from pathlib import Path

import duckdb

DATA_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"
PARQUET_FILE = "yellow_tripdata_2024-01.parquet"
DB_PATH = Path(__file__).resolve().parent / "taxi.db"

con = duckdb.connect(str(DB_PATH))


def setup_database():
    """Download the parquet file and load it into DuckDB."""
    if not os.path.exists(PARQUET_FILE):
        print(f"Downloading {DATA_URL}...")
        urllib.request.urlretrieve(DATA_URL, PARQUET_FILE)

    con.execute(f"""
        CREATE TABLE IF NOT EXISTS trips AS
        SELECT * FROM '{PARQUET_FILE}'
    """)
    count = con.execute("SELECT COUNT(*) FROM trips").fetchone()[0]
    print(f"Loaded {count} rows")
    return count


class SQLTools:
    """Read the trips schema and run SQL against the taxi database."""

    def __init__(self, db_path: str | Path = DB_PATH):
        self.db_path = str(db_path)

    def get_schema(self) -> str:
        """Run DESCRIBE trips and return every column name with its type.

        Call this before writing SQL. Each line is a column name followed by its type.
        """
        with duckdb.connect(self.db_path) as connection:
            rows = connection.execute("DESCRIBE trips").fetchall()
        return "\n".join(f"{name}: {column_type}" for name, column_type, *_rest in rows)

    def run_sql(self, query: str) -> str:
        """Execute one DuckDB SQL query and return the result as text.

        Args:
            query: SQL to run against the trips table.

        The text has a header line of column names, then up to 50 data rows.
        A failed query returns the error text instead of raising.
        """
        try:
            with duckdb.connect(self.db_path) as connection:
                result = connection.execute(query)
                columns = [desc[0] for desc in result.description]
                rows = result.fetchmany(50)
        except Exception as err:
            return f"SQL error: {err}"

        lines = [" | ".join(columns)]
        lines.extend(
            " | ".join("" if value is None else str(value) for value in row)
            for row in rows
        )
        return "\n".join(lines)


if __name__ == "__main__":
    from sql_tools import setup_database
    count = setup_database()
    print(count)