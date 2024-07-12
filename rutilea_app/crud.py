from sqlalchemy.orm import Session
from . import models, schema

from fastapi import HTTPException
from passlib.context import CryptContext


pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto")


#User
def get_password_hash(password):
    return pwd_context.hash(password)
def get_user_by_id(db:Session,user_id:int):

    return db.query(models.UserModel).filter(models.UserModel.user_id==user_id).first()



def create_user(db:Session, user:schema.UserCreate):
    # user=models.UserModel(**user.dict())
    user.user_password=get_password_hash(user.user_password)
    user=models.UserModel(**user.dict())

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_all(db:Session):
    return db.query(models.UserModel).all()

def update_by_user(db:Session,user_email:str,user_password:str):
    user_info=get_user_by_email(db,user_email)

    if user_info is not None:
        user_info.user_email=user_email
        user_info.user_password=get_password_hash(user_password)
        db.commit()
        db.refresh(user_info)
        return {"message": "Your information have been update "}
    else:

        return "user email does not exist"

    
def get_user_by_email(db:Session,user_email:str):

    return db.query(models.UserModel).filter(models.UserModel.user_email==user_email).first()


def delete_user(db:Session,user_id:int):
    user_to_delete=get_user_by_id(db,user_id)
    db.delete(user_to_delete)
    db.commit()
    return "User have been delete"






def get_employee_by_id(db:Session,employee_id:int):
    return db.query(models.EmployeeModel).filter(models.EmployeeModel.employee_id==employee_id).first()




def get_department_by_id(db:Session, department_id:int):
    return db.query(models.DepartmentModel).filter(models.DepartmentModel.department_id==department_id).first()


def get_task_by_id(db:Session, task_id:int):
    return db.query(models.TaskModel).filter(models.TaskModel.tasks_id==task_id).first()




