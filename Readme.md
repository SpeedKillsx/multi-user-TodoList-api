# multi-user-TodoList API (Python)

Production-ready REST API for a multi-user TODO list. Python-first project layout and commands are shown below (FastAPI/Flask/Django flavors outlined where relevant). Supports user registration, JWT auth, per-user tasks, assignment/sharing, filtering, pagination and role-based actions.

---

## Features
- User registration & login (JWT)
- Create/read/update/delete TODOs (per-user)
---

## Tech stack (typical Python choices)
- Language: Python 3.10+
- Web framework: FastAPI
- ASGI server: uvicorn 
- ORM: SQLAlchemy / SQLModel
- DB: PostgreSQL 
- Auth: JWT 
- Packaging: pip + venv
- Conetainerization: Docker
---

## Repository layout (Python)
- src/ or app/ — application package
    - api/, resources/, models/, services/, dto/
- scripts/ — helper scripts (seed, lint, build)
- requirements.txt
- .env
- Dockerfile, docker-compose.yml

---

## Quickstart (local development)

1. Clone
     git clone <repo-url>
     cd multi-user-TodoList-api

2. Create virtualenv & install
     python -m venv .venv
     source .venv/bin/activate
     pip install -r requirements.txt

3. Start server
     # FastAPI
     uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Server runs at http://localhost:8000
