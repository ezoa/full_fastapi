from .database import Base
from sqlalchemy import Column, String, Boolean,Float, Integer,Date,ForeignKey,Table

from sqlalchemy.orm import relationship


# Association table for Many-to-Many relationship between Employee and Task
employee_task_association = Table(
    'employee_task', Base.metadata,
    Column('employee_id', Integer, ForeignKey('employees.employee_id')),
    Column('task_id', Integer, ForeignKey('tasks.tasks_id'))
)
class EmployeeModel(Base):
    __tablename__ ='employees'
    employee_id=Column(Integer, primary_key=True, autoincrement=True)
    employee_name= Column(String)
    employee_position=Column(String)
    employee_salary=Column(Float)
    department_id=Column(Integer,ForeignKey('departments.department_id'))
    user_id=Column(Integer, ForeignKey('users.user_id'))

    tasks=relationship('TaskModel',secondary=employee_task_association, back_populates='employees')
    department=relationship('DepartmentModel',back_populates='employees')
    user = relationship('UserModel', back_populates='employee', uselist=False)


class TaskModel(Base):
    __tablename__='tasks'
    tasks_id=Column(Integer,primary_key=True,autoincrement=True)
    tasks_label= Column(String)
    created_date=Column(Date)
    start_date=Column(Date)
    end_date= Column(Date)

    employees = relationship('EmployeeModel', secondary=employee_task_association, back_populates='tasks')

class DepartmentModel(Base):
    __tablename__='departments'
    department_id=Column(Integer, autoincrement=True, primary_key=True)
    department_name=Column(String)
    employees = relationship('EmployeeModel', back_populates='department')




class UserModel(Base):
    __tablename__='users'
    user_id=Column(Integer, primary_key=True,autoincrement=True)
    username=Column(String)
    user_email=Column(String)
    user_password=Column(String)
    is_active=Column(Boolean)
    is_admin=Column(Boolean)
    employee = relationship('EmployeeModel', back_populates='user', uselist=False)
