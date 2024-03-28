import requests

from frame.utils.jsonschema import JsonSchemaUtils


def test_httpbin_schema():
    '''
    生成针对httpbin的响应信息，生成对应的schema文件
    :return:
    '''
    r = requests.request("GET", "https://httpbin.ceshiren.com/get")
    JsonSchemaUtils.generate_jsonschema_by_file(r.json(), "httpbin.json")

def test_httpbin_req():
    # 1、获取响应信息
    r = requests.request("GET", "https://httpbin.ceshiren.com/get")
    # 2、把响应信息传入到验证方法里面
    validate_res = JsonSchemaUtils.validate_schema_by_file(r.json(), "httpbin.json")
    # 3.验证返回的数据结构是否一致
    assert validate_res == True