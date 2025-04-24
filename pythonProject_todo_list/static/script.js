document.addEventListener('DOMContentLoaded', () => {
    loadTasks();
    setupDragAndDrop();
});

function loadTasks() {
    fetch('/tasks')
        .then(response => response.json())
        .then(tasks => {
            ['todo', 'in-progress', 'done'].forEach(status => {
                document.getElementById(status).innerHTML = `<h2>${status.replace('-', ' ').toUpperCase()}</h2>`;
            });
            tasks.forEach(task => {
                addTaskToColumn(task);
            });
        });
}

function addTask() {
    const title = document.getElementById('task-title').value;
    const description = document.getElementById('task-description').value;
    const status = document.getElementById('task-status').value;
    if (!title) return alert('Title is required!');

    fetch('/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, description, status })
    })
    .then(response => response.json())
    .then(task => {
        addTaskToColumn(task);
        document.getElementById('task-title').value = '';
        document.getElementById('task-description').value = '';
        document.getElementById('task-status').value = 'To Do';
        // Close the modal
        const modalElement = document.getElementById('task-modal');
        const modalInstance = bootstrap.Modal.getInstance(modalElement);
        if (modalInstance) modalInstance.hide();
    });
}

function editTask(id) {
    const card = document.querySelector(`[data-id="${id}"]`);
    const oldTitle = card.querySelector('h5').innerText;
    const oldDescription = card.querySelector('p').innerText;
    const oldStatus = getStatusFromColumn(card.parentElement.id);

    const title = prompt('Enter new title:', oldTitle);
    if (title === null) return;
    const description = prompt('Enter new description:', oldDescription);
    if (description === null) return;
    const status = prompt('Enter new status (To Do, In Progress, Done):', oldStatus);
    if (status === null) return;

    fetch(`/tasks/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, description, status })
    })
    .then(response => response.json())
    .then(task => {
        card.remove();
        addTaskToColumn(task);
    });
}

function getStatusFromColumn(columnId) {
    if (columnId === 'todo') return 'To Do';
    if (columnId === 'in-progress') return 'In Progress';
    if (columnId === 'done') return 'Done';
    return 'To Do';
}

function deleteTask(id) {
    if (confirm('Delete this task?')) {
        fetch(`/tasks/${id}`, {
            method: 'DELETE'
        })
        .then(() => {
            document.querySelector(`[data-id="${id}"]`).remove();
        });
    }
}

function addTaskToColumn(task) {
    let columnId;
    if (task.status === "To Do") columnId = "todo";
    else if (task.status === "In Progress") columnId = "in-progress";
    else if (task.status === "Done") columnId = "done";
    else columnId = task.status.toLowerCase().replace(' ', '-');

    const column = document.getElementById(columnId);
    if (!column) return;

    const taskCard = document.createElement('div');
    taskCard.className = 'task-card';
    taskCard.setAttribute('draggable', 'true');
    taskCard.setAttribute('data-id', task.id);
    taskCard.innerHTML = `
        <h5>${task.title}</h5>
        <p>${task.description || ''}</p>
        <button class="btn btn-edit btn-sm" onclick="editTask(${task.id})">Edit</button>
        <button class="btn btn-delete btn-sm" onclick="deleteTask(${task.id})">Delete</button>
    `;
    column.appendChild(taskCard);
}

function setupDragAndDrop() {
    const columns = document.querySelectorAll('.column');
    columns.forEach(column => {
        column.addEventListener('dragover', e => e.preventDefault());
        column.addEventListener('drop', e => {
            e.preventDefault();
            const taskId = e.dataTransfer.getData('text/plain');
            const taskCard = document.querySelector(`[data-id="${taskId}"]`);
            const newStatus = getStatusFromColumn(column.id);
            fetch(`/tasks/${taskId}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ status: newStatus })
            })
            .then(response => response.json())
            .then(task => {
                taskCard.remove();
                addTaskToColumn(task);
            });
        });
    });

    document.addEventListener('dragstart', e => {
        if (e.target.classList.contains('task-card')) {
            e.dataTransfer.setData('text/plain', e.target.dataset.id);
        }
    });
}
