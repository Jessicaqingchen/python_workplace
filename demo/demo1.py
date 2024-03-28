'''
1、三三数之剩二，五五数之剩三，七七数之余二，问几何？
要求：请编写一段python代码，找出1到100（包含首尾）之间的所有符合条件的整数

'''
import calendar

for i in range(1, 101): #range是包头不包尾
    if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
        print(f"符合条件的整数：", i)

i = 1
while i <= 100:
    if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
        print(f"符合条件的整数：{i}")
    i += 1

'''
2、今有雉兔同笼，上有三十五头，下有九十四足，问雉兔各几何？
这四句话的意思是：有若干只鸡和兔子同在一个笼子里，从上面数，有35个头，从下面数，有94只脚。问：笼中各有多少只鸡和兔？
'''
# 思路分析
# 1、x + y = 35; 2x + 4y = 94
# 2、双循环
for x in range(36):
    for y in range(36):
        if (x + y) == 35 and (2 * x + 4 * y) == 94:
            print(f"鸡有{x}只， 兔子有{y}只")


'''
给定一个四位数字表示年份（1583年~4000年之间），请编写一个函数，找出这年出现次数最多的是星期几，返回数据的给是为列表，
元素为英文字符串，并且按照Monday到Sunday的顺序排列。
'''
def solution(year: int):
#     定义一个星期
    weekday = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sta", "Sun"]
#   定义一年有多少天
#     if calendar.isleap(year):
#         days = 366
#     else:
#         days = 365
    days = 365 if calendar.isleap(year) else 365
# 求出第一天是周几
    beginIndex = calendar.weekday(year, 1, 1)
    # 返回的是索引
    # print(beginIndex)
# 求出余下天数
    rest = days % 7
    # print(rest)

    # 对结果进行判断
    if rest == 1:
        return [weekday[beginIndex]]
    elif rest == 2:
        if beginIndex == 6:
            return [weekday[0], weekday[beginIndex]]
        else:
            return [weekday[beginIndex], weekday[beginIndex + 1]]


if __name__ == '__main__':
    data = solution(2022)
    print(data)
    assert solution(2022) == ['Sta']
    assert solution(2860) == ['Thu', 'Fri']

