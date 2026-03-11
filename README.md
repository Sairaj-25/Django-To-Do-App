# 📝 Django To-Do Application

![Python Version](https://img.shields.io/badge/python-3.12-blue.svg)
![Django Version](https://img.shields.io/badge/django-5.1.4-green.svg)
![CI/CD](https://github.com/Sairaj-25/To_do_Django/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A robust, full-stack To-Do list web application built with Python and Django. This project features secure user authentication, efficient task management, and a clean, responsive UI built with Bootstrap 5. It is equipped with a modern CI/CD pipeline ensuring code quality, security, and test coverage.

## 🚀 Features

- **User Authentication:** Secure registration, login, and logout functionality.
- **Task Management:** Create, view, update (planned), and delete personal tasks.
- **Search Functionality:** Quickly filter tasks by title.
- **Due Date Tracking:** Keep track of task deadlines visually.
- **Responsive UI:** Clean frontend powered by Bootstrap 5 and custom CSS.
- **Automated CI/CD:** GitHub Actions integration for code linting (Flake8), formatting (Black), security scanning (Bandit), and testing (Coverage).

## 🧰 Tech Stack

- **Backend:** Python 3.12, Django 5.1.4
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (Default)
- **DevOps/CI:** GitHub Actions, Black, Flake8, Bandit, Coverage
- **Environment Management:** `django-environ`

---

## 📁 Repository Structure

```text
To_do_Django/
│
├── Todo/                   # Main Django project settings
│   ├── settings.py
│   ├── urls.py
|   ├── asgi.py
│   └── wsgi.py 
│
├── todoapp/                # Main Application Logic
|   ├── admin.py
|   ├── apps.py
│   ├── models.py           # Database schemas
│   ├── views.py            # Business logic and routing
│   ├── forms.py            # Form handling
│   └── urls.py             # App-level routing
│
├── static/                 # CSS, images, and static assets
├── templates/              # HTML templates (Login, Register, Dashboard)
├── .github/workflows/      # CI/CD Pipeline configurations
├── manage.py               # Django project entry point
├── requirements.txt        # Python dependency list
└── .env.example            # Example environment variables
```

🏁 Getting Started
### 1. Prerequisites
- Ensure you have the following installed on your local machine:

1. Python 3.10+

2. Git

### 2. Clone the Repository
```Bash
git clone [https://github.com/Sairaj-25/To_do_Django.git](https://github.com/Sairaj-25/To_do_Django.git)
cd To_do_Django
```

### 3. Setup Virtual Environment
- It is highly recommended to use a virtual environment to manage project dependencies.

```bash
python -m venv env
```

- Activate the virtual environment
# On Windows:
```
env\Scripts\activate
```
# On macOS/Linux:
```
source env/bin/activate
```
### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Environment Variables
- Create a .env file in the root directory of your project to securely store your secrets.

```Code snippet
# .env
DJANGO_SECRET_KEY=your_super_secret_key_here
DEBUG=True
(Note: Never commit your actual .env file to version control. It is already included in .gitignore.)
```

### 6. Run Database Migrations
-Initialize the SQLite database with Django's built-in schema:

```bash
python manage.py makemigrations
```
```
python manage.py migrate
```

### 7. Create a Superuser (Optional)
- To access the Django admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server
```bash
python manage.py runserver
```
- Open your web browser and navigate to http://127.0.0.1:8000/.

🛡️ CI/CD Pipeline & Testing
- This project uses GitHub Actions to enforce code quality and security on every push and pull request to the main branch.

- The pipeline automatically runs:

- Black: Code formatting check.

- Flake8: Syntax and style linting.

- Bandit: Automated security scanning for common vulnerabilities.

- Coverage: Runs Django tests and generates a test coverage report (uploaded as a workflow artifact).

- To run these tools locally:

```bash
# Format code
black .
```

```
# Run linter
flake8 .
```
```
# Run security scan
bandit -r . -ll -ii -x "venv,env,tests"
```

```
# Run tests with coverage
coverage run manage.py test
```
```
coverage report -m
```
💡 Roadmap / Next Enhancements

- [x] Add task editing functionality (edit_task view integration).

- [ ] Implement AJAX for seamless, page-reload-free task updates.

- [ ] Add pagination for users with long task lists.

- [ ] Implement task categorization and priority tags.

- [ ] Containerize the application using Docker.

- [ ] Deploy to a production cloud environment (e.g., AWS, Render, or Railway).

📌 License
- This project is open-source and available under the MIT License. Feel free to fork, modify, and use it for your own projects.
