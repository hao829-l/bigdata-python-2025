# 1.计算1~100的所有奇数的和

my_sum = 0      #  定义一个结果
n = 1
while 1 <= n <= 100:
    if n % 2 == 1:
        my_sum += n
    n += 1
print(f'计算结果是{my_sum}')



# 2.输出九九乘法表

i = 1
while i <= 9:       #代表九行
    j = 1
    while j <= i:
        print(f'{j}*{i}={j*i}',end='\t')
        j += 1
    i += 1
    print()
