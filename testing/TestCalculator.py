# 测试模板
import pytest
from testing.test_yaml import get_datas

from demo.Calculator import Calculator


# pytest类型需要以大写的Test开头，方法名也需要以test开头
class TestCalculator:
    add_P0_datas = get_datas()[0]
    add_P0_ids = get_datas()[1]
    def setup_class(self):
        print("实例化对象")
        self.calc = Calculator()

    # 在每个测试方法之前打印
    # 前置条件：准备测试环境，测试数据之类的
    def setup_method(self):
        print("开始计算")

    # 在每个测试方法之后打印
    # 完成一些资源的销毁
    def teardown_method(self):
        print("结束计算")

    # 整个测试结束后打印
    def teardown_class(self):
        print("结束测试")

    # 标记测试用例优先级
    @pytest.mark.P0
    # 需要至少两个参数，第一个参数是字符串，里面可以存放要传递的参数，以逗号隔开
    # 第二个参数是我们要传递的数据序列（可以列表，元组）每个序列里存放一组数据，以逗号隔开
    @pytest.mark.parametrize(["a", "b", "except1"],[[1,1,2],[-0.01,0.02,0.01],[10,0.01,10.01]],
                             ids=["整型", "浮点型", "整形+浮点型"])
    # ids为测试用例命名
    def test_add0(self, a, b, except1):
#         测试相加方法
        result = self.calc.add(a, b)
        print(result)
        # 实际结果和预期结果进行对比
        assert result == except1

    @pytest.mark.P1
    @pytest.mark.parametrize(["a", "b", "error"], [["中", 9.3, "参数大小超出范围"]])
    def test_add1(self, a, b, error):
#         捕获异常
#         try:
#             result = self.calc.add(a, b)
#             print(result)
#             # 实际结果和预期结果进行对比
#             assert result == error
#         except Exception as e:
#             print("异常信息", e)
# #       捕获异常方法2
        with pytest.raises(Exception) as e:
            result = self.calc.add(a, b)
        print(e)

    # 完成执行顺序的控制（按从小到大顺序），即优先级
    @pytest.mark.run(order=1)
    @pytest.mark.P0
    # 需要至少两个参数，第一个参数是字符串，里面可以存放要传递的参数，以逗号隔开
    # 第二个参数是我们要传递的数据序列（可以列表，元组）每个序列里存放一组数据，以逗号隔开
    @pytest.mark.parametrize(["a", "b", "except1"], add_P0_datas,
                             ids=add_P0_ids)
    # ids为测试用例命名
    def test_add2(self, a, b, except1):
    #         测试相加方法
        result = self.calc.add(a, b)
        print(result)
        # 实际结果和预期结果进行对比
        assert result == except1





#
# class TestCalculator:
#     def setup_method(self):
#         pass
#
#     def teardown_method(self):
#         pass
#
#     expection  = [(1,1,2),(-0.01,0.02,0.01),(10,0.02,10.02),(98.99,99,197.99),
#                   (99,98.99,197.99),(-98.99,-99,-197.99),(-99,-98.99,-197.99),
#                   (99.01,0,'参数大小超出范围'),(-99.01,-1,'参数大小超出范围'),(2,99.01,'参数大小超出范围'),
#                   (1,-99.01,'参数大小超出范围')
#                   ]
#     @pytest.mark.parametrize("first_num,two_num,expected",expection)
#     def test_add0(self,first_num,two_num,expected):
#         # 测试相加方法
#         calc = Calculator()
#         result = calc.add(first_num, two_num)
#         print(result)
#         # 实际结果 对比 预期结果
#         assert result == expected
