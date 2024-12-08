from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row  # To access columns by name
    return conn

# Home route to display tasks
@app.route('/')
def index():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task_description = request.form['task_description']
    if task_description:
        conn = get_db_connection()
        conn.execute('INSERT INTO tasks (task_description, completed) VALUES (?, ?)', 
                     (task_description, 0))  # 0 means incomplete
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

# Route to mark a task as completed
@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    conn = get_db_connection()
    conn.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Route to delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Route to edit a task
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    conn = get_db_connection()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    if request.method == 'POST':
        task_description = request.form['task_description']
        if task_description:
            conn.execute('UPDATE tasks SET task_description = ? WHERE id = ?', 
                         (task_description, task_id))
            conn.commit()
        return redirect(url_for('index'))
    conn.close()
    return render_template('edit_task.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)
