// Get elements
const taskList = document.getElementById('task-list');
const newTaskInput = document.getElementById('new-task-input');
const addTaskBtn = document.getElementById('add-task-btn');

// Add a new task
addTaskBtn.addEventListener('click', () => {
    const taskText = newTaskInput.value.trim();

    if (taskText === "") {
        alert("Please enter a task.");
        return;
    }

    const taskItem = document.createElement('li');

    // Create checkbox
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.className = 'task-checkbox';
    checkbox.addEventListener('change', () => {
        taskItem.classList.toggle('completed', checkbox.checked);
    });

    // Create task text
    const taskTextElement = document.createElement('h2');
    taskTextElement.textContent = taskText;

    // Create buttons
    const buttons = document.createElement('div');
    buttons.className = 'buttons';

    // Edit button
    const editBtn = document.createElement('input');
    editBtn.type = 'button';
    editBtn.value = 'Edit';
    editBtn.addEventListener('click', () => {
        const newTaskText = prompt("Edit your task:", taskTextElement.textContent);
        if (newTaskText !== null) {
            taskTextElement.textContent = newTaskText;
        }
    });

    // Delete button
    const deleteBtn = document.createElement('input');
    deleteBtn.type = 'button';
    deleteBtn.value = 'Delete';
    deleteBtn.addEventListener('click', () => {
        taskList.removeChild(taskItem);
    });

    // Append elements to the task item
    buttons.appendChild(editBtn);
    buttons.appendChild(deleteBtn);
    taskItem.appendChild(checkbox);
    taskItem.appendChild(taskTextElement);
    taskItem.appendChild(buttons);

    // Add task item to the list
    taskList.appendChild(taskItem);

    // Clear input field
    newTaskInput.value = '';
});
