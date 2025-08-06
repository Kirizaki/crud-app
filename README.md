# 🧩 FastAPI CRUD App

A minimal FastAPI application with full CRUD support for users, using SQLAlchemy, Pydantic, Docker, and GitHub Actions for CI/CD.

---

## 🚀 Features

- FastAPI web framework
- SQLAlchemy ORM
- Pydantic request/response validation
- SQLite database
- Dockerized
- GitHub Actions CI pipeline with linting
- Auto-generated Swagger UI (`/docs`)

---

## 📁 Project Structure

```
crud-app/
│
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app + routes
│   ├── models.py         # SQLAlchemy DB models
│   ├── schemas.py        # Pydantic request/response models
│   ├── crud.py           # CRUD logic
│   └── database.py       # DB engine + session
│
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker container config
├── .dockerignore         # Files to ignore in Docker builds
├── .gitignore
│
├── .github/
│   └── workflows/
│       └── python-ci.yml # GitHub Actions workflow
│
└── README.md
```

---

## 🧪 Local Development

### 1. Install requirements

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run the app

```bash
uvicorn app.main:app --reload
```

### 3. Open in browser

- Root: http://localhost:8000
- Docs: http://localhost:8000/docs

---

## 🐳 Docker

### Build and run

```bash
docker build -t fastapi-app .
docker run -p 8000:8000 fastapi-app
```

### Visit:

- http://localhost:8000
- http://localhost:8000/docs

---

## ✅ CI/CD (GitHub Actions)

- Runs on every push and pull request to `main`
- Uses [Ruff](https://github.com/astral-sh/ruff) for lightning-fast linting
- Placeholder step for tests

---

## 🛠️ Future Ideas

- Add user authentication (OAuth2/JWT)
- Add unit/integration tests with `pytest`
- Connect to PostgreSQL or MySQL
- Deploy to cloud (Kubernetes / GCP / Azure)

---

## 📄 License

MIT – do whatever you want, just give credit.
