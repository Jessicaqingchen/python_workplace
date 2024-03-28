import json

from genson import SchemaBuilder
from jsonschema.validators import validate


class JsonSchemaUtils:
    @classmethod
    def validate_schema_by_file(cls, data_obj, schema_file):
        with open(schema_file) as f:
            schema_data = json.load(f)
        return cls.validate_schema(data_obj, schema_data)

    @classmethod
    def validate_schema(cls, data_obj, schema):
        '''
        通过schema 验证数据
        :param data_obj:
        :param schema:
        :return:
        '''
        # 在实际使用过程中，不想直接抛异常，而是想返回成功或失败的标志（P or F）
        try:
            validate(data_obj, schema=schema)
            return True
        except Exception as e:
            print("结构体验证失败:", e)
            return False

    @classmethod
    def generate_jsonschema_by_file(cls, obj, file_path):
        schema_data = cls.generate_jsonschema(obj)
        with open(file_path, "w") as f:
            schema_data = json.dump(schema_data, f)

    @classmethod
    def generate_jsonschema(cls, obj):
        '''
        生成schema数据
        :param obj:
        :return:
        '''
        # 实例化SchemaBuilder类
        bulider = SchemaBuilder()
        # 调用add_object方法，将要转换成jsonschame的数据传入进去
        bulider.add_object(obj)
        # 转换成jsonschame数据
        return bulider.to_schema()

