import pytest
from python.unittesting.to_test import even_odd


@pytest.mark.parametrize('test_arg,expected',
                         [(1, 'odd'),
                          (12, 'even'),
                          (-5, 'odd'),
                          (10.0, 'even')])
def test_even_odd(test_arg, expected):
    assert even_odd(test_arg) == expected


@pytest.mark.parametrize('test_arg', [None, 'str'])
def test_even_odd_incorrect_arg(test_arg):
    with pytest.raises(TypeError):
        even_odd(test_arg)
