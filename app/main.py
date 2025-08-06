from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

app = FastAPI()

# create db tables
models.Base.metadata.create_all(bind=database.engine)

# dependency: db session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def raise_user_not_found_error():
    raise HTTPException(status_code=404, detail="User not found")


# routes:
@app.get("/")
def root():
    return {"message": "User CRUD API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/users/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users/", response_model=list[schemas.UserRead])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.get("/users/{user_id}", response_model=schemas.UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise_user_not_found_error()
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, user_id)
    if not user:
        raise_user_not_found_error()
    return user

