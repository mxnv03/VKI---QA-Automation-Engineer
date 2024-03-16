import pytest


def list_length(list_: list):
    return len(list_)


# возвращает: None если в списке нет четных чисел
def list_finding_average_of_even(list_: list):
    list_of_even = [x for x in list_ if x % 2 == 0]
    if len(list_of_even):
        return sum(list_of_even) / len(list_of_even)


def remove_element_by_value(list_: list, value: int | float | str):
    if value in list_:
        list_.remove(value)
    else:
        raise ValueError
    return list_


# Тесты для списков
class TestListStructure:
    def test_list_length(self):
        assert list_length([-5, -2, 0, 1, 10]) == 5


    @pytest.mark.parametrize("lst, result",
                             [
                                 ([1, 2, 3, 4, 5], 3),
                                 ([-5, -4, -2, 5], -3),
                                 ([1, 3, 5, 7, 9], None),
                                 ([], None),
                                 ([0, 0, 0, 0], 0)
                             ])
    def test_list_finding_average_of_even(self, lst, result):
        assert list_finding_average_of_even(lst) == result

    def test_remove_element_by_value(self):
        with pytest.raises(ValueError):
            assert remove_element_by_value([1, 2, 3, 4], 5) == [1, 2, 3, 4]


def tuple_max_value(tuple_: tuple):
    return max(tuple_)


def tuple_find_value_by_index(tuple_: tuple, index: int):
    return tuple_[index]


# Тесты для кортежей
class TestTupleStructure:
    def test_tuple_max_value(self):
        assert tuple_max_value((1, -5, 6, 100, -100)) == 100

    @pytest.mark.parametrize("tuple_, index, result",
                             [
                                 ((1, 2, 3), 1, 2),
                                 ((1, 2, 3), -1, 3),
                                 ((1, 2, 3, 4), 0, 1)
                             ])
    def test_tuple_find_value_by_index(self, tuple_, index, result):
        assert tuple_find_value_by_index(tuple_, index) == result

    def test_tuple_immutable(self):
        tuple_ = (1, 2, 3)
        with pytest.raises(TypeError):
            tuple_[0] = 4
