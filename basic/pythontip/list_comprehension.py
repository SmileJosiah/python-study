events = [x for x in range(1, 10) if x % 2 == 0]
print(events == list(filter(lambda x: x % 2 == 0, range(1, 10))))

squares = [x ** 2 for x in range(1, 10)]
print(squares)
msquares = map(lambda x: x ** 2, range(1, 10))
print(list(msquares))


cords = [(x,y) for x in range(3) for y in range(3) if x > 0]
print(cords)

dns = {
    domain:ip
    for domain in ['github.com','git.io']
    for ip in ['192.168.0.10','23.257.125.142']
}

print(dns)
names = {name for name in ['ana','bob','catty','otocat'] if len(name) > 3}
print(names)

squares = (x for x in range(10) if x % 2==0)
print(list(squares))