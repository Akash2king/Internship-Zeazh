import sqlite3

def insert_user(name, email):
    conn = sqlite3.connect('user_tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (name, email)
    VALUES (?, ?);
    ''', (name, email))
    conn.commit()
    conn.close()

    print(f"User {name} added successfully!")

def insert_task(user_id, task_description):
    conn = sqlite3.connect('user_tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO tasks (user_id, task_description, completed)
    VALUES (?, ?, ?);
    ''', (user_id, task_description, 0))  # 0 means not completed
    conn.commit()
    conn.close()

    print(f"Task '{task_description}' added successfully!")

# Example usage
insert_user("John Doe", "john@example.com")
insert_task(1, "Finish the report")
insert_task(1, "Clean the office")
