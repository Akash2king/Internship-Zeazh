import sqlite3

def view_tasks(user_id):
    conn = sqlite3.connect('user_tasks.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT tasks.id, tasks.task_description, tasks.completed
    FROM tasks
    WHERE tasks.user_id = ?;
    ''', (user_id,))
    tasks = cursor.fetchall()

    if tasks:
        print(f"Tasks for User ID {user_id}:")
       
        for task in tasks:
            
            task_id, task_description, completed = task
            status = "Completed" if completed else "Not Completed"
            print(f"{task_id}. {task_description} - {status}")
    else:
        print(f"No tasks found for User ID {user_id}")

    conn.close()

view_tasks(1)  
