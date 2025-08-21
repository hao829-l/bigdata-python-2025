# 创建字典


# dict0 = {}      # 空字典
dict1 = {'name':'wanghao','age':18,'address':1113}
dict2 = dict([('name','wh'),('age',18)])
dict3 = dict(name='wl',age = 20,city='hangzho')

# 新增修改
dict3['hangzho'] = 'wuhan'
dict1['age'] = 20

# 删除
# dict1.clear()
# dict1.pop('name')
# del dict1['age']

# 查询
if 'address' in dict1:
    print(dict1['address'])

# 字典中的函数
new_dict = dict.fromkeys('name','age')
new_dict['name'] = '王昊'
print(new_dict)

print(dict1['address'])
print(dict1.get('address'))

# 字典的遍历
# items把所有的向放到一个列表中
for k,v in dict1.items():
    print(f'key = {k}, value = {v}')

for k in dict1.keys():
    print(k)
for v in dict1.values():
    print(v)

print(dict1)

