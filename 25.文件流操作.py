# # 创建/打开文件流
#
# f = open('test.txt', mode = 'r' , encoding = 'utf-8')
#
# # 读的相关操作
# # print(f.read(20))
#
# # print(f.readline())         # 读取一行
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
#
# # print(f.readlines())          # 全部读完
#
# f.close()


# 写的相关操作

# wf = open('test1.txt','w',encoding = 'utf-8')
#
# # 往文件中写入三个hello
# for i in range(4):
#     print(f'当前指针位置是：{wf.tell()}')
#     wf.write('hello\n')

# wf.close()


# 指针的相关操作
#
# # 在第一个hello后面加一个world
# wf = open('test1.txt','r+',encoding = 'utf-8')  # 在指定位置写入数据，会覆盖原有数据
# # 把指针移动到第一个hello后面
# wf.seek(5,0)
# # 把第一个hello后面的内容先读取出来
# after = wf.read()       # 读完之后指针又到了文件末尾
# wf.seek(5,0)
# wf.write('world'+after)
# wf.close()


# with语句来操作文件流
with open('test2.txt','w+',encoding = 'utf-8') as f:
    for i in range(10):
        f.write('python\n')


