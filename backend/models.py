from sqlalchemy import Column, Integer, String, CheckConstraint
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False, default="To Do")

    __table_args__ = (
        CheckConstraint(status.in_(["To Do", "In Progress", "Done"]), name="tasks_status_check"),
    )
