# conftest文件中的函数是不需要导入的
# conftest文件中的函数会提前初始化（即加载）
# conftest所在目录必须是python package.位置：项目根目录
# 寻找顺序：先从当前模块找>再从当前目录>上级节点
import time

import pytest

from demo.Calculator import Calculator


@pytest.fixture(scope="class")
def get_calc():
    calc = Calculator()
    yield calc
    print("结束测试")

# autouse 自动应用，如要返回值需要传fixture函数名
@pytest.fixture(autouse=True)
def calcu_fix():
    print("开始计算")
    yield
    print("结束计算")


@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    log_name = './log/' + now + '.logs'

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path((log_name))