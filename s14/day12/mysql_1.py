#连接数据库 并插入数据
import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='1122',db='arch')#创建连接

cursor = conn.cursor()#创建游标

# effect_row = cursor.execute("select * from student")
# print(cursor.fetchone()) #读student表一行
# print(cursor.fetchone()) #再读一行
# print('-------------')
# print(cursor.fetchall()) #上面读了两行 所以上面两行不会再读了

data = [
    ("N1",16,"2008-01-01"),
    ("N2",17,"2009-01-01"),
    ("N3",16,"2010-01-01"),
]

cursor.executemany("insert into student (name,age,register_date) VALUES (%s,%s,%s)",data)

conn.commit()#一定要提交才能写入 默认就是开启事务的