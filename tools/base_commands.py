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


def get_all_data():
    cursor.execute("SELECT * FROM todo_list")
    rows = cursor.fetchall()
    return [{
        'id': row[0],
        'name': row[1],
        'description': row[2],
        'is_active': row[3],

    }
        for row in rows]


def get_object_by_id(todo_id):
    cursor.execute("SELECT * FROM todo_list WHERE id = ?", (todo_id,))
    row = cursor.fetchone()
    return {
        'id': row[0],
        'name': row[1],
        'description': row[2],
        'is_active': row[3],
    }


def delete_object_by_id(todo_id):
    cursor.execute("DELETE FROM todo_list WHERE id = ?", (todo_id,))
    conn.commit()


def complete_object_by_id(todo_id, choice):
    cursor.execute('UPDATE todo_list SET is_active = ? WHERE id = ?', (choice, todo_id))
    conn.commit()


def change_todo_name_by_id(todo_id, name):
    cursor.execute('UPDATE todo_list SET name = ? WHERE id = ?', (name, todo_id))
    conn.commit()


def change_todo_description_by_id(todo_id, description):
    cursor.execute('UPDATE todo_list SET description = ? WHERE id = ?', (description, todo_id))
    conn.commit()
