📝 Django To-Do App

A full-stack To-Do list web application built using Python & Django — featuring user authentication, task creation, and task management in a clean and intuitive interface.

🚀 Features

✔ User registration & login
✔ Add new tasks
✔ View existing tasks
✔ Mark tasks as completed
✔ Delete tasks when done
✔ Uses Django templates with HTML & CSS
✔ Simple and responsive UI

🧰 Technology Used

Python (backend logic)

Django (framework)

HTML, CSS (front-end)

SQLite (default Django database)

Django-environ for secure environment configuration (if enabled)

📁 Repository Structure
To_do_Django/

│
├── Todo/ # Main Django project

│   ├── settings.py

│   ├── urls.py

│   └── wsgi.py

│
├── todoapp/              # To-Do app

│   ├── models.py

│   ├── views.py

│   ├── urls.py

│   └── templates/
│
├── static/               # CSS, images, static files

├── templates/            # Shared templates

├── manage.py             # Django project entry point

├── requirements.txt      # Python dependency list

└── .gitignore

🏁 Getting Started
🔹 Pre-requisites

Ensure you have Python 3.x and pip installed.

🔹 Clone the repository
git clone https://github.com/Sairaj-25/To_do_Django.git
cd To_do_Django

🔹 Create & activate virtual environment
python -m venv env
env\Scripts\activate         # Windows
# source env/bin/activate    # macOS / Linux

🔹 Install dependencies
pip install -r requirements.txt

🔹 Migrate the database
python manage.py migrate

🔹 Create a superuser (optional)
python manage.py createsuperuser


Follow the prompts to set username, email & password.

🔹 Run the development server
python manage.py runserver


Open your browser and visit:

http://127.0.0.1:8000/

🔐 Environment Variables (Optional)

If you want to hide sensitive settings like SECRET_KEY or email passwords using django-environ, create a .env file in the project root and add:

DJANGO_SECRET_KEY=your_secret_key_here
DEBUG=True


Then make sure .env is in .gitignore (so you don’t push secrets to GitHub)

🛠️ How It Works (High Level)

The app uses Django’s built-in authentication for login and registration.

Tasks are stored in the SQLite database using Django models.

Views handle user requests for task list, add, complete and delete.

Templates render the UI with dynamic data from views.

🐛 Troubleshooting

If you see errors like KeyError: DJANGO_SECRET_KEY, make sure you either:

✔ add a default secret in .env
✔ or set a fallback in settings.py temporarily:

SECRET_KEY = env("DJANGO_SECRET_KEY", default="unsafe-dev-key")

💡 Next Enhancements

✔ Add due dates & reminders
✔ Edit task feature
✔ AJAX for smoother UX
✔ Pagination for long task lists
✔ Task prioritization or categories
✔ Deploy to a cloud platform (Heroku, Railway, Render)

📌 License

This project is open-source and free to use.

🙌 Author

Sairaj Jadhav
