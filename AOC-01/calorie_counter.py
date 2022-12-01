def get_calories(filename):
    # Read the list of calories carried by each elf
    current_elf = 0
    elfs = {"elf0": []}

    # Read every line in the file and split the contents into groups by blank lines
    with open(filename) as f:
        file_contents = f.readlines()
        for line in file_contents:
            line = line.splitlines()[0]
            if line == "":
                current_elf += 1
                elfs[f'elf{current_elf}'] = []
                continue

            elfs[f'elf{current_elf}'].append(int(line))
        return elfs


def get_highest_calorie_count(calorie_list):
    max_calories = 0
    for elf in calorie_list:
        cur_calories = sum(calorie_list[elf])
        if cur_calories > max_calories:
            max_calories = cur_calories
    return max_calories


def get_sum_of_top_three_calorie_counts(calorie_list):
    elf_totals = [sum(calorie_list[elf]) for elf in calorie_list]
    elf_totals.sort(reverse=True)
    return sum(elf_totals[:3])
