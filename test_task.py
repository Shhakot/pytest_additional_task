import pytest


class TestIntClass:
    def test_negative_int_type_first(self):
        test_number = 5.5
        result = test_number % 1
        assert result != 0, "Тип данных не int"

    # предположим, что число int имеет ограничения: от -1000 до 1000, тогда
    # параметры выбраны по граничным значениям числа + число из середины диапазона
    @pytest.mark.parametrize("test_number", [-1000, -999, 0, 999, 1000])
    def test_int_type_second(self, test_number):
        result = test_number % 1
        assert result == 0, "Тип данных не int"


class TestStrClass:
    def test_str_type_first(self):
        test_string = 'тест строки '
        result = test_string * 2
        assert result == 'тест строки тест строки ', "Тип данных не str"

    def test_str_type_second(self):
        test_string = 'тест строки!'
        assert type(test_string) == str, "Тип данных не str"


class TestDictClass:
    def test_dict_type_first(self):
        test_dict = {'a': 1, 'b': 4, 'c': 9}
        result = isinstance(test_dict, dict)
        assert result, "Тип данных не dict"

    def test_dict_type_second(self):
        test_dict = {'a': 1, 'b': 4, 'c': 9}
        assert type(test_dict) == dict, "Тип данных не dict"


