class Human:
    '''人类'''

    # 类属性
    on_earth = True
    population = 0

    # 构造方法
    def __init__(self, name, age, salary):
        # 实例属性
        self.name = name
        self.__age = age
        # __name 不能读写，实例无法访问，只能通过类访问
        self.__salary = salary

    # property的作用是把一个方法绑定为一个属性，访问方式为：实例.get_age
    @property
    def get_age(self):
        return self.__age

    # setter前面的age为get_age
    @get_age.setter
    def get_age(self, value):
        if value < 0 or value > 150:
            print("离谱")
        else:
            self.__age = value


#     实例方法
    def speak(self):
        print(self.name, self.age)

#   类方法
    @classmethod
    def load_from_csv(cls):
        pass

#     静态方法
    @staticmethod
    def war():
        pass

if __name__ == '__main__':
    stu = Human("李白", 36, 80000)
    print(stu.get_age)
    stu.get_age = -1
    print(stu.get_age)