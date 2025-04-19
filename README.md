# Student

Andriw Rollo Castro
e-mail: randriw4@gmail.com

# 🛍 Caribe Market API

A modular Flask API designed to serve a marketplace system (Caribe Market) using SQLAlchemy, Marshmallow, and a microservices architecture. Built for clean separation of business logic, data access, and service communication.

---

## 🚀 Features

-   Flask REST API (MVC-like)
-   SQLAlchemy ORM + Marshmallow Schemas
-   Dockerized environment with `docker-compose`
-   Microservice-friendly structure
-   Reusable HTTP response helpers
-   External client communication between services
-   Example: `user_service`, `store_service`, etc.

---

## 🐳 Getting Started with Docker

1. **Clone the repository**

2. **Copy the environment file**

3. **Start the application**

```bash
docker-compose up --build
```

This will:

-   Build the Flask app
-   Start the PostgreSQL database
-   Link services and expose ports

---

## ⚙️ Migrations with Flask-Migrate

Manage your database schema using the `flask db` commands inside the Docker container:

**Create a new migration:**

```bash
docker-compose exec backend flask db migrate -m "your message"
```

**Apply migrations to the database:**

```bash
docker-compose exec backend flask db upgrade
```

**Check migration history:**

```bash
docker-compose exec backend flask db history
```

---

## 📬 API Endpoints

Example for users:

```http
GET    /users
GET    /users/<id>
POST   /users
PUT    /users/<id>
DELETE /users/<id>
```

Other entities (stores, products, etc.) follow a similar structure.

---

## 📦 HTTP Response Format

All endpoints return data in this standardized format:

```json
{
  "message": "User data retrieved successfully.",
  "data": {...},
  "errors": [],
  "status": 200
}
```

Use the `http_response()` helper in `utils/` to generate consistent responses.

---

## 🔁 Inter-Service Communication

Each service communicates via HTTP using reusable `clients/`, for example:

```python
# src/clients/user_client.py
UserServiceClient.get_user(user_id)
```
