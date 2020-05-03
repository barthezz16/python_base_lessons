import unittest
from bowling_engine import analyzing_result, analyzing_result_worldwide


class MyTests(unittest.TestCase):

    def test_1(self):
        result = analyzing_result('XXXXXXXXXX')
        self.assertEqual(result, 200)

    def test_2(self):
        result = analyzing_result('XXXXX-/-/-/-/-/')
        self.assertEqual(result, 175)

    def test_3(self):
        result = analyzing_result_worldwide('XXXXX-/-/-/-/-/')
        self.assertEqual(result, 180)

    def test_4(self):
        result = analyzing_result_worldwide('XXXXXXXXXX')
        self.assertEqual(result, 270)

    def test_error_1(self):
        result = '9934-/1744XX23--4/'
        with self.assertRaises(ValueError) as err:
            analyzing_result(result)
        self.assertEqual('Введено неправильное значение, сумма одного фрейма больше 9 очков', str(err.exception))

    def test_error_2(self):
        result = '1/34-/1744XX23--4/22'
        with self.assertRaises(Exception) as err:
            analyzing_result(result)
        self.assertEqual('Не правильное количество фреймов!', str(err.exception))

    def test_error_3(self):
        result = '/134-/1744XX23--4/'
        with self.assertRaises(ValueError) as err:
            analyzing_result(result)
        self.assertEqual('Spare на первом броске', str(err.exception))

    def test_error_4(self):
        result = '1X34-/1744XX23--4/'
        with self.assertRaises(ValueError) as err:
            analyzing_result(result)
        self.assertEqual('Strike на втором броске', str(err.exception))

    def test_error_5(self):
        result = '0434-/1744XX23--4/'
        with self.assertRaises(ValueError) as err:
            analyzing_result_worldwide(result)
        self.assertEqual('Введено неправильное значение', str(err.exception))
