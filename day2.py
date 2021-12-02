"""This programm calculates the answer
for day 2 challenges of Advent of Code 2021"""


def get_input_commands(input_data):
    '''extract instructions from input text'''
    input_lines = input_data.split('\n')
    result = []
    for il in input_lines:
        if il != "":
            res = il.split(" ")
            result.append([res[0], int(res[1])])
    return result

def get_final_coordinates_product(commands):
    """Get result of multiplying a final horizontal position by a final depth;
    commands: list[str. int]"""
    hor = 0
    depth = 0
    for com in commands:
        if com[0] == "up":
            depth -= com[1]
        elif com[0] == "down":
            depth += com[1]
        else:
            hor += com[1]
    return hor * depth


def get_corrected_final_coordinates_product(commands):
    """Get result of multiplying a final horizontal position by a final depth;
    commands: list[str. int]"""
    hor = 0
    depth = 0
    aim = 0
    for com in commands:
        if com[0] == "up":
            aim -= com[1]
        elif com[0] == "down":
            aim += com[1]
        else:
            hor += com[1]
            depth += (com[1] * aim)

    return hor * depth



if __name__ == "__main__":
    with open('day2_task.txt', 'r') as file:
        data = file.read()
    commands = get_input_commands(data)
    print(f"The answer for the 1st task is: {get_final_coordinates_product(commands)}")
    print(f"The answer for the 2nd task is: {get_corrected_final_coordinates_product(commands)}")
