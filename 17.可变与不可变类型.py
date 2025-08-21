s1 = 'hello world'
print(id(s1))

s1 = 'hello python'
print(id(s1))

print('*' * 58)

lst = [1,2,2,3,4,5]
print(id(lst))

lst.append(0)
lst.pop(2)
print(id(lst))