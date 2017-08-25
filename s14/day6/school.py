#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

class School(object): #没有人继承School 但要调用里面的参数
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    def enroll(self,stu_obj):#学生注册
        print("为学员%s办理注册手续"%stu_obj.name)
        self.students.append(stu_obj)

    def hire(self,staff_obj):#雇佣老师
        self.staffs.append(staff_obj)
        print("雇佣新员工%s"%staff_obj.name)

class SchoolMember(object):#学校成员
    def __init__(self,name,age,sex): #构造函数
        self.name = name
        self.age  = age
        self.sex  = sex

    def tell(self):#打印个人信息
        pass

class Teacher(SchoolMember): #老师继承学校成员
    def __init__(self,name,age,sex,salary,course):#重构函数 加入参数 工资 课程
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):#打印老师的个人信息
        print('''
        ----info of Teacher:%s----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):#老师教什么课程
        print("%s is teaching course [%s]" %(self.name,self.course))

class Student(SchoolMember):#学生继承学校成员
    def __init__(self,name,age,sex,stu_id,grade):#重构函数 加入参数 学号 班级
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):  # 打印学生的个人信息
        print('''
         ----info of Teacher:%s----
         Name:%s
         Age:%s
         Sex:%s
         Stu_id:%s
         Grade:%s
         ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self,amount):#交学费的功能
        print("%s has paid tuition for $%s" %(self.name,amount))


school = School("老男号IT","坏男孩") #生成学校

t1 = Teacher("Oldboy",56,"M",200000,"Linux") #生成老师
t2 = Teacher("Alex",22,"MF",300,"PythonDevOps")

s1 = Student("Surface",18,"M","001","PythonDevOps") #生成学生
s2 = Student("花木兰",19,"F","002","Linux")

t1.tell() #打印自己的信息
t2.tell()

school.hire(t1)#雇佣t1
school.enroll(s1)#注册s1
school.enroll(s2)#注册s2

print(school.students)
print(school.staffs)

school.staffs[0].teach() #老师教课 t1教什么课 只注册了t1

for stu in school.students: #交学费
    stu.pay_tuition(5000)
