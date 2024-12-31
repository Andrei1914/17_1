from pydantic import BaseModel


#Создание пользователя
class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

#ОБновление данных юзера
class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int

#Создание задачи
class CreateTask(BaseModel):
    title: str
    content: str 
    priority: str

#Обновление задачи
class UpdateTask(BaseModel):
    title: str
    content: str 
    priority: str