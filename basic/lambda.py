print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def build(x, y):
    return lambda: x + y


print(build(1, 2)())

print(list(filter(lambda x: x % 2 == 1, range(1, 20))))
