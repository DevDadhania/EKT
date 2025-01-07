from fastapi import FastAPI, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database

app = FastAPI()

# Initialize the database
database.init_db()

# Dependency to get the DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new task
@app.post("/tasks/", response_model=schemas.Task)
async def create_task(
    title: str = Form(...), description: str = Form(...), db: Session = Depends(get_db)
):
    db_task = models.Task(title=title, description=description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Get all tasks
@app.get("/tasks/", response_model=list[schemas.Task])
async def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.Task).all()
    return tasks

# Delete a task by ID
@app.delete("/tasks/{task_id}", response_model=schemas.Task)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return db_task
