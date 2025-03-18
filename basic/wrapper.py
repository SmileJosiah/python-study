from enum import unique, Enum


def log(func):
    def wrapper(*args, **kwargs):
        print('calling {}'.format(func.__name__))
        result = func(*args, **kwargs)
        print('calling {} done'.format(func.__name__))
        return result

    return wrapper


@log
def say_hello()->int:
    return 42

i = say_hello()
print(i)

class Screen(object):
    width = None
    height = None
    @property
    def resolution(self):
        return (self.width*self.height)

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

class Student:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    def __str__(self):
        return 'Student {}, age {}'.format(self.name, self.age)


s1 = Student('张三',25)
print(s1)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 2
    Tue = 1

print(Weekday.Tue.value)