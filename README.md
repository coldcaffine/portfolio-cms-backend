# Portfolio CMS Backend

A custom Portfolio Content Management System backend built with **FastAPI**, **PostgreSQL (Neon)**, **SQLAlchemy**, and **JWT authentication**.

## Features

* JWT-based authentication
* Admin registration and login
* About section management
* Skills CRUD
* Projects CRUD
* Blogs CRUD
* Experience CRUD
* Testimonials CRUD
* Services CRUD
* Image/media upload and deletion
* Contact/message management
* PostgreSQL database integration
* CORS support
* Static media file serving
* REST API

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL / Neon
* Pydantic
* JWT
* Passlib / bcrypt
* Uvicorn
* FastAPI Mail

## Project Structure

```text
portfolio-cms-backend/
├── app/
│   ├── core/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── config.py
│   ├── database.py
│   └── main.py
├── uploads/
├── requirements.txt
├── .env
└── .gitignore
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/coldcaffine/portfolio-cms-backend.git
cd portfolio-cms-backend
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file containing the required database, JWT, and mail configuration values.

Do not commit `.env` to GitHub.

### 5. Start the development server

```bash
python -m uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Main API Routes

| Route            | Purpose                        |
| ---------------- | ------------------------------ |
| `/auth/register` | Register an admin              |
| `/auth/login`    | Login                          |
| `/auth/me`       | Get current authenticated user |
| `/about/`        | About information              |
| `/skills/`       | Skills                         |
| `/projects/`     | Projects                       |
| `/blogs/`        | Blogs                          |
| `/experience/`   | Experience                     |
| `/testimonials/` | Testimonials                   |
| `/services/`     | Services                       |
| `/upload/image`  | Upload media                   |
| `/contact/`      | Contact messages               |
| `/uploads/`      | Serve uploaded media           |

## Authentication

Admin write operations are protected using JWT bearer authentication.

The frontend stores the authentication token and sends it with protected API requests.

## Database

The application uses PostgreSQL hosted through Neon. SQLAlchemy is used for database interaction and the database connection is configured through environment variables.

## Frontend

This backend is designed to work with the Portfolio CMS React frontend.

Frontend repository:

`https://github.com/coldcaffine/dr-strange-`

## Development

Run the backend and frontend separately during local development.

Backend:

```bash
cd ~/portfolio-cms-backend
source venv/bin/activate
python -m uvicorn app.main:app --reload
```

Frontend:

```bash
cd ~/Desktop/portfolio-cms-frontend
npm run dev
