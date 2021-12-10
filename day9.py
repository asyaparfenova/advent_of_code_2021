"""This program calculates the answer
for day-9 challenges of Advent-of-Code-2021"""

from functools import reduce


def get_input_numbers(input_data):
    """convert text input into matrix (list of lists(int)
    with additional lines of max values(=9) around"""
    heightmap = input_data.split("\n")
    for l in range(len(heightmap)):
        if heightmap[l] == "":
            heightmap.remove(heightmap[l])
        else:
            heightmap[l] = "9" + heightmap[l] + "9"
    heightmap.insert(0, "9" * len(heightmap[0]))
    heightmap.append("9" * len(heightmap[0]))
    for l in range(len(heightmap)):
        heightmap[l] = list(heightmap[l])
        for m in range(len(heightmap[l])):
            heightmap[l][m] = int(heightmap[l][m])
    return heightmap


def recognize_central_min(heightmap, l, m):
    """recognize central minimum"""
    neighbours = [
        heightmap[l + 1][m],
        heightmap[l][m - 1],
        heightmap[l][m + 1],
        heightmap[l - 1][m],
    ]
    cntr = heightmap[l][m]
    if cntr == min(neighbours + [cntr]) and cntr < min(neighbours):
        return (l, m)
    return None


def get_central_mins(heightmap):
    """generates list of central minimums"""
    central_mins = []
    for l in range(1, len(heightmap) - 1):
        for m in range(1, len(heightmap[l]) - 1):
            central_min = recognize_central_min(heightmap, l, m)
            if central_min:
                central_mins.append(central_min)
    return central_mins


def get_risks_sum(heightmap):
    """calculate sum of the risk levels of all low points on a given heightmap"""
    central_mins = get_central_mins(heightmap)
    risks_sum = 0
    for central_min in central_mins:
        risks_sum += heightmap[central_min[0]][central_min[1]] + 1
    return risks_sum


def flood_fill(heightmap):
    """generate list of enclosed areas sizes (using so called FLOOD-FILL algorithm)"""
    areas = []

    def fill(heightmap, l, m):
        nonlocal area
        if heightmap[l][m] not in [9, -1]:
            heightmap[l][m] = -1
            area += 1
        for x, y in [(l + 1, m), (l, m - 1), (l, m + 1), (l - 1, m)]:
            if heightmap[x][y] not in [9, -1]:
                fill(heightmap, x, y)
        return

    central_mins = get_central_mins(heightmap)
    for l, m in central_mins:
        area = 0
        fill(heightmap, l, m)
        areas.append(area)

    return areas


if __name__ == "__main__":
    with open("day9_task.txt", "r") as file:
        data = file.read()
    heightmap = get_input_numbers(data)
    print(f"The answer for the 1st task is: {get_risks_sum(heightmap)}")
    x = flood_fill(heightmap)
    x.sort()
    print(
        f"The answer for the 2nd task is: {reduce(lambda x, y: x*y, (x[-3:]))}"
    )
