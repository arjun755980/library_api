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
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
-H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "password123"}'
