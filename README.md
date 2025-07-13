# Simple Django Portfolio
This is a basic personal portfolio website built with Django. It serves as a simple showcase for projects and provides a foundational structure for a web presence.

- Table of Contents
Description

- Features

- Setup Instructions

- Prerequisitess

- Installation

- Database Setup

- Running the Development Server

## Project Description

Usage

Contributing

License

Description
This project is a minimal Django application designed to serve as a personal online portfolio. It's built to be straightforward, focusing on demonstrating basic Django concepts like views, templates, and static file handling. It provides a clean starting point for showcasing your work.

Features
Home Page: A simple landing page.

Static File Handling: Properly configured to serve CSS (e.g., Bootstrap) and JavaScript assets locally.

Basic Project Structure: Follows Django's recommended app structure for maintainability.

Setup Instructions
Follow these steps to get the project up and running on your local machine.

Prerequisites
Before you begin, ensure you have the following installed:

Python 3.8+: Download from python.org

pip (Python package installer): Usually comes with Python.

Installation
Clone the repository (if it's in a Git repository):

git clone <your-repository-url>
cd mypersonalportfolio # Navigate into your project directory

If you don't have it in a repository, just navigate to your mypersonalportfolio project directory.

Create a virtual environment (highly recommended):

python -m venv venv

Activate the virtual environment:

On Windows:

.\venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Install Django and other dependencies:

pip install Django # Or pip install -r requirements.txt if you have one

(Note: If you plan to add more dependencies, create a requirements.txt file using pip freeze > requirements.txt and then install using pip install -r requirements.txt)

Database Setup
This project uses Django's default SQLite database, which requires no external setup.

Apply database migrations:

python manage.py migrate

This command will create the necessary database tables.

Running the Development Server
Start the Django development server:

python manage.py runserver

Access the application:
Open your web browser and go to http://127.0.0.1:8000/

You should see your home page.

Project Description
This portfolio is structured as a single Django project (mypersonalportfolio) containing a core application (pages).

mypersonalportfolio/: The main project directory.

settings.py: Contains project-wide settings, including database configuration, installed apps, and static files configuration.

urls.py: The main URL dispatcher for the entire project.

wsgi.py, asgi.py: Entry points for web servers.

pages/: A Django app dedicated to handling static content like the home page.

views.py: Contains the HomePageView function, which renders the home.html template.

urls.py: Defines URL patterns specific to the pages app.

templates/pages/: This directory holds the HTML templates for the pages app (e.g., home.html).

static/: If you have app-specific static files, they would go here.

static/ (Project-level): This directory at the project root is where all global static assets (like Bootstrap CSS/JS, custom CSS, images) are stored and collected from.

manage.py: A command-line utility for interacting with your Django project.

Usage
Once the server is running, you can access the home page at http://127.0.0.1:8000/. You can extend this project by adding more apps for different sections (e.g., projects app for project details, contact app for a contact form).
