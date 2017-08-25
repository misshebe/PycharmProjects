#python3.x
#-*- coding:utf-8 -*-

# a = "正视你的邪恶"   #现在编码是unicode 因为python3默认 不能指定utf-8就能看中文

a = "正视你的邪恶".encode("utf-8") #unicode转utf-8编码

print(a)