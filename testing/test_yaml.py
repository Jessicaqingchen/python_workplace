import yaml

def get_datas():
    # safe_load 把yaml格式转成python对象
    # safe_dump 把python对象转成yaml
    with open("./testdata/demo.yaml", encoding="utf-8") as f:
        result = yaml.safe_load(f)
        print(result)
        # 或缺元素
        add_P0_datas = result.get("add2").get("P0").get("datas")
        add_P0_ids = result.get("add2").get("P0").get("ids")
        print(add_P0_datas)
        print(add_P0_ids)
    return [add_P0_datas, add_P0_ids]