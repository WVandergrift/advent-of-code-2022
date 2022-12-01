from calorie_counter import get_calories, get_highest_calorie_count

if __name__ == '__main__':
    calorie_list = get_calories('data/calories.txt')
    max_calories = get_highest_calorie_count(calorie_list)
    print(f'Max Calories is: {max_calories}')
