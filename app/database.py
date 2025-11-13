# app/database.py

import sqlite3
from app.config import DATABASE_PATH

class Database:
    def __init__(self, db_path=DATABASE_PATH):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        """Creates a table for authorized license plates if it doesn't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS authorized_plates (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    plate TEXT UNIQUE NOT NULL
                )
            """)
            conn.commit()

    def add_plate(self, plate: str):
        """Add a new authorized plate."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT OR IGNORE INTO authorized_plates (plate) VALUES (?)", (plate,))
            conn.commit()

    def remove_plate(self, plate: str):
        """Remove a plate from authorization."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM authorized_plates WHERE plate = ?", (plate,))
            conn.commit()

    def is_authorized(self, plate: str) -> bool:
        """Check if a plate is authorized."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM authorized_plates WHERE plate = ?", (plate,))
            return cursor.fetchone() is not None
