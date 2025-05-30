from lib.models import CURSOR, CONN

class User:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
        """)
        CONN.commit()

    def save(self):
        CURSOR.execute("INSERT INTO users (name) VALUES (?)", (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM users")
        return CURSOR.fetchall()

    @classmethod
    def find_by_name(cls, name):
        CURSOR.execute("SELECT * FROM users WHERE name = ?", (name,))
        row = CURSOR.fetchone()
        if row:
            return User(id=row[0], name=row[1])
        return None
