class Animal:
    #定义类属性
    name = ""
    color = ""
    age = ''
    gender = ''

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    # 类方法
    def speak(self):
        print(f"{self.name}会叫")

    def run(self):
        print(f"{self.name}会跑")

# 创建猫类，继承Animal
class Cat(Animal):
    def __init__(self, name, color, age, gender):
        # 重写父类构造方法，继承父类的属性（共性）
        super().__init__(name, color, age, gender)
#         添加新的属性（个性）
        self.fur = "短毛"

    def catch_mouse(self):
        print("会捉老鼠")

    # 重写父类speak 方法
    def speak(self):
        print("喵喵叫")

class Dog(Animal):
    def __init__(self, name, color, age, gender):
        # 重写父类构造方法，继承父类的属性（共性）
        super().__init__(name, color, age, gender)
        #         添加新的属性（个性）
        self.fur = "长毛"

    def house_keeping(self):
        print("会看家")

        # 重写父类speak 方法

    def speak(self):
        print("汪汪叫")

    # 重写魔法方法,在实例化的时候会自动打印self.name
    def __repr__(self):
        return f"{self.name}, {self.color}"

# 入口函数，创建类的实例，程序执行入口
if __name__ == '__main__':
    kitty = Cat("kitty", "白色", 3, 1)
    print(kitty.name, kitty.color, kitty.age, kitty.gender, kitty.fur)
    kitty.catch_mouse()

    wangwang = Dog("wangwang", "白色", 2, 1)
    # print(wangwang.name, wangwang.color, wangwang.age, wangwang.gender, wangwang.fur)
    # wangwang.house_keeping()
    print(wangwang)
