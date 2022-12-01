import unittest
import calorie_counter


class TestCalorieCounter(unittest.TestCase):

    def test_get_calorie_lists_from_file(self):
        valid_response = {
            'elf0': [1000, 2000, 3000],
            'elf1': [4000],
            'elf2': [5000, 6000],
            'elf3': [7000, 8000, 9000],
            'elf4': [10000]
        }

        result = calorie_counter.get_calories('data/test_calories.txt')
        self.assertDictEqual(result, valid_response)

    def test_get_max_calories_from_calorie_file(self):
        calorie_list = calorie_counter.get_calories('data/test_calories.txt')
        result = calorie_counter.get_highest_calorie_count(calorie_list)
        self.assertEqual(result, 24000)
