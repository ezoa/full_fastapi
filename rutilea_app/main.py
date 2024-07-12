from fastapi import FastAPI, Depends, HTTPException, Request
from .database import SessionLocal,engine
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from .schema import Employee,Task,User,Department,UserCreate

from .crud import get_user_by_id,get_employee_by_id,create_user,get_user_all,update_by_user,delete_user

from .models import EmployeeModel,UserModel,TaskModel,DepartmentModel,Base

import sys
from loguru import logger
from uuid import uuid4
Base.metadata.create_all(bind=engine)


app=FastAPI()

def db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()

# logger.remove()

logger.add("app_logs/info.log",format="{time:YYYY-MM-DD HH:mm:ss} | {level}|{module}:{function}:{line} -<level>{message}</level> {extra}",enqueue=True,rotation="500 MB")

@app.middleware("http")
#in order to give for every task an id to easily monitoring in the log file , i will use uuid4 to give unique identifier to each log

async def log_middleware(request:Request,call_next):
    task_id=str(uuid4())
    with logger.contextualize(task_id=task_id):
        logger.info("Request to access the folowing"+request.url.path)
        try:
            response=await call_next(request)
            return response
        except Exception as ex:
            logger.error(f"Request to "+ request.url.path+"failed:{ex}")
            response = JSONResponse(content={"success": False}, status_code=500)
            return response
        finally:
            logger.info("Sucessfully accessed"+request.url.path)
            return response


@app.get("/redtrieve_user_by_id/{user_id}/")


def retrieve_user_by_id(user_id:int,db=Depends(db)):
    if user_id is not None:
        with logger.catch():

            user=get_user_by_id(user_id,db)
            return user
    else:
        raise HTTPException(status_code=404, detail="Can not find this User")
    
    return print("good")


@app.post("/create_user/")
def create_user_(user:UserCreate,db=Depends(db)):
    user_in_db=create_user(db, user)

    return {"message":"user successfully register","user":user_in_db}


@app.get("/get_all_user/")
def get_user_all_( db=Depends(db)):

    return get_user_all(db)


@app.delete("/delete/user/{user_id}")
def delete_user_(user_id:int, db=Depends(db)):
    delete_user(db,user_id)
    return {"delete all "}

@app.patch("/update/user/info")

def update_user_(user_email:str,user_password:str, db=Depends(db)):
    user_new_info=update_by_user(db, user_email,user_password)
    return {"user_info":user_new_info}