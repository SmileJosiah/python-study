s1 = 'hello world \\'
print(s1)

s2 = r'\it \is \time \to \read \now'
print(s2)
s3 = '\141\142\143\x61\x62\x63'
s4 = '\u9a86\u660a'
print(s3)
print(s4)


s5 ='hello' + ', ' + 'world'
print(s5)

s6 = '!' * 3
print(s6)
print(s5+s6)
print(s5*2)

s7 = 'hello world'
s8 = 'goodbye,world'
print('world' in s7)
print('world' not in s7)
print(s8 in s7)


print(len('hello world'))
print(len('goodbye, world'))

for c in list(s7):
    print(c,end='')

print()
print(s7.capitalize())
print(s7.title())
print(s7.upper())
print(s7.lower())
print(s7.find('world'))

print(s7.startswith('hello'))
print(s7.isdigit())
print(s7.isalnum())


print(s7.center(16,'*'))
print(len(s7))
print(s7.zfill(16))


s9 = ' hello world '
print(s9.strip())
print(s9.lstrip())
print(s9.rstrip())

s = 'hello, good world'
print(s.replace('o', '@'))     # hell@, g@@d w@rld
print(s.replace('o', '@', 1))
s = 'I love you'
words = s.split()
print(words)
print('~'.join(words))