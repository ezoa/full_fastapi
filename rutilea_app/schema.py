from typing import Union,List,Optional
from datetime import date
from pydantic import BaseModel



class TaskBase(BaseModel):
    tasks_label:str
    created_date: Optional[date]
    start_date: Optional[date]
    end_date: Optional[date]



class TaskCreate(TaskBase):
    pass
class Task(TaskBase):

    tasks_id:int

    class Config:
        orm_mode=True


class EmployeeBase(BaseModel):
    employee_name:str
    employee_position:str
    employee_salary:float
    

class EmployeeCreate(BaseModel):
    department_id:int
    user_id:int

class Employee(EmployeeBase):
    employee_id:int
    tasks:List[Task]=[]

    class Config:
        orm_mode=True
    
class UserBase(BaseModel):
    user_email:str
    username:str


class UserCreate(UserBase):
    user_password:str

class User(UserBase):
    user_id:int
    is_active:bool
    is_admin:bool
    class Config:
        orm_mode=True




class DepartmentBase(BaseModel):
    department_name:str
    

class DepartmentCreate(DepartmentBase):
    pass

class Department(DepartmentBase):
    department_id:int
    employee:List[Employee]=[]

    


    class Config:
        orm_mode=True



    
