# CI/CD Final Project

A Python Flask application demonstrating CI/CD pipelines using GitHub Actions, Tekton, and OpenShift.

## Project Structure

```
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI pipeline
├── .tekton/
│   ├── tasks/
│   │   ├── lint.yaml           # Tekton linting task
│   │   ├── tests.yaml          # Tekton unit testing task
│   │   ├── buildah.yaml        # Tekton build image task
│   │   └── deploy.yaml         # Tekton deploy task
│   ├── pipeline.yaml           # Tekton pipeline definition
│   └── pipelinerun.yaml        # Pipeline run template
├── deploy/
│   ├── deployment.yaml         # OpenShift Deployment manifest
│   ├── service.yaml            # OpenShift Service manifest
│   └── route.yaml              # OpenShift Route manifest
├── service/
│   ├── __init__.py             # Flask app initialization
│   └── routes.py               # API routes
├── tests/
│   └── test_routes.py          # Unit tests
├── Dockerfile                  # Container image definition
├── requirements.txt            # Python dependencies
├── setup.cfg                   # Tool configuration
└── wsgi.py                     # WSGI entry point
```

## Objectives Completed

1. ✅ **GitHub Actions CI Pipeline** - Linting and unit testing
2. ✅ **Tekton Tasks** - Lint, test, and build image tasks
3. ✅ **OpenShift CI Pipeline** - Using Tekton tasks
4. ✅ **Deploy Step** - Deploys to OpenShift cluster

---

## Part 1: GitHub Actions CI Pipeline

The GitHub Actions workflow is located at `.github/workflows/ci.yml` and includes:

- **Linting Job**: Runs flake8 to check code quality
- **Testing Job**: Runs pytest for unit tests

### Triggering the Pipeline

The pipeline runs automatically on:
- Push to `main` branch
- Pull requests to `main` branch

---

## Part 2: Running Locally

### Prerequisites
- Python 3.11+
- pip

### Setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Application

```bash
python wsgi.py
```

Visit: http://localhost:8080

### Run Tests

```bash
pytest tests/ -v
```

### Run Linting

```bash
flake8 service/
```

---

## Part 3: Tekton Pipeline on OpenShift

### Prerequisites
- OpenShift CLI (`oc`) installed and logged in
- Tekton Pipelines installed on the cluster

### Step 1: Apply Tekton Tasks

```bash
# Apply all Tekton tasks
oc apply -f .tekton/tasks/lint.yaml
oc apply -f .tekton/tasks/tests.yaml
oc apply -f .tekton/tasks/buildah.yaml
oc apply -f .tekton/tasks/deploy.yaml
```

### Step 2: Apply the Pipeline

```bash
oc apply -f .tekton/pipeline.yaml
```

### Step 3: Run the Pipeline

```bash
oc create -f .tekton/pipelinerun.yaml
```

### Step 4: Monitor Pipeline Run

```bash
# List pipeline runs
tkn pipelinerun list

# View logs
tkn pipelinerun logs cicd-pipeline-run-xxxxx -f
```

---

## Part 4: Manual Deployment to OpenShift

If you want to deploy manually without the pipeline:

```bash
# Build and push the image
oc new-build --name=cicd-final-project --binary --strategy=docker
oc start-build cicd-final-project --from-dir=. --follow

# Deploy the application
oc apply -f deploy/deployment.yaml
oc apply -f deploy/service.yaml
oc apply -f deploy/route.yaml

# Get the route URL
oc get route cicd-final-project -o jsonpath='{.spec.host}'
```

---

## API Endpoints

| Endpoint  | Method | Description                    |
|-----------|--------|--------------------------------|
| `/`       | GET    | Welcome message                |
| `/health` | GET    | Health check for k8s probes    |
| `/info`   | GET    | Application information        |
| `/count`  | GET    | Counter endpoint               |

---

## Technologies Used

- **Python/Flask**: Web application framework
- **GitHub Actions**: CI pipeline for linting and testing
- **Tekton**: Cloud-native CI/CD pipelines
- **OpenShift**: Container orchestration platform
- **Buildah**: Container image building

---

## Author

Randel Ortega

