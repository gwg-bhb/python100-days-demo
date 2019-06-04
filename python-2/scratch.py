"""
使用变量保存数据并进行算术运算

Version: 0.1
Author: 骆昊
"""

# a = 321
# b = 123
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)


# a = int(input('a= '))
# b = int(input('b= '))
# print("%d+%d=%d" %(a, b, a+b))
# print('%d - %d=%d' %(a, b, a-b))
# print('%d * %d = %d' %(a, b, a*b))
# print('%d / %d = %d' %(a, b, a/b))
# print("%d//%d=%d" %(a, b, a//b))
# print("%d**%d=%d" %(a, b, a**b))


"""
使用type()检查变量的类型

Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

g=str("123456")
h=int(100)
print(type(g), type(h))


"""
运算符的使用

Version: 0.1
Author: 骆昊
"""

a = 5
b = 10
c = 3
d = 4
e = 5
a += b
a -= c
a *= d
a /= e
print("a = ", a)

flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag1
print("flag1 = ", flag1)
print("flag2 = ", flag2)
print("flag3 = ", flag3)
print("flag4 = ", flag4)
print("flag5 = ", flag5)
print(flag1 is True)
print(flag2 is not False)


"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: 骆昊
"""

huashi=float(input('huashi= '))
print("将华氏温度转为摄氏温度", "----", type(huashi))

f=1.8*huashi+32
print("f=%f" %(f))

"""
输入半径计算圆的周长和面积

Version: 0.1
Author: 骆昊
"""
import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * (radius**2)
print("周长:", perimeter, "---面积:%f" %(area))

"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: 骆昊
"""

year = int(input("输入年份:"))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print("是闰年吗：", is_leap)


"""
字符串常用操作
Version: 0.1
Author: 骆昊
Date: 2018-02-27
"""

str1 = 'hello, world!'
print('字符串的长度是:', len(str1))
print('单词首字母大写: ', str1.title())
print('字符串变大写: ', str1.upper())
# str1 = str1.upper()
print('字符串是不是大写: ', str1.isupper())
print('字符串是不是以hello开头: ', str1.startswith('hello'))
print('字符串是不是以hello结尾: ', str1.endswith('hello'))
print('字符串是不是以感叹号开头: ', str1.startswith('!'))
print('字符串是不是一感叹号结尾: ', str1.endswith('!'))
str2 = '- \u9a86\u660a'
str3 = str1.title() + ' ' + str2.lower()
print(str3)