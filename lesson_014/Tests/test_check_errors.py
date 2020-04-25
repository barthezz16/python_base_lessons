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
        # self.assertEqual(result, 'Введено неправильное значение, сумма одного фрейма больше 9 очков')
        # TODO Для проверки ошибок есть подобный синтаксис
        # with self.assertRaises(Exception) as err:
        #     get_score(game_result)
        # self.assertEqual("Неверное число ходов", str(err.exception))
        with self.assertRaises(Exception) as err:
            analyzing_result(result)
        self.assertEqual("Введено неправильное значение, сумма одного фрейма больше 9 очков", str(err.exception))
