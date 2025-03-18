file = open('/basic/day12.py', 'r', encoding ='utf-8')
# print(file.read())

for line in file:
    print(line,end='')
file.close()



import json

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}

with open('../data.json', 'w', encoding ='utf-8') as f:
    json.dump(my_dict,f)

