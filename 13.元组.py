t = ()
t0 = ('abc',)
t1 = (1,2,'a','b',34,1,1)

print(t1[1:4])
print(t1[4])

print(t1.index('a'))

print(t1.count(1))

print(len(t1))

for i in t1:
    print(i)
