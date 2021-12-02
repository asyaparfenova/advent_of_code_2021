"""This programm calculates the answer
for day 2 challenges of Advent of Code 2021"""


def get_input_commands(input_data):
    """extract instructions che from input text
    input data (str): plain text read from txt file"""
    input_lines = input_data.split("\n")
    result = []
    for il in input_lines:
        if il != "":
            res = il.split(" ")
            result.append([res[0], int(res[1])])
    return result


def get_first_guess_coordinates_product(commands):
    """Get result of multiplying a final horizontal position by a final depth
    received by straightforward approach;
    commands(list of list[direction(str), steps(int)]): instructions"""
    hor = 0
    dep = 0
    for com in commands:
        if com[0] == "up":
            dep -= com[1]
        elif com[0] == "down":
            dep += com[1]
        else:
            hor += com[1]
    return hor * dep


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
    with open("day2_task.txt", "r") as file:
        data = file.read()
    commands = get_input_commands(data)
    print(
        f"The answer for the 1st task is: {get_first_guess_coordinates_product(commands)}"
    )
    print(
        f"The answer for the 2nd task is: {get_correct_final_coordinates_product(commands)}"
    )
