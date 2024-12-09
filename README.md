Library API
A RESTful API for managing a library system built with Django and Django REST Framework (DRF).

Features
Authentication: Secured API endpoints using JWT (JSON Web Tokens).
CRUD Operations: Manage books and users in the library system.
Permissions: Only authenticated users can access the API.
Error Handling: Handles invalid requests and authentication errors gracefully.
Installation
Prerequisites
Python 3.x
Django 4.x
Django REST Framework
Django Simple JWT
A database (e.g., SQLite or MySQL)
Setup
Clone the repository:

bash
Copy code
git clone https://github.com/<your_username>/<repository_name>.git
cd repository_name
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database:

Apply migrations:
bash
Copy code
python manage.py migrate
Create a superuser:
bash
Copy code
python manage.py createsuperuser
Run the server:

bash
Copy code
python manage.py runserver
Endpoints
Authentication
Method	Endpoint	Description
POST	/api/auth/login/	Obtain access and refresh tokens
POST	/api/auth/refresh/	Refresh an expired access token
Example Request for Login:
bash
Copy code
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "password123"}'
Books
Method	Endpoint	Description
GET	/api/books/	List all books (authenticated users only)
POST	/api/books/	Add a new book (authenticated users only)
GET	/api/books/<id>/	Retrieve a specific book (authenticated users only)
PUT	/api/books/<id>/	Update a book (authenticated users only)
DELETE	/api/books/<id>/	Delete a book (authenticated users only)
Example Request for Listing Books:
bash
Copy code
curl -X GET http://127.0.0.1:8000/api/books/ \
-H "Authorization: Bearer <your_access_token>"
Example Request for Adding a Book:
bash
Copy code
curl -X POST http://127.0.0.1:8000/api/books/ \
-H "Content-Type: application/json" \
-H "Authorization: Bearer <your_access_token>" \
-d '{
  "title": "Django for Beginners",
  "author": "William S. Vincent",
  "published_year": 2024,
  "genre": "Technology",
  "available_copies": 5
}'
Database Models
Book
title (CharField): Title of the book.
author (CharField): Author of the book.
published_year (IntegerField): Year the book was published.
genre (CharField): Genre of the book.
available_copies (IntegerField): Number of available copies in the library.
User
Uses Django’s default User model for authentication.
Testing the API
Run the Django Development Server
bash
Copy code
python manage.py runserver
Test Authentication
Create a user:

bash
Copy code
python manage.py shell
python
Copy code
from django.contrib.auth.models import User
User.objects.create_user(username="testuser", password="password123")
exit()
Obtain a JWT token using the /api/auth/login/ endpoint.

Test Book Endpoints
Use tools like curl, Postman, or your browser to test the endpoints.
Include the JWT token in the Authorization header for all requests.
Project Structure
bash
Copy code
library_api/
├── library_api/        # Main Django project
│   ├── settings.py     # Project settings
│   ├── urls.py         # URL routing
├── books/              # Library API app
│   ├── models.py       # Database models
│   ├── serializers.py  # DRF serializers
│   ├── views.py        # API views
│   ├── urls.py         # App-specific URL routing
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
└── README.md           # Project description
