#   1.计算1~100的所有奇数的和

# total = 0  # 定义一个结果

# for x in range(1,100,2):
#     total += x

#   第二种写法

# for x in range(100):
#     if x % 2 != 0:
#         total += x


#   第三种写法
# x = 0
# while True:
#     x += 1
#     if x > 100:
#         break       # 结束循环
#     if x % 2 != 0:
#         total += x

#   第四种写法

# for x in range(100):
#     if x % 2 == 0 :
#         continue
#     total += x


# print (f'结果为:{total}')


#   九九乘法表for

# for i in range(1,10):
#     for j in range(1,i):
#         print(f'{i}*{j}={i*j}',end='\t')
#     print()


# while+break版

i = 1
while i <= 9:       #代表九行
    j = 1
    while True:
        if j > i:
            break
        print(f'{j}*{i}={j*i}',end='\t')
        j += 1
    i += 1
    print()

