import sqlite3

def mark_task_completed(task_id):
    conn = sqlite3.connect('user_tasks.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE tasks
    SET completed = 1
    WHERE id = ?;
    ''', (task_id,))

    conn.commit()
    conn.close()

    print(f"Task {task_id} marked as completed.")

mark_task_completed(2)  
