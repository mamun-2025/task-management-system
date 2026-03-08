
# Django Task Manager

A Task Management Web Application built with Django.
This project is being developed step-by-step to practice Django backend development.

---

## 🚀 Project Goal

The goal of this project is to learn an implement:
- Django Backend Development
- Authentication System
- CRUD Operations
- UI Improvement
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
- CSS
- JavaScript

Tools:
- Git
- Github
- VS Code

---

## 📂 Project Structure
Task-Management-System/
│
├── README.md
│
├── task_manager/                 # Main Django project folder
│
│   ├── task_manager/             # Django project settings
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── tasks/                    # Django app (Task management)
│   │
│   │   ├── migrations/
│   │   │
│   │   ├── templates/
│   │   │   └── tasks/
│   │   │        ├── login.html
│   │   │        └── signup.html
│   │   │
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests.py
│   │
│   ├── venv/                     # Virtual Environment
│   │
│   ├── .env                      # Environment variables
│   ├── .gitignore
│   ├── db.sqlite3
│   ├── manage.py
│   └── requirements.txt

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

```

# ⏳ Step 3: Task Management (CRUD)

Planned Features:
- Create Task
- View Task
- Update Task
- Delete Task

Status: 🔄 In Progress

# ⏳ Step 4: UI Improvement

- Planned Features:
- Responsive design
- Clean UI

Status: ⏳ Pending


# ⏳ Step 5: Database Upgrade

Planned Features:
- Configure PostgreSQL
- Connect Django with PostgreSQL
- Migrate database from SQLite to PostgreSQL

Status: ⏳ Pending


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



