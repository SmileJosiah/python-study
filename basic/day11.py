import time


class Clock:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def run(self):
        self.second +=1
        if self.second == 60:
            self.second = 0
            self.minute +=1
            if self.minute == 60:
                self.minute = 0
                self.hour +=1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        return f'{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}'


clock = Clock()
# while True:
#     print(clock.show())
#     time.sleep(1)
#     clock.run()

class Student:
    __slots__ = ('name','age')

    def __init__(self,name,age):
        self.name = name
        self.age = age

stu = Student('John',18)


class Triangle(object):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a,b,c):
        return a+b>c and b+c > a and c+a > b

    def perimeter(self):
        return self.a+self.b+self.c

    def area(self):
        p = self.perimeter()/2
        return (p*(p-self.a)* (p-self.b)* (p-self.c)) **0.5

Triangle(1,2,3)