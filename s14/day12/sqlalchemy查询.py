#创建一个user表 & 插入 & 查询 & 修改 & 回滚 &统计与分组
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

from sqlalchemy.orm import sessionmaker#这条是插入数据用到的

# engine = create_engine("mysql+pymysql://root:1122@localhost/arch",encoding='utf-8', echo=True)
engine = create_engine("mysql+pymysql://root:1122@localhost/arch",encoding='utf-8')

Base = declarative_base()#生成orm基类

class User(Base):
    __tablename__ = 'user' #表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):#本集特别嘉宾 不要忽略我 # b
        return "<%s name:%s>" % (self.id,self.name)

Base.metadata.create_all(engine)#创建表结构 自动提交 多次提交 相同则不会再提交


Session_class = sessionmaker(bind=engine)#创建与数据库的会话 session class
#注意这里给session返回的是class 不是实例
Session = Session_class()#生成session实例 #可以理解为cursor

# user_obj = User(name="surface", password="know123")#生成你要创建的数据对象
# user_obj2 = User(name="red-queen", password="unknow456")#生成你要创建的数据对象
# print(user_obj.name,user_obj.id)#此时还没有创建对象 如果还没有创建对象id应该是None
#
# Session.add(user_obj) #把要创建的数据对象添加到这个session里 一会统一创建
# Session.add(user_obj2) #把要创建的数据对象添加到这个session里 一会统一创建
# print(user_obj.name,user_obj.id)#此时也依然没创建对象

# Session.commit()#现在才统一提交 创建数据 不同与表 插入数据重复提交会一直插入

#查询 主角在此
# data = Session.query(User).filter_by(name='surface').all() # a #FROM user WHERE user.name = %(name_1)s
# print(data[0].name, data[0].password) # a
# data = Session.query(User).filter_by().all() # b #查所有的
# data = Session.query(User).filter_by().first() # c #查第一个
# data = Session.query(User).filter(User.id>2).all() # d #我懂的
# data = Session.query(User).filter(User.id==2).all() # e #这里判断相等是双等号
# data = Session.query(User).filter_by(id=2).all() # e #这里判断相等是等号
# data = Session.query(User).filter(User.id >1).filter(User.id <4).all() # f #多条件查询
#
# print(data) # b c d e


#修改 查出来 一个个改
# data = Session.query(User).filter_by().first() # c #查第一个
# print(data)
# data.name = "Oreo"
# data.password = "Pass_oreo"
# Session.commit() #修改要提交 查询不用 去数据库看看


# 回滚
# fake_user = User(name='dante',password='666666') #创建一个用户
# Session.add(fake_user)
#
# print(Session.query(User).filter(User.name.in_(['surface','dante'])).all())
# #in 或者 就是surface或dante都可以 #我只为证明你存在过
#
# Session.rollback() #回滚
# print("after rollback")
# print(Session.query(User).filter(User.name.in_(['surface','dante'])).all())
# #Bye~Bye~ D叔
# Session.commit()
# #此时再往数据库插一条数据 会发现自增长的id被用了一个


#统计
# fake_user = User(name='dante',password='666666') #创建一个用户
# Session.add(fake_user)
#
# print(Session.query(User).filter(User.name.in_(['surface','dante'])).count())
# #统计surface和dante共出现次数 mysql默认不区分大小写
#
# Session.commit() #此时再次提交会加1 因为又插入了一个

#分组
# from sqlalchemy import func
#
# print(Session.query( User.name,func.count(User.name)).group_by(User.name).all())
