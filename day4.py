import random

items1 = [1, 2, 5, 4, 5]
# items4=[1,2,5,3,4]
# item2 = ['python','java']
# item3 = [True,False]
# print(items1)
# print(item2)
# print(item3)
#
#
# print(items1[-5])
# print(items1[0:5:2])
# items1[1:1] = ['x','0']
# print(items1)
#
# print(items4==items1)
# items1.remove(5)
# print(items1.count(5))
# items1.sort()
# print(items1)
# items1.reverse()
#
# print(items1)
#
# items = [i for i in range(1, 10) if i % 2 == 0]
# print(items)
# nums1 = [35, 12, 97, 64, 55]
# nums2 = [num ** 2 for num in nums1]
# print(nums2)
# num3 = [num for num in nums1 if num > 50]
# print(num3)


scores = [[random.randrange(60,101) for _ in range(3)] for _ in range(5)]
print(scores)


print('------------------------------------------------------------------------')
# red_balls = list(range(1,34))
# select_balls = []
# for _ in range(6):
#     index = random.randrange(len(red_balls))
#     select_balls.append(red_balls.pop(index))
# select_balls.sort()
#
# for ball in select_balls:
#     print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# blue_ball = random.randrange(1,17)
# print(f'\033[034m{blue_ball:0>2d}\033[0m')

reb_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]

for _ in range(20):
    selected_balls = random.sample(reb_balls,6)
    selected_balls.sort()
    for ball in selected_balls:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    blue_ball =  random.choice(blue_balls)
    print(f'\033[034m{blue_ball:0>2d}\033[0m')


console = Console()
n = int(input('生成几组号码:'))
reb_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]

table = Table(shjo)