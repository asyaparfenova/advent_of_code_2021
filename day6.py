"""This programm calculates the answer
for day 2 challenges of Advent of Code 2021"""

EMPTY_SCHOOL_DICT = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

def get_lanternfish_school(input_data):
    """extract initial fish school state
    :input data (str): plain text read from txt file
    :returns dict{int:int}: initial state of fish school, count by internal timer"""
    input_data = input_data.replace('\n', '')
    numbers = input_data.strip().split(",")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    school_dict = EMPTY_SCHOOL_DICT.copy()
    for n in numbers:
        school_dict[n] += 1
    return school_dict


def spawn(school_dict, days):
    """let the fish school spawn for the given number of days
    :school_dict(dict{int:int}): initial state of fish school, count by internal timer
    :days(int): number of days we want them to spawn
    :returns (int): result number of fish"""
    for i in range (1, days+1):
        staged_dict = EMPTY_SCHOOL_DICT.copy()
        for j in staged_dict.keys():
            if j == 8:
                staged_dict[j] = school_dict[0]
            elif j == 6:
                staged_dict[j] = school_dict[7] + school_dict[0]
            else:
                staged_dict[j] = school_dict[j+1]
        school_dict = staged_dict
    count = 0
    for j in school_dict.keys():
        count += school_dict[j]
    return count


if __name__ == "__main__":
    with open("day6_task.txt", "r") as file:
        data = file.read()
    school = get_lanternfish_school(data)
    print(
        f"The answer for the 1st task is: {spawn(school, 80)}"
    )
    print(
        f"The answer for the 2nd task is: {spawn(school, 256)}"
    )
