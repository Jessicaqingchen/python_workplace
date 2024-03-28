import time

from pythonds.basic.stack import Stack
import turtle

def fun(x):
    if x > 0:
        print(x)
        fun(x-1) #X=3,3,2,1

def fun2(x):
    if x > 0:
        print(x)
        fun2(x+1) #X=3,3,4,5

def fun3(x):
    if x > 0:
        fun3(x - 1)
        print(x) #X=3,1,2,3

# n表示N个盘子，a,b,c表示盘子经过的路径a->b->c
def hannoo(n, a, b, c):
    if n > 0:
        hannoo(n-1, a, c, b)
        print("moving form %s to %s" % (a, c))
        hannoo(n - 1, b, a, c)

# 斐波那契数列0 1 1 2 3 5 8 13....
'''
规律：n>2时，第二项等于前两项之和
当n = k(n > 1),f(k) = f(k-1)+f(k-2)
n=0时，f(0)=0
n=1时，f(1)=1
'''
def Fibonacci(n):
    '''从0开始，第0项为0，求第n项'''
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        num = Fibonacci(n-1) + Fibonacci(n-2)
        return num
    return None

def demo():
    l = [i for i in range(1000)]
    return l

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

def turtleDemo():
    '''画出正方形'''
    t = turtle.Turtle()
    for i in range(4):
        t.forward(100)
        t.right(90)
    # turtle.done()
    time.sleep(5)
    '''画出5角星'''
    t.pencolor('red')
    t.pensize(3)
    for i in range(5):
        t.forward(100)
        t.right(144)
    t.hideturtle()
    turtle.done()


if __name__ == '__main__':
    # fun3(3)
    # hannoo(3,"a", "b", "c")
    print(Fibonacci(5))
    print(demo())
    print(parChecker("(())"))
    turtleDemo()

