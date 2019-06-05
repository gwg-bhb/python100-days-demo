#素数

from math import sqrt

num = int(input("随便输入一个正整数:"))
end = int(sqrt(num))

is_prime = True

for i in range(2, end+1):
    if num % i == 0:
        is_prime = False
        print("约数:%d" %(i))

if is_prime and num != 1:
    print("%d素数" %(num))
else:
    print("%d合数" %(num))
