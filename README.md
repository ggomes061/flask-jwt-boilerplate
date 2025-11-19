# Secure REST API Boilerplate with Flask + JWT

Production-ready backend template with everything you need to start a new project in 5 minutes.

### Features
- JWT Authentication (access + refresh tokens)
- Role-based access control (admin/user)
- PostgreSQL + SQLAlchemy + Flask-Migrate
- Ready for Docker & Docker Compose
- Full documentation & Postman collection
- Rate limiting & CORS configured

### Live Demo
https://flask-jwt-boilerplate.onrender.com

### Endpoints
| Route         | Method | Auth     | Description            |
|---------------|--------|----------|------------------------|
| `/register`   | POST   | Public   | Create new user        |
| `/login`      | POST   | Public   | Get access + refresh   |
| `/protected`  | GET    | JWT      | Test authenticated     |
| `/admin`      | GET    | JWT+admin| Admin-only route       |

### Tech Stack
Python 3.11 • Flask • JWT Extended • PostgreSQL • Docker • Gunicorn

### Quick Start (Docker)
```bash
cp .env.example .env
docker-compose up --build
