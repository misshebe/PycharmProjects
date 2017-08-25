#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Surface
name = "my \tname is {name} and i am {year} old"

print(name.capitalize())  #首字母大写
print(name.count("s"))    #统计s的个数
print(name.center(50,"-"))#打印50个字符 字符不够 -来凑数
print(name.endswith("ce"))#判断字符串以什么结尾 是的话返回True
print(name.expandtabs(tabsize=30)) #帮你自动打多少个空格 无卵用
print(name.find("name")) #name从第四个开始 m0 y1 空格2 \t3
print(name.find("y")) #y的下标是1 所以返回1
print(name[name.find("name"):]) #字符串切片 从name到最后
print(name.format(name='surface',year=18)) #format用法
print(name.format_map( {'name':'surface','year':'18'})) #format_map里面是一个字典
print('sb250'.isalnum()) #是否为阿拉伯字母和数字 有特殊符号会返回False
print('guapi'.isalpha()) #是否为纯英文字母 包含大小写
print('233'.isdecimal()) #是否为10进制
print('213'.isdigit())   #是否为整数
print('name'.isidentifier()) #判断是不是一个合法的标识符 就是是不是一个合法的变量名
print('pipixia'.islower()) #判断是不是小写
print('42'.isnumeric()) #是否只有数字 不能有小数点
print(' '.isspace()) #是不是一个空格
print('What The Fuck'.istitle()) #是不是一个标题 每个字母首字母大写即是title
print('linux'.isprintable()) #是不是可以打印的 ##例如tty file,drive file就不能打印了
print('WHATTHEFUCK'.isupper()) #是不是全是大写
print('+'.join(['1','2','3'])) #join的用法 字符串拼接
print(name.ljust(50,'*')) # l是字母不是数字 长度不足50在后面用*填充
print(name.rjust(50,'-')) #长度不足50 在前面填充
print('SURFACE'.lower()) #把大写转换成小写 小写不变
print('Surface'.upper())  #把小写转换成大写 大写也是大写
print('\nArch\n')    #左边的\n就是往上有一个回车  右边的\n就是往下有一个回车
print('\nArch'.lstrip()) #lstrip去左边空格回车
print('Arch\n'.rstrip()) #rstrip去右边空格回车
print('Arch') #我的存在就是为了证明上一个\n没有生效
print('   Arch\n'.strip()) #去两边的空格和回车

p = str.maketrans("abcdLhr",'1234567') #两边的要一样多
print("Arch Linux".translate(p))  ##把左右两边的位置一一对调

print('google'.replace('o','O')) #替换 把o替换成O
print('google'.replace('o','O',1)) #只替换一个

print('shadowsocks'.rfind('s')) #找最右边的s的下标

print('fifty five flags flutter from floating frigate fighting for freedom'.split()) #以空格分隔 分成列表
print('fifty five flags flutter from floating frigate fighting for freedom'.split("f")) #以f为分隔 分成列表

print('1+2+3+4'.split('+')) #只把数字提取出来 作为列表
print('1+2\n+3+4'.splitlines()) #按换行作为分隔符

print('Oh My God'.swapcase()) #把大写转换成小写 把小写转换成大写
print('no zuo no die'.title()) #把每个首字母大写 作为标题
print('game over'.zfill(50)) #不够50的在左边用0填充






