from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Task
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for task creation
class TaskCreate(BaseModel):
    name: str
    status: str

# Valid statuses
VALID_STATUSES = {"To Do", "In Progress", "Done"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tasks")
def read_tasks(db: Session = Depends(get_db)):
    result = db.query(Task).all()
    return [{"id": r.id, "name": r.name, "status": r.status} for r in result]

@app.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    if task.status not in VALID_STATUSES:
        raise HTTPException(status_code=400, detail="Invalid status value!")

    new_task = Task(name=task.name, status=task.status)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"id": new_task.id, "name": new_task.name, "status": new_task.status}
