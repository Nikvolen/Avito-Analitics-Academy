import pytest
from one_hot_encoder import fit_transform


def test_cities_eq():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert fit_transform(cities) == exp_transformed_cities


def test_ints_eq():
    ints = [1, 2, 3, 4, 4, 2]
    expected = [
        (1, [0, 0, 0, 1]),
        (2, [0, 0, 1, 0]),
        (3, [0, 1, 0, 0]),
        (4, [1, 0, 0, 0]),
        (4, [1, 0, 0, 0]),
        (2, [0, 0, 1, 0])
    ]
    assert fit_transform(ints) == expected


def test_cities_not_eq():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    exp_transformed_cities = [
        ('Tokyo', [0, 0, 1]),
        ('Tokyo', [0, 0, 1]),
        ('Toronto', [0, 1, 0]),
        ('London', [1, 0, 0]),
    ]
    assert fit_transform(cities) != exp_transformed_cities


def test_cities_not_in():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    assert 'Tokyo' not in fit_transform(cities)


def test_exception():
    data = 1337
    with pytest.raises(TypeError):
        fit_transform(data)





