from calorie_counter import get_calories, get_highest_calorie_count, get_sum_of_top_three_calorie_counts

if __name__ == '__main__':
    calorie_list = get_calories('data/calories.txt')
    max_calories = get_highest_calorie_count(calorie_list)
    sum_top_three = get_sum_of_top_three_calorie_counts(calorie_list)
    print(f'Max Calories is: {max_calories}')
    print(f'Sum of top three is: {sum_top_three}')
