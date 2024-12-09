# Library API

A RESTful API for managing a library system built with **Django** and **Django REST Framework (DRF)**.

---

## Features
- **Authentication**: Secured API endpoints using JWT (JSON Web Tokens).
- **CRUD Operations**: Manage books and users in the library system.
- **Permissions**: Only authenticated users can access the API.
- **Error Handling**: Handles invalid requests and authentication errors gracefully.

---

## Installation

### Prerequisites
- Python 3.x
- Django 4.x
- Django REST Framework
- Django Simple JWT
- A database (e.g., SQLite or MySQL)

### Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your_username>/<repository_name>.git
   cd repository_name
2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   Set up the database:

4. **Apply migrations**:
   ```bash
   python manage.py migrate
5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
6. **Run the server**:
   ```bash
   python manage.py runserver
## Endpoints

### Authentication
| Method | Endpoint           | Description                           |
|--------|---------------------|---------------------------------------|
| POST   | `/api/auth/login/`  | Obtain access and refresh tokens      |
| POST   | `/api/auth/refresh/`| Refresh an expired access token       |

#### Example Request for Login:
   
     curl -X POST http://127.0.0.1:8000/api/auth/login/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "password123"}'

## Books

### Endpoints

| Method | Endpoint          | Description                              |
|--------|-------------------|------------------------------------------|
| GET    | `/api/books/`      | List all books (authenticated users only) |
| POST   | `/api/books/`      | Add a new book (authenticated users only) |
| GET    | `/api/books/<id>/` | Retrieve a specific book (authenticated users only) |
| PUT    | `/api/books/<id>/` | Update a book (authenticated users only) |
| DELETE | `/api/books/<id>/` | Delete a book (authenticated users only) |

---

### Example Requests

#### 1. **List Books**

    curl -X GET http://127.0.0.1:8000/api/books/ \
    -H "Authorization: Bearer <your_access_token>"
#### Example Request for Adding a Book:

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
#### Example Response:
    {
        "id": 1,
        "title": "Django for Beginners",
        "author": "William S. Vincent",
        "published_year": 2024,
        "genre": "Technology",
          "available_copies": 5
    }
### Features
- Secure authentication using JSON Web Tokens (JWT).
- RESTful APIs for managing a library's books.
- CRUD operations on the Book model.
- Accessible only to authenticated users.

