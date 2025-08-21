import random   #导入random模块。(生成随机数)

print("-" * 66)
print('欢迎来到猜数游戏')
print('规则一:系统每次会生成一个1~10之间的随机数')
print('规则二:每次游戏最多只能猜3次')
print('规则三:开始游戏输入y，离开游戏输入n')
print("-" * 66)


#   定义一个记录游戏次数的变量
n = 0
z = 0
while True:
    my_sum = input('请输入是否开始游戏:')
    if my_sum == 'y' or my_sum == 'Y':        # 用户想玩
        print(f'这是你第{n}次玩')
        number = random.randint(1,10)       # 生成一个随机数
        n += 1
        for i in range(1,4):
            my_num = int(input('请输入你所猜的数字:'))
            if my_num == number:
                print(f'恭喜你猜对了，答案就是{number}')
                z += 1
                print(f'你通关了{z}次')
                break
            elif my_num > number:
                print(f'你猜的数字大了，还剩{3-i}次机会')
            else:
                print(f'你猜的数字小了，还剩{3-i}次机会')
        else:
            print(f'你三次都猜错了,正确答案是{number}')
    elif my_sum == 'n' or my_sum == 'N':      # 用户不想玩
        print('再见!')
        break
    else:
        print('请输入正确的指令!!')