from requests_xml import XMLSession


def test_xml():
    # 设置session
    session = XMLSession()
    url = ""
    r = session.get(url)
    print(r.text)
    # 获取标签<link>里面的数据，返回列表
    print(r.xml.links)
    # xpath 断言
    # 参数1：xpath表达式；参数2：返回第一个查找结果
    item = r.xml.xpath("//item", first=True)
    # 返回的是对象，需要调用text来获取具体的值
    print(item.text)