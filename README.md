# 🔐 Vulnerable Tracker API

This project is a FastAPI-based web API that checks Python dependencies for known vulnerabilities using the [OSV (Open Source Vulnerabilities)](https://osv.dev/) database.

## 🚀 Features

- Accepts a `requirements.txt` file.
- Parses dependencies and versions.
- Checks each package against the OSV vulnerability database.
- Returns a JSON response listing:
  - Validated dependencies with any found vulnerabilities.
  - Ignored dependencies (if any).

---

## 🧰 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/) – high-performance web framework.
- [Pydantic](https://docs.pydantic.dev/) – data validation and settings management.
- [Uvicorn](https://www.uvicorn.org/) – ASGI server for running the FastAPI app.
- [OSV](https://osv.dev/) - fetch vulnerability data for dependencies.
- [Redis](https://www.redis.io/) – in-memory cache for fast data storage.
---

# API Endpoint

## POST /applications/

Accepts the following form data:

| Field           | Type   | Description                                      |
|-----------------|--------|--------------------------------------------------|
| `name`          | string | Name of the application                         |
| `description`   | string | (Optional) Description of the application        |
| `requirements_file` | file   | `requirements.txt` file with dependencies     |

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/dancinoman/vulnerable-tracker-api.git
   cd vulnerable-tracker-api
   ```
2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the API locally**:
    ```bash
    uvicorn app.main:app --reload
    ```
5. **Run Redis with Docker if not installed locally**:
    ```bash
    docker run -d -p 6379:6379 redis
    ```
6. **Curl test**:
    ```bash
    curl -X POST "http://localhost:8000/applications/" \
    -H "accept: application/json" \
    -F "name=MyApp" \
    -F "description=A test app for vulnerabilities" \
    -F "requirements_file=@tests/data/sample_requirements.txt"
    ```

## Example of response
  ```json
  {
    "application": "MyApp",
    "dependencies_checked": [
      {
        "name": "requests",
        "version": "2.25.1",
        "vulnerabilities": [],
        "error": null
      }
    ],
    "ignored_dependencies": []
  }
  ```
