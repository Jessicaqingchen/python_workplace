import requests


def file_request():
    '''
    解决接口测试流程中文件上传问题
     - 指定name
     - 指定filename
     - 指定Content-type
    :return:
    '''
    url = "https://httpbin.ceshiren.com/post"
    # files value是通过元组的形式传递，实现指定filename需求
    r = requests.request("POST", url=url,
                         files={"filename": open('1.txt', "rb")},
                         proxies={"https://127.0.01：8080"},
                         verify=False)
    r.json()