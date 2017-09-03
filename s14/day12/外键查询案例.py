import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Enum, DATE,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey

engine = create_engine("mysql+pymysql://root:1122@localhost/arch",encoding='utf-8')

Base = declarative_base()

class Student(Base):
    __tablename__ = 'egg_student'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE,nullable=False)

    def __repr__(self):
        return "<%s name:%s>" % (self.id, self.name)

class StudyRecord(Base):
    __tablename__ = "egg_record"
    id = Column(Integer, primary_key=True)
    day = Column(Integer,nullable=False)
    status = Column(String(32), nullable=False)
    stu_id = Column(Integer, ForeignKey("egg_student.id"))

    def __repr__(self):
        return "<%s name:%s>" % (self.id, self.day)


Base.metadata.create_all(engine) #创建表结构 自动提交