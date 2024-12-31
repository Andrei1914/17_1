from backend.db import *
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship



class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title= Column(String)
    content= Column(String)
    priority= Column(Integer, default=0)
    completed= Column(Boolean, default=False)
    user_id= Column(Integer, ForeignKey("user.id"), nullable=False, index=True)
    slug= Column(String, unique=True, index=True)
    user= relationship('user', back_populates='tasks')
