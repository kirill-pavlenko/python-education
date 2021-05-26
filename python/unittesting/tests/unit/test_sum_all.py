import pytest
from python.unittesting.to_test import sum_all


@pytest.mark.parametrize('test_args,expected',
                         [((1, 2, 3, 4), 10),
                          (1, 1),
                          ((-5.0, 3), -2.0),
                          ((float('inf'), 3, -100), float('inf'))])
def test_even_odd(test_args, expected):
    if hasattr(test_args, '__iter__'):
        assert sum_all(*test_args) == expected
    else:
        assert sum_all(test_args) == expected


@pytest.mark.parametrize('test_args',
                         [[],
                          ['1', '2', 3]])
def test_even_odd_incorrect_args(test_args):
    with pytest.raises(TypeError):
        sum_all(test_args)
