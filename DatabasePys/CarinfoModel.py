from sqlalchemy import ForeignKey,Unicode,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
from Base import Base

# Base=declarative_base()
class CarinfoModel(Base):
        __tablename__='CarInf'      
        Thekey=Column(Integer,primary_key=True,nullable=False,autoincrement=True)
        CarColor=Column(Unicode(50),nullable=False)
        CarColor.description="رنگ ماشین"
        girbox=Column(Unicode,nullable=True)
        OptionCond=Column(Unicode,nullable=True)
        MotorGirboxCond=Column(Unicode,nullable=True)
        Motor=Column(Unicode,nullable=True)
        information=Column(Unicode,nullable=True)
        Useage=Column(Unicode(50),nullable=True)
        CarType=Column(Unicode(50),nullable=False)
        CarType.description="نوع خودرو"
        model=Column(Unicode(50),nullable=False)
        model.description="مدل"

