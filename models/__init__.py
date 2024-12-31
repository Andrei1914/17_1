from models.user import User 
from models.task import Task
from sqlalchemy.schema import CreateTable as create

print(create(User.__table__))
print(create(Task.__table__))