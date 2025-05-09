import sqlite3
from config import DB_PATH

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS motion_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT NOT NULL,
                    message TEXT NOT NULL
                )
            ''')

    def insert_event(self, timestamp, message):
        with self.conn:
            self.conn.execute('''
                INSERT INTO motion_events (timestamp, message)
                VALUES (?, ?)
            ''', (timestamp, message))
