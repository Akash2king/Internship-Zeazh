import sqlite3
conn = sqlite3.connect('todo.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_description TEXT NOT NULL,
    completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
);
''')
conn.commit()
conn.close()

print("Database and tasks table created successfully!")
