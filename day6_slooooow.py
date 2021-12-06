"""This programm calculates the answer
for day 2 challenges of Advent of Code 2021"""


def get_input(input_data):
    """extract instructions che from input text
    input data (str): plain text read from txt file"""
    input_data = input_data.replace('\n', '')
    numbers = input_data.strip().split(",")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    return numbers


def solution1(numbers, days):
    """Get result of multiplying a final horizontal position by a final depth
    received by straightforward approach;
    commands(list of list[direction(str), steps(int)]): instructions"""
    for i in range (1, days+1):
        for j in range(len(numbers)):
            if numbers[j] == 0:
                numbers.append(8)
                numbers[j] = 6
            else:
                numbers[j] -= 1
    return len(numbers)


def get_correct_final_coordinates_product(commands):
    """Get result of multiplying a final horizontal position by a final depth
    taking into account the aim value;
    commands(list of list[direction(str), steps(int)]): instructions"""
    hor = 0
    dep = 0
    aim = 0
    for com in commands:
        if com[0] == "up":
            aim -= com[1]
        elif com[0] == "down":
            aim += com[1]
        else:
            hor += com[1]
            dep += com[1] * aim
    return hor * dep


if __name__ == "__main__":
    with open("day6_ex.txt", "r") as file:
        data = file.read()
    numbers = get_input(data)
    print(
        f"The answer for the 1st task is: {solution1(numbers, 256)}"
    )
    # print(
    #     f"The answer for the 2nd task is: {get_correct_final_coordinates_product(commands)}"
    # )
