import sqlite3

conn = sqlite3.connect(f'ToDo.sqlite')

c = conn.cursor()

cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS todo_list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    is_active INTEGER NOT NULL
)
''')


def insert_data(name, description, is_active):
    cursor.execute('''
    INSERT INTO todo_list(name, description, is_active) VALUES (?, ?, ?)
    ''', (name, description, is_active))
    conn.commit()

