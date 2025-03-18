from functools import reduce


def f(x):
    return x * x

r = map(f,[1,2,3,4])
print(list(r))


def add(x,y):
    return x*10+y

print(reduce(add, [1,2,3,4]))

def is_odd(x:int):
    return x % 2 == 1


print(list(filter(is_odd, [1,2,3,4])))

def not_empty(s:str):
    return s and s.strip()
print(list(filter(not_empty,['','1','','','s'])))

def is_palindrome(n):
    return str(n) == str(n)[::-1]

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


def lazy_sum(*args):
    def sum(a):
        ax = 0
        for x in args:
            ax += x
        return ax
    return sum

f = lazy_sum(1,2,3,4,5,6)
print(f(1))



