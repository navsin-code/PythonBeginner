# 📝 Flask To-Do List Web App

A simple yet functional web-based To-Do list application built using **Flask**, **SQLite**, and **SQLAlchemy**. It provides full CRUD (Create, Read, Update, Delete) functionality through a clean REST API and renders an HTML interface using Jinja templates.

## ✅ Features

- Create new tasks with title and optional description.
- View all tasks via API or frontend.
- Update task details and status (`To Do`, `In Progress`, `Done`).
- Delete tasks.
- RESTful API endpoints (GET, POST, PUT, DELETE).

## 🚀 Technologies Used

- Python 3
- Flask (Web Framework)
- SQLAlchemy (ORM)
- SQLite (Database)
- HTML (for `index.html` frontend)

## 📁 Folder Structure

```

your\_project/
│
├── app.py                # Main Flask application
├── tasks.db              # SQLite database (auto-created)
└── templates/
└── index.html        # HTML template

````

## ⚙️ Setup Instructions

### 1. Clone the Repository or Copy Files

```bash
git clone https://github.com/yourusername/flask-todo-app.git
cd flask-todo-app
````

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install Flask Flask-SQLAlchemy
```

### 4. Run the App

```bash
python app.py
```

The app will run on: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## 🔄 API Endpoints

| Method | Endpoint      | Description            |
| ------ | ------------- | ---------------------- |
| GET    | `/tasks`      | Fetch all tasks        |
| POST   | `/tasks`      | Add a new task         |
| PUT    | `/tasks/<id>` | Update a specific task |
| DELETE | `/tasks/<id>` | Delete a task          |

### Sample JSON for POST/PUT:

```json
{
  "title": "Buy groceries",
  "description": "Milk, Bread, Eggs",
  "status": "In Progress"
}
```

## ✨ Example Task Object

```json
{
  "id": 1,
  "title": "Complete project",
  "description": "Finish the Flask To-Do App",
  "status": "Done"
}
```

---

## 💡 Notes

* The database is auto-generated on first run as `tasks.db`.
* You can customize the task statuses and UI via `index.html`.


