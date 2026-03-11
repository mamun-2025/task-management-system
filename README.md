
# Django Task Manager

A Task Management Web Application built with Django.
Users can signup, login, create tasks, update tasks, and manage their daily work efficiently..

---

## 🚀 Project Goal

The goal of this project is to learn an implement:
- Django Backend Development
- Authentication System
- CRUD Operations
- Responsive UI Improvement
- PostgreSQL Database Integration
- REST API Development
- Deployment
- Advanced API Features(API Pagination,Search API,Filter API)

---

## 🛠 Tech Stack

 Backend:
 - Python 
 - Django
 - Django REST Framework(DRF)
 - JWT Authentication(DRF)

Database:
- SQLite (Development)
- PostgreSQL

Frontend:
- HTML
- Tailwind CSS v4
- JavaScript

Tools:
- Git
- Github
- VS Code

---

## ✨ Features

- User Authentication (Signup / Login / Logout)
- Task CRUD Operations
- Task Priority System
- Task Status Tracking
- Responsive UI with Tailwind CSS
- PostgreSQL Database Integration
- Environment Variables (.env)
- Django REST Framework APIs
- Token Authentication
- JWT Authentication
- Postman API Testing

---

## 📂 Project Structure

Task-Management-System/
│
├── README.md                <-- Project documentation and setup guide
│
└── task_manager/            <-- Main project directory(application)
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
    ├── .gitignore               <-- Specifies ignored files (venv, .env, node_modules, etc.)
    
--- 

## ⚙️ Environment Setup

Repository Clone:
git clone: https://github.com/mamun-2025/task-management-system 
cd Task-Management-System

Create virtual environment:
python -m venv venv

Activate virtual environment:
Windows:
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt
npm install
pip install django
pip install psycopg2-binary
pip install python-dotenv

Database Migrations:
python manage.py makemigrations 
python manage.py migrate

Tailwind built and runserver:
npm run dev

Server Run:
python manage.py runserver

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
pip install django
django-admin startprject tasks_manager
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

Implemented Features:
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

# ⏳ Step 5: Database Upgrade

Implemented Features:
- Configure PostgreSQL
- Connect Django with PostgreSQL
- Migrate database from SQLite to PostgreSQL

Status: ✅ Completed


## ⏳ Step 6: REST API Development (Django REST Framework)

Implemented Features:

- Created REST APIs using Django REST Framework (DRF)
- Implemented Task Serializer to convert model data into JSON
- Built CRUD API endpoints for tasks
- Added Token Authentication for secure API access
- Restricted API access using `IsAuthenticated` permission
- Each user can access only their own tasks
- Tested APIs using Postman

Status: ✅ Completed

⏳ Step 7: JWT Authentication (SimpleJWT)

Implemented Features:

1. Implemented JWT Authentication using Django REST Framework
2. Used Simple JWT for secure token-based authentication
3. Login API returns Access Token and Refresh Token
4. Access Token is used to access protected API endpoints
5. Refresh Token is used to generate a new Access Token
6. Added JWT authentication to DRF settings


## 🧪 API Testing (Postman)

All APIs were tested using Postman.

- Token Authentication Testing:
Steps 1:
Send POST request to
/api/login/

Get authentication token
Add token in header:
Authorization: Token your_token_here

Access protected endpoints such as:
/api/tasks/

- JWT Authentication Testing:
Steps 2:
Send POST request to
/api/token/
Body:

{
  "username": "admin",
  "password": "yourpassword"
}
Copy the access token
Add it in header:
Authorization: Bearer your_access_token

Test protected endpoints:
/api/tasks/
Refresh Token Testing

Send POST request to:
/api/token/refresh/
Body:

{
  "refresh": "your_refresh_token"
}

Response:

{
  "access": "new_access_token"
}

- API Testing Tools
Postman for API testing
Django Admin Panel for database management

Status: ✅ Completed

```

## ⏳ Step 8: Deployment
The project will be deployed using Render 
Planned Features:

- Connect GitHub repository to Render
- Deploy Django Project(Render)

Status: ⏳ In Progress

---

## ⏳ Step 9: Advanced API Features (Future Update)

Future improvements planned using Django REST Framework.
Planned Features:

- API Pagination
- Search API
- Filter API

Status: ⏳ Planned

---

## 📸 Screenshots
### Dashboard
![Dashboard](screenshots/Dashboard.png)

### Task List
![Task List](screenshots/task_list.png)

## 👨‍💻 Author

- [Mamun Bepari] 
- Aspiring Backend Developer (Python & Django)

GitHub: https://github.com/mamun-2025



