#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface

#异常处理 虽然程序出错了 但不想给用户看到这个错误

names = ['ashe','fiora']
data = {}
#names[3]
try:                #尝试下面的代码 一直执行
    # names[3]
    # data['name']
    open("huluwa.avi")
except KeyError as e:    #除非出了这个错
    print("没有这个key",e)

except IndexError as e:
    print("列表操作错误",e)

except (KeyError,IndexError) as e:#同时判断多个错误类型 但不知是哪个类型的出错
    print("错错错",e)              #当两种错误都采用同一种处理方法的时候可用

except Exception as e:         #可以用在后面 抓所有未知错误
    print("一下子抓住所有错误",e)

else:
    print("一切正常 万事大吉")

finally:
    print("不管有没有错 都执行")