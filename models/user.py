from backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username= Column(String)
    firstname= Column(String)
    lastname= Column(String)
    age= Column(Integer)
    slug= Column(String, unique=True, index=True)
    tasks = relationship('tasks', back_populates='user')