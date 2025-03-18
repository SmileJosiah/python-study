obj = {"a":123,"b":234}
for e in obj:
    print(e)

ita = iter([1,2,3])
print(next(ita))
print(next(ita))
print(next(ita))


class Container:
    def __init__(self,start=0,end=0):
        self.start = start
        self.end = end
    def __iter__(self):
        print('[LOG] I made this iterator')
        return self
    def __next__(self):
        print("[LOG] Calling __next__ method!")
        if self.start < self.end:
             i = self.start
             self.start += 1
             return i
        else:
            raise StopIteration

c = Container(0,5)
for i in c:
    print(i)


def container(start=0,end=0):
     while start < end:
         yield start
         start += 1
c = container(0,5)
for i in c:
    print(i)