import unittest
from bowling_engine import analyzing_result


class MyTests(unittest.TestCase):

    def test_1(self):
        result = analyzing_result('XXXXXXXXXX')
        self.assertEqual(result, 200)

    def test_2(self):
        result = analyzing_result('XXXXX-/-/-/-/-/')
        self.assertEqual(result, 175)

    def test_3(self):
        result = analyzing_result('9934-/1744XX23--4/')
        self.assertEqual(result, 'Введено неправильное значение, сумма одного фрейма больше 9 очков')
