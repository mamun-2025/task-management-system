
# Django Task Manager

A Task Management Web Application built with Django.
This project is being developed step-by-step to practice Django backend development.

---

## 🚀 Project Goal

The goal of this project is to learn an implement:
- Django Backend Development
- Authentication System
- CRUD Operations
- Responsive UI Improvement
- Database Upgrade
- REST API
- Deployment

---

## 🛠 Tech Stack

 Backend:
 - Python 
 - Django

Database:
- SQLite (Development)
- PostgreSQL (Planned)

Frontend:
- HTML
- Tailwind CSS v4
- JavaScript

Tools:
- Git
- Github
- VS Code

---

## 📂 Project Structure

Task-Management-System/
│
├── README.md                <-- Project documentation and setup guide
│
└── task_manager/            <-- Main project directory
    ├── core/                <-- Project configuration (settings.py, urls.py)
    ├── tasks/               <-- Main application logic
    │   ├── static/          <-- CSS/JS assets (Tailwind output.css)
    │   ├── templates/       <-- HTML templates (base.html, dashboard.html)
    │   ├── forms.py         <-- Django ModelForms styled with Tailwind
    │   ├── models.py        <-- Task database models
    │   └── views.py         <-- Dashboard logic and task views
    ├── manage.py            <-- Django's command-line utility
    ├── node_modules/        <-- Tailwind CSS v4 dependencies (Local only)
    ├── package.json         <-- NPM script configurations
    └── package-lock.json    <-- Locked versions of frontend dependencies
    ├── .gitignore               <-- Specifies ignored files (venv, node_modules, etc.)
    
--- 

## ⚙️ Environment Setup

Create virtual environment:
python -m venv venv

Activate virtual environment:
Windows:
venv\Scripts\activate

Install dependencies:
pip install django

---

## 📅 Development Progress

# ✅ Step 1: Project Setup
Completed:

- python installed
- Django installed
- Django project created
- Django app created
- Python migrations
- Development server running
- superuser created

Commands Used:
```bash
pip installed django
django-admin startprject taks_manager
cd task_manager
python manage.py startapp tasks
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser

Status: ✅ Completed

# ⏳ Step 2: Authentication System
Implemented Features:

- User Signup
- User Login
- User Logout
- Authentication Forms
- Basic Authentication Templates

Status: ✅ Completed

# ⏳ Step 3: Task Management (CRUD)

Planned Features:
- Create Task
- View Task
- Update Task
- Delete Task

### Task Model 
- Fields: titile, description, status, priority, due_date, created_at
- Each task is linked to a user(ForeignKey)
- Status Choices: Pending, In Progress, Completed
- Priority Choices: Low, Medium, High

### Task Form
- TaskForm(ModelForm) for handling task creation and update

### URLs
- `/` → Task List
- `/task/create/` → Create Task
- `/task/<id>/update/` → Update Task
- `/task/<id>/delete/` → Delete Task

### Templates
- `task_list.html` → List all tasks
- `task_form.html` → Create / Update task
- `task_confirm_delete.html` → Confirm task deletion

Status: ✅ Completed

# ⏳ Step 4: UI Improvement

- Implemented Features:
- Responsive design
- Clean UI

Status: ✅ Completed


```

# ⏳ Step 5: Database Upgrade

Planned Features:
- Configure PostgreSQL
- Connect Django with PostgreSQL
- Migrate database from SQLite to PostgreSQL

Status: 🔄 In Progress


## ⏳ Step 6: REST API (Django REST Framework)
Planned Features:

- Task API
- Authentication API
- API endpoints for CRUD operations

Status: ⏳ Pending

---

## 👨‍💻 Author
- Mamun_Bepari
- Aspiring Backend Developer (Python & Django)



