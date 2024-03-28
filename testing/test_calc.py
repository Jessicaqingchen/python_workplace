import logging

import allure
import pytest
from pytest_assume.plugin import assume

from testing.test_yaml import get_datas

from demo.Calculator import Calculator

# pytest类型需要以大写的Test开头，方法名也需要以test开头
# allure.feature定义模块名
@allure.feature("计算器加法功能")
class TestCalculator:
    add_P0_datas = get_datas()[0]
    add_P0_ids = get_datas()[1]

    # allure.story定义小的功能名
    @allure.story("相加功能")
    # 标记测试用例优先级
    @pytest.mark.P0
    # 需要至少两个参数，第一个参数是字符串，里面可以存放要传递的参数，以逗号隔开
    # 第二个参数是我们要传递的数据序列（可以列表，元组）每个序列里存放一组数据，以逗号隔开
    @pytest.mark.parametrize(["a", "b", "except1"],[[1,1,2],[-0.01,0.02,0.01],[10,0.01,10.01]],
                             ids=["整型", "浮点型", "整形+浮点型"])
    # ids为测试用例命名
    def test_add0(self, get_calc, a, b, except1):
        logging.info(f"参数{a}, {b}, 期望结果{except1}")
#         测试相加方法
        with allure.step("相加操作："):
            result = get_calc.add(a, b)
        logging.info(f"结果为：{result}")
        with allure.step("结果验证："):
            # 实际结果和预期结果进行对比
            # assume多重断言
           with assume: assert result == except1

