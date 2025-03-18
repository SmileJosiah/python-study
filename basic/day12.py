# from enum import Enum
#
#
# class Suite(Enum):
#     SPADE,HEART,CLUB,DIAMOND = range(4)
#
#
#  class Card:
#      def __init__(self,suit,value):
#          self.suit = suit
#          self.value = value
#
from abc import ABCMeta, abstractmethod


class Employee(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def salary(self):
        return 15000.0

class Programmer(Employee):
    def __init__(self,name,work_hour = 0):
       super().__init__(name)
       self.work_hour = work_hour
    def salary(self):
        return 200.0 * self.work_hour

class Salesman(Employee):
    def __init__(self,name,sales=0):
        super().__init__(name)
        self.sales = sales
    def salary(self):
        return 1800.0 + self.sales *0.05

emps = [Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'), Programmer('荀彧'), Salesman('张辽')]
for emp in emps:
    if isinstance(emp, Programmer):
        emp.work_hour = int(input(f'请输入{emp.name}本月的工作时间:'))
    elif isinstance(emp, Salesman):
        emp.sales = float(input(f'请输入{emp.name}本月的销售额:'))
    print(f'{emp.name}本月工资为:￥{emp.salary():.2f}')

