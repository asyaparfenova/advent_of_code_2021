"""This programm calculates the answer
for day 5 challenges of Advent of Code 2021"""


def get_lines_coordinates(input_data):
    """extract end coordinates from input text
    :input data (str): plain text read from txt file
    :returns end_coordinates (list of list of tuples)"""
    input_lines = input_data.split("\n")
    end_coordinates = []
    for il in input_lines:
        if il != "":
            res = il.strip().split(" -> ")
            end_coordinates.append(
                [
                    (int(res[0].split(",")[0]), int(res[0].split(",")[1])),
                    (int(res[1].split(",")[0]), int(res[1].split(",")[1])),
                ]
            )
    return end_coordinates


def map_vents(point, vents):
    """add coordinate of a single vent to a dictionary of vent coordinates as keys and overlaps count as values
    :point (tuple(int,int): coordinate of a vent
    :vents (dict{tuple:int}: vent points with overlaps count
    :returns _updated_ vents (dict{tuple:int})"""
    if point not in vents:
        vents[point] = 1
    else:
        vents[point] += 1
    return vents


def count_overlaps(end_coordinates, with_diagonals=False):
    """add coordinates of all vents to a dictionary of vent coordinates as keys and overlaps count as values;
    then count overlaps
    :end_coordinates (list of list of tuples): end coordinates of all vent lines
    :with_diagonals (bool): True if we want to take diaginals into account
    :returns count of overlaps (int)"""
    vents = {}
    for ec in end_coordinates:
        if ec[0][0] == ec[1][0]:
            if ec[0][1] > ec[1][1]:
                ec.reverse()
            for i in range(ec[0][1], ec[1][1] + 1):
                point = (ec[0][0], i)
                vents = map_vents(point, vents)
        elif ec[0][1] == ec[1][1]:
            if ec[0][0] > ec[1][0]:
                ec.reverse()
            for i in range(ec[0][0], ec[1][0] + 1):
                point = (i, ec[0][1])
                vents = map_vents(point, vents)
        if with_diagonals:
            if ec[0][1] > ec[1][1]:
                ec.reverse()
            if ec[0][0] - ec[1][0] == ec[1][1] - ec[0][1]:
                for i in range(ec[0][0] - ec[1][0] + 1):
                    point = (ec[0][0] - i, ec[0][1] + i)
                    vents = map_vents(point, vents)
            if ec[0][0] - ec[1][0] == ec[0][1] - ec[1][1]:
                for i in range(ec[1][0] - ec[0][0] + 1):
                    point = (ec[0][0] + i, ec[0][1] + i)
                    vents = map_vents(point, vents)
        result = 0
        for v in vents.values():
            if v > 1:
                result += 1
    return result


if __name__ == "__main__":
    with open("day5_task.txt", "r") as file:
        data = file.read()
    end_coordinates = get_lines_coordinates(data)
    print(f"The answer for the 1st task is: {count_overlaps(end_coordinates)}")
    print(
        f"The answer for the 2nd task is: {count_overlaps(end_coordinates, with_diagonals=True)}"
    )
