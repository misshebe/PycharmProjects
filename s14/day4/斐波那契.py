
# Author: Surface

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        #print(b)   #直接打印结果
        yield (b)   #这段代码只要有yield的存在就不叫函数  叫生成器 yield保存了函数的中断状态
        a,b =b,a+b
        n = n + 1
    return 'done'  #用for循环 这里的done就不会被打印 return这里是异常的时候打印的消息

#fib(10)  #生成10个斐波那契数列

#print(fib(10))  #变成了生成器

f=fib(3)    #当__next__超过括号的数字  会出异常 StopIteration: done
g=fib(10)
#----这里是异常处理代码----start---
while True:
    try:
        x = next(g)   #这里和__next__方法一样
        print('g:',x)
    except StopIteration as e:
        print("Generator return value:",e.value)
        break
#----------------end---------------
# print(f.__next__())
# print("七")
# print(f.__next__())
# print("进")
# print(f.__next__())
# print("七")
# print(f.__next__())
# print("出")
# print(f.__next__())

# print("========start loop===自动档======")
# for i in f:
#     print(i)


