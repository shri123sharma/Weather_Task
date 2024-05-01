# # Welcome to Weather Project

A Django project for [brief description].

## Getting Started

Follow these instructions to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/shri123sharma/weather_api_project.git
```
### 2.Check Python Version
Make sure you have the required Python version installed. This project requires Python 3.7 or higher.

`python --version`==3.11.0

### 3. Create a Virtual Environment
Activate the virtual environment.

`cd weather_forecast/`
windows command:`python -m venv venv`

### 4. Activate the Virtual Environment
Activate the virtual environment.

windows : `venv\Scripts\activate`
linux :`source venv/bin/activate` 

### 5. Install Dependencies
Install the project dependencies from the requirements.txt file.

`pip install -r requirements.txt`

### 6.Apply database migrations to create/update your database schema:

```bash
    python manage.py makemigrations
    python manage.py migrate
```

### 7.Run the Development Server
Run the development server using the local settings.

`python manage.py runserver`

The development server will start, and you can access the application at 
[Localhost URL](http://127.0.0.1:8000/)

