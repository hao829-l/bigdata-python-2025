lst = []
lst = [12,'abc',34,'xyz',[5,6],12]

# 使用下标进行修改
lst[1] = 'efg'

# 查找
print(lst.index(12))
# 统计
print(lst.count(12))
# 统计
print(len(lst))


# 添加数据
lst.append('hi')
lst.extend('hello')
lst.insert(1,34)

print(lst)

# 删除
# print(lst.pop(2))
# del lst[2]
# lst.remove(34)

# 对字符串逆序
# print(lst[::-1])
lst.reverse()

lst2 = [11,8,6,21,45,30]
lst2.sort()     # 括号里加reverse=True是倒叙
print(lst2)

print(lst)


# for循环遍历
for i in lst:
    print(i)