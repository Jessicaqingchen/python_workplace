import requests


def cookie_request():
    url = ""
    # 方法1：cookie放在请求头传递
    # header = {"Cookie": ""}
    # r = requests.request("GET", url=url, headers=header)
    # print(r.request.headers)
    # 方法2：定义一个cookie参数，再传递cookie值
    cookie_data = ""
    r = requests.request("GET", url=url, cookies=cookie_data)
    print(r.request.headers)
