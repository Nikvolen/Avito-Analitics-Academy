import unittest
from one_hot_encoder import fit_transform


class TestOneHotEncoder(unittest.TestCase):

    def test_cities_eq(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_ints_eq(self):
        ints = [1, 2, 3, 4, 4, 2]
        expected = [
            (1, [0, 0, 0, 1]),
            (2, [0, 0, 1, 0]),
            (3, [0, 1, 0, 0]),
            (4, [1, 0, 0, 0]),
            (4, [1, 0, 0, 0]),
            (2, [0, 0, 1, 0])
        ]
        transformed = fit_transform(ints)
        self.assertEqual(expected, transformed)

    def test_cities_not_eq(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Tokyo', [0, 0, 1]),
            ('Tokyo', [0, 0, 1]),
            ('Toronto', [0, 1, 0]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertNotEqual(transformed_cities, exp_transformed_cities)

    def test_cities_not_in(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        transformed = fit_transform(cities)
        self.assertNotIn('Tokyo', transformed)

    def test_exception(self):
        data = 1337
        with self.assertRaises(TypeError):
            fit_transform(data)


if __name__ == '__main__':
    unittest.main()
