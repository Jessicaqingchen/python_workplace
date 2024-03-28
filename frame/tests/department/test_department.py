from frame.apis.department import Department


class TestDepartment:
    def setup_class(self):
        self.department = Department()
        self.department.id = 210
        self.creat_data = {
            "name" : "广州研发中心",
            "name_en": "GZYFZX",
            "parentid" : 1,
            "id" : self.department.id
        }
        self.updata_data = {
            "id": self.department.id,
            "name": "广州研发中心aa",
            "name_en": "GZYFZXaa",
            "parentid": 1
        }

    def teardown_class(self):
        pass

    def test_department_flow(self):
        # 部门新增
        creat_data = self.department.creat(self.creat_data)
        # 获取部门列表，判断是否为新增
        _list = self.department.get()
        assert creat_data.json().get("id") in _list.json().get("department")
#         更新部门信息
        self.department.update(self.updata_data)
        _list = self.department.get()
        assert creat_data.json().get("name") in [de.get("name") for de in _list.json().get("department")]

#         删除部门
        self.department.delete("self.department.id")
        _list = self.department.get()
        assert self.department.id not in [de.get("name") for de in _list.json().get("department")]



