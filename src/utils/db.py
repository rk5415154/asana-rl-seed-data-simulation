import sqlite3
from pathlib import Path


def get_connection(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def execute_schema(conn, schema_path: str):
    schema_sql = Path(schema_path).read_text()
    conn.executescript(schema_sql)
    conn.commit()

