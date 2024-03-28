import json

from genson import SchemaBuilder
from jsonschema.validators import validate


def generate_jsonschema(obj):
    # 实例化SchemaBuilder类
    bulider = SchemaBuilder()
    # 调用add_object方法，将要转换成jsonschame的数据传入进去
    bulider.add_object(obj)
    # 转换成jsonschame数据
    return bulider.to_schema()

def generate_jsonschema_file(obj, file_path):
    json_schema_data = generate_jsonschema(obj)
    with open(file_path, "w") as f:
        json.dump(json_schema_data, f)

def test_jsonschema():
    print(generate_jsonschema({"name": 1}))

def validate_schema(data_obj, schema):
    # 在实际使用过程中，不想直接抛异常，而是想返回成功或失败的标志（P or F）
    try:
        validate(data_obj, schema=schema)
        return True
    except Exception as e:
        print("结构体验证失败:", e)
        return False

def test_validate_schema():
    with open("validate.json", "rb") as f:
        json_schema_data = json.load(f)
    assert validate_schema({"name": 1}, schema=json_schema_data)

def test_generate_jsonschema_file():
    generate_jsonschema_file({"name": 1}, "validate.json")