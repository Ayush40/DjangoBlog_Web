# Django Blog Website

This is a simple blog website built using Django, a Python web framework.

## Features

- User registration and authentication
- Create, read, update, and delete blog posts
- Comment on blog posts
- Categorize blog posts by tags
- Search functionality to find specific blog posts
- Responsive design for mobile and desktop devices

## Installation

1. Clone the repository:

    git clone https://github.com/Ayush40/DjangoBlog_web.git

2. Navigate to the project directory:

    cd miniblog

3. Create a virtual environment:

    python -m venv env1

4. Activate the virtual environment:

    env1\scripts\activate

5. Install the dependencies:

    pip install -r requirements.txt
    
6. Perform database migrations:

    python manage.py migrate

7. Create a superuser (admin):

    python manage.py createsuperuser

8. Start the development server:

    python manage.py runserver

9. Open your web browser and visit `http://localhost:8000` to access the website.

## Configuration

- You can customize various settings in the `settings.py` file to suit your needs, such as database configuration, static files, email settings, etc.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please submit an issue or create a pull request.
