import sqlite3
conn = sqlite3.connect('user_tasks.db')

cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    task_description TEXT NOT NULL,
    completed BOOLEAN NOT NULL CHECK (completed IN (0, 1)),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully!")
