#   切片
from dataclasses import replace

s = 'I love Python'
print(s[2:6])
print(s[:4])
print(s[:-5:3])
print(s[::-1])

#   字符串查询

s0 = 'hello python'
print(s0.find('py'))
print(s0.find('hh'))
# s0.index('hh')      #查不到会报错

#   字符串大小写转换

s1 = 'Hello World'
print(s1.upper())
print(s1.lower())

#   字符串切割

s2 = 'I am a student'
print(s2.split(' '))        #切割：按照 进行切割
print(s2.partition(' '))    #分区：按照 进行分区， 单独一个区

#   字符串替换

s3 = 'hello hubei'
print(s3.replace('hubei', 'zhonguo'))

#


