tuple1 = (1,2,3,6666)
tuple2 = (1,2,3,6666,'Hello',True)
print(type(tuple1))
print(type(tuple2))

print(len(tuple1))
print(len(tuple2))
print(type((11,)))
a= 1,10,100
print(type(a))
i,j,k,*l = a
print(i,j,k,*l)


a,*b,c = 'hello'
print(a,b,c)

a = 20
b=10
c= 30
a,c,b = b,a,c
print(a,b,c)


