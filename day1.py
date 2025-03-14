import math

print(0b100)
print(0o100)  # 八进制整数
print(bool('22.54'))


if a:=101:
    print(a)

# f = float(input("请输入华氏温度:"))
# c  = (f-32) /1.8
# print(f'{f:.1f} {c:.1f}')


# radius = float(input("输入圆的半径:"))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
#
# print(f'{perimeter = :.2f}')
# print(f'{area = :.2f}')

year = int(input("输入年份："))
is_leap = year % 4 == 0 and year % 100 !=0 or year % 400 == 0
print(f'{is_leap=}')