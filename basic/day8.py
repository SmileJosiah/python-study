person = dict(name='朱兴义',age=28)
print(person)


items3 = {x:x**3 for x in range(1,10)}
print(items3)
print(len(items3))


person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': ['成都市武侯区科华北路62号1栋101', '北京市西城区百万庄大街1号'],
    'car': {
        'brand': 'BMW X7',
        'maxSpeed': '250',
        'length': 5170,
        'width': 2000,
        'height': 1835,
        'displacement': 3.0
    }
}
print('brand' in person['car'])

#找出股价大于100元的股票并创建一个新的字典。
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stocks2 = {key:value for key,value in stocks.items() if value > 100}
print(stocks2)