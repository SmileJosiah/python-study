from functools import reduce, partial


def myMap(func,iterable):
    for item in iterable:
        yield func(item)

names = ['zhangsan','lisi']
print(map(lambda x:x.capitalize(),names))
for name in myMap(lambda x:x.capitalize(),names):
    print(name)


def myFilter(func,iterable):
    for item in iterable:
        if func(item):
            yield item

print(filter(lambda x:x%2==0,range(10)))

for item in myFilter(lambda x:x%2==0,range(10)):
    print(item)

print(reduce(lambda x,y:x*y,range(1,5)))

#偏函数
add = lambda x,y:x-y
add1024 = partial(add, 1024)
print(add1024(1))