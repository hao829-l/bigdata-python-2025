set1 = set()

set1 = {'asdfg',11,12,13,1.3}
print(len(set1))

# 添加
set1.add(99)
set1.add('hello')
print(set1)

# 删除
set1.remove('hello')
print(set1)

# for可以遍历
for i in set1:
    print(i)