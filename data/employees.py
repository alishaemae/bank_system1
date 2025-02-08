from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from service.db_connector import Base  # base уже определен в db_connector.py

class Employee(Base):
    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)  
    password_hash = Column(String(255), nullable=False)  
    full_name = Column(String(100))
    role_id = Column(Integer, ForeignKey('roles.role_id'))
    status = Column(String(50), default='active')
    contact_number = Column(String(20), nullable=True) 
    email = Column(String(100), nullable=True, unique=True)