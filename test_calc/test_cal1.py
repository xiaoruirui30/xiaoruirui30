import pytest
import yaml


class Calculator:
    def cal_add(self, a, b):
        return a + b

    def cal_sub(self, a, b):
        return a - b

    def cal_mul(self, a, b):
        return a * b

    def cal_div(self, a, b):
        return a / b


with open('test_data.yml') as f:
    data = yaml.safe_load(f)['add']
    add_data = data['datas']
    print(add_data)
    te_name = data['myid']
    print('te_name')


class TestCalc:

    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize(
        'a, b, expect',
        add_data, ids=te_name
    )
    # @pytest.mark.parametrize(
    #     'a, b, expect',
    #  [
    #      (1,3,4),
    #      (2,3,5),
    #      (2,4,6)
    #  ]
    # )

    def test_add(self, a, b, expect):
        result = self.cal.cal_add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect
