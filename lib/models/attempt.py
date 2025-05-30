from lib.models import CURSOR, CONN

class QuizAttempt:
    def __init__(self, user_id, score, id=None):
        self.id = id
        self.user_id = user_id
        self.score = score

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS quiz_attempts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                score INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id)
            );
        """)
        CONN.commit()

    def save(self):
        CURSOR.execute("""
            INSERT INTO quiz_attempts (user_id, score)
            VALUES (?, ?)
        """, (self.user_id, self.score))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM quiz_attempts")
        return CURSOR.fetchall()
