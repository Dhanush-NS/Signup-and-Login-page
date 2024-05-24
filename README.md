# Django Signup and Login Project

This project is a simple signup and login application built using Django, HTML, CSS, and JavaScript. The application includes client-side validation and uses a MySQL database for storing user information.

## Features

- User signup with form validation
- User login with form validation
- Client-side validation using JavaScript
- Backend powered by Django framework
- MySQL database for data storage

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- Python 3.x
- Django
- MySQL
- pip (Python package installer)

## Installation

Follow these steps to get the project up and running:

### 1. Clone the repository


- git clone https://github.com/Dhanush-NS/Signup-and-Login-page.git
- cd Signup-and-Login-page

## Create and activate a virtual environment
- python -m venv env
- pip install django mysqlclient


## Set up the MySQL database
- CREATE DATABASE login;
- use login;

## Update your Django project's settings to connect to the MySQL database. In project/settings.py, add the following:
- DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'login',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
## Make migrations and migrate

- cd jango/project
- py manage.py makemigrations app
- py manage.py migrate

## Run the development server
- py manage.py runserver

You should see the following output indicating that the server is running:

- Watching for file changes with StatReloader
 Performing system checks...

 System check identified no issues (0 silenced).
 May 22, 2024 - 18:00:00
 Django version 5.0.6, using settings 'project.settings'
 Starting development server at http://127.0.0.1:8000/
 Quit the server with CONTROL-C.

## Technologies Used
- Backend: Django
- Frontend: HTML, CSS, JavaScript
- Database: MySQL
- Other: pip (for package management)

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes.

## Contact

For any questions or suggestions, please contact [nsdhanush5@gmail.com].

Replace `https://github.com/Dhanush-NS/Signup-and-Login-page.git`

This README file should provide clear instructions for setting up and running your project. Feel free to customize it further based on your project's needs.
a
