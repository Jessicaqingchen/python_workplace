# fixture 类似于setup teardown的测试装置
import pytest

# @pytest.fixture的作用做测试前后的初始化设置，例如测试数据准备、链接数据库、打开浏览器等操作
# 有pytest.fixture的函数/方法名不能含有test
# 默认是方法级别,最主要用到返回值（多个前置条件用fixture）
@pytest.fixture
def login():
    print("准备登录")
    # 使用yield，yield后面的代码可继续执行，相当于暂停执行,并记住上一次的位置
    # return 停止执行
    yield "username, password"
    print("登出操作")


# scope="class" 相当于setup_class
@pytest.fixture(scope="class")
def conndb():
    print("connect database")

'''
fixture的用法：
1、可以通过方法名传递到测试用例的参数中，进行调用
2、返回使用return 关键字返回数据
3、使用fixture名字来调用返回数据
'''

class TestDemo:
    def test_demo1(self, login, conndb):
        print(f"登录信息：{login}")

    def test_demo2(self, login):
        print("demo")

