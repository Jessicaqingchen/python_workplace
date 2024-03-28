'''
抢红包案例

某群有多个成员，群主给成员发普通红包。

发红包的规则是：
1、群主负责发红包，不能抢红包。红包金额从群主余额中扣除，按成员人数平均分成n等份，以备领取。
每个红包的金额为整数，如果有余数则加到最后一个红包中。
2、成员负责抢红包。抢到的红包金额存到自己余额中。
3、抢完红包后需要进行报数，打印格式“我是XX，现在有 XX 块钱。”。

请根据描述信息，完成案例中所有类的定义、类之间的继承关系，以及发红包、抢红包的操作。
'''
import random

'''
思路分析：
1、分析有几个对象，即定义几个类，如：群主，群员，红包。发红包，抢红包方法
2、分析对象要做的事情，以及要定义的属性
如：群主：name,余额，发红包【分好的红包list】，报数
    群员：name,余额，抢红包[list]，报数
'''
class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money
    def show(self):
        print(f"我是{self.name},我现在有{self.money}钱")

class Manager(Person):
    #     群主发红包
    def send(self, money, num):
        # 定义空的红包容器
        red_list = []
        # 判断群主红包是否够
        if self.money < money:
            print("余额不够发红包，请充值")
            return None
    # 扣钱
        self.money -= money

        # 瓜分算法(整除)
        avg = money // num
        rest = money % num
        for i in range(num):
            red_list.append(avg)
        # 每个红包的金额为整数，如果有余数则加到最后一个红包中
        red_list[-1] += rest
        return red_list

class Menber(Person):
    def garb(self, red_list: list):
        '''
        成员负责抢红包。抢到的红包金额存到自己余额中
        '''
        # 判断红包不为空
        if not red_list:
            print("红包抢完了")
            return None
        random_index = random.randint(0, len(red_list) - 1)
        lucky_money = red_list.pop(random_index)

#         存钱
        self.money += lucky_money


if __name__ == '__main__':
    manager = Manager("李白", 10000)
    # 发红包
    reds = manager.send(100, 3)
    print(reds)

    test1 = Menber("壮壮", 0)
    test1.garb(reds)
    print(len(reds))
    # print(manager.show())

    input_list = [(6, 'apple'), (1, 'google'), (4, 'future'),
                  (1, 'stand'), (6, 'zero')]
    result = sorted(input_list, key= lambda x: (x[0], x[1]))
    result2 = sorted(input_list)
    print("***************")
    print(result)
    print("***************")
    print(result2)