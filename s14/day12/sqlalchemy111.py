#创建一个user表 & 插入数据
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

from sqlalchemy.orm import sessionmaker#这条是插入数据用到的

engine = create_engine("mysql+pymysql://root:1122@localhost/arch",encoding='utf-8', echo=True)

Base = declarative_base()#生成orm基类

class User(Base):
    __tablename__ = 'user' #表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

Base.metadata.create_all(engine)#创建表结构 自动提交 多次提交 相同则不会再提交


Session_class = sessionmaker(bind=engine)#创建与数据库的会话 session class
#注意这里给session返回的是class 不是实例
Session = Session_class()#生成session实例 #可以理解为cursor

user_obj = User(name="surface", password="know123")#生成你要创建的数据对象
user_obj2 = User(name="red-queen", password="unknow456")#生成你要创建的数据对象
print(user_obj.name,user_obj.id)#此时还没有创建对象 如果还没有创建对象id应该是None

Session.add(user_obj) #把要创建的数据对象添加到这个session里 一会统一创建
Session.add(user_obj2) #把要创建的数据对象添加到这个session里 一会统一创建
print(user_obj.name,user_obj.id)#此时也依然没创建对象

Session.commit()#现在才统一提交 创建数据 不同与表 插入数据重复提交会一直插入

