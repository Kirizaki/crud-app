# 🧩 FastAPI CRUD App

A minimal FastAPI application with full CRUD support for users, using SQLAlchemy, Pydantic, Docker, Kubernetes, and GitHub Actions for CI/CD.

---

## 🚀 Features

- FastAPI web framework
- SQLAlchemy ORM
- Pydantic request/response validation
- SQLite database
- Dockerized
- Kubernetes deployment (via Minikube or cloud)
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
├── k8s/                  # Kubernetes manifests
│   ├── deployment.yaml
│   └── service.yaml
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

---

## ⚙️ Kubernetes (Minikube)

### 1. Start Minikube

```bash
minikube start
```

### 2. Use Minikube Docker daemon

```bash
eval $(minikube docker-env)
docker build -t fastapi-app .
```

### 3. Apply K8s manifests

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### 4. Access the app

```bash
minikube service fastapi-service
```

This will open the FastAPI app in your browser via NodePort.

---

## ✅ CI/CD (GitHub Actions)

- Lints Python code using Ruff
- Runs on every push and PR to `main`
- Placeholder for test integration

---

## 🛠️ Future Ideas

- Add user authentication (OAuth2 / JWT)
- Add unit/integration tests with `pytest`
- Connect to PostgreSQL or MySQL
- Add production-grade Ingress (with cert-manager)
- Deploy to GKE, AKS, or EKS with Helm

---

## 📄 License

MIT – do whatever you want, just give credit.
