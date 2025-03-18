import time

print('Hello world')
time.sleep(1)

total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print(total)

total = 0
for i in range(2, 101, 2):
    if i % 2 == 0:
        total += i
print(total)


print(sum(range(1, 101)))


for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end='\t')
    print()