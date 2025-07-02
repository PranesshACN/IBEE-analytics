from fastapi import FastAPI, UploadFile, File, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from typing import List
import pandas as pd
from io import StringIO
from datetime import datetime

from app import models, schemas
from app.database import SessionLocal

app = FastAPI()

# ==========================
# Middleware for DB logging
# ==========================
@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)

    db = SessionLocal()
    log_entry = models.APILog(
        method=request.method,
        url=str(request.url.path),
        status_code=response.status_code,
        timestamp=datetime.utcnow()
    )
    db.add(log_entry)
    db.commit()
    db.close()

    return response

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.get("/people/", response_model=List[schemas.PersonResponse])
def read_people(db: Session = Depends(get_db)):
    people = db.query(models.Person).all()
    return people        

@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files allowed.")

    contents = await file.read()
    try:
        df = pd.read_csv(StringIO(contents.decode()))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading CSV: {e}")

    required_columns = ["name", "age", "email"]
    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise HTTPException(
            status_code=400,
            detail=f"Missing columns in CSV: {missing}"
        )

    for index, row in df.iterrows():
        if pd.isnull(row["name"]) or pd.isnull(row["age"]) or pd.isnull(row["email"]):
            raise HTTPException(status_code=400, detail=f"Row {index} has missing data.")
        if not isinstance(row["age"], (int, float)):
            raise HTTPException(status_code=400, detail=f"Row {index} has invalid age.")

    for _, row in df.iterrows():
        person = models.Person(
            name=row["name"],
            age=int(row["age"]),
            email=row["email"],
        )
        db.add(person)
    db.commit()

    return {"message": "CSV uploaded and saved successfully."}
