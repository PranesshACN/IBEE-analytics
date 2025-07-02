#app folder
database.py
schemas.py
models.py
these three files should be present inside app folder

# Data Upload and Query API

A FastAPI backend for uploading CSV data, storing it in a database, and exposing API endpoints to query the data. All API requests are logged to the database.

---

## Features

✅ Upload CSV files  
✅ Validate CSV data  
✅ Store records in SQLite  
✅ Query all people via REST API  
✅ Log all API requests to a DB table  
✅ Swagger UI docs

---

## How to Run

1. **Clone repository** (or unzip folder)

2. Create virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate virtualenv:

- Windows:

    ```powershell
    .\venv\Scripts\activate
    ```

- Linux/macOS:

    ```bash
    source venv/bin/activate
    ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Initialize DB:

    ```bash
    python create_db.py
    ```

6. Run API server:

    ```bash
    uvicorn main:app --reload
    ```

7. Visit Swagger UI:

    http://127.0.0.1:8000/docs

---

## Endpoints

- `GET /people/` → Get all people records  
- `POST /upload/` → Upload CSV  
- `GET /` → Test root path

---

## Checking Logs

Run:

```bash
python show_logs.py

thank you....
