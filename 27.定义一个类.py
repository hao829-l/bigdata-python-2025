# 描述一台汽车

class Car:

    def __init__(self):
        # 汽车的品牌
        self.brand = None
        # 汽车的型号
        self.type_name = None
        # 汽车的类型
        self.categorry = None

    def run(self):      #run函数就是汽车的行为
        print('开起来')
