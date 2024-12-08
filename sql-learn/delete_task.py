import sqlite3

def delete_task(task_id):
    conn = sqlite3.connect('user_tasks.db')
    cursor = conn.cursor()

    cursor.execute('''
    DELETE FROM tasks
    WHERE id = ?;
    ''', (task_id,))

    conn.commit()
    conn.close()

    print(f"Task {task_id} deleted successfully.")

delete_task(2) 
