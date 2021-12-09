"""This programm calculates the answer
for day 9 challenges of Advent of Code 2021"""

from functools import reduce

def get_input_numbers(input_data):
    """extract diagnostic report from input text
    input data (str): plain text read from txt file
    return: list of str"""
    input_numbers = input_data.split("\n")
    for l in range(len(input_numbers)):
        if input_numbers[l] == "":
            input_numbers.remove(input_numbers[l])
        else:
            input_numbers[l] = "9" + input_numbers[l] + "9"
            #input_numbers[l] = list(input_numbers[l])
    input_numbers.insert(0, "9"*len(input_numbers[0]))
    input_numbers.append("9" * len(input_numbers[0]))
    for l in range(len(input_numbers)):
        input_numbers[l] = list(input_numbers[l])
        for m in range(len(input_numbers[l])):
            input_numbers[l][m] = int(input_numbers[l][m])

    return input_numbers


def get_central_min(mtrx, l, m):
    """generate ..."""
    li1 = (mtrx[l+1][m], mtrx[l][m-1], mtrx[l][m], mtrx[l][m+1], mtrx[l-1][m])
    li2 = (mtrx[l + 1][m], mtrx[l][m - 1], mtrx[l][m + 1], mtrx[l - 1][m])
    if mtrx[l][m] == min(li1) and min(li1) < min(li2):
        return mtrx[l][m] + 1
    return 0


def get_risks_sum(mtrx):
    """generate ..."""
    s = 0
    for l in range(1, len(mtrx)-1):
        for m in range(1, len(mtrx[l])-1):
            s += get_central_min(mtrx, l, m)
    return s


def flood_fill(mtrx): # THIS CALLED FLOOD-FILL ALGORITHM
    """generate ..."""
    areas = []
    def fill(mtrx, l, m):  # , area):
        nonlocal area
        if mtrx[l][m] not in [9, -1]:
            mtrx[l][m] = -1
            area += 1
            # print(f"repainted: mtrx[{l}][{m}] AREA IS {area}")
        # elif mtrx[l][m] == 9:
        #     return area
        # li = [mtrx[l + 1][m], mtrx[l][m - 1], mtrx[l][m + 1], mtrx[l - 1][m]]
        if mtrx[l + 1][m] not in [9, -1]:
            fill(mtrx, l + 1, m)  # , area)
        if mtrx[l][m - 1] not in [9, -1]:
            fill(mtrx, l, m - 1)  # , area)
        if mtrx[l][m + 1] not in [9, -1]:
            fill(mtrx, l, m + 1)  # , area)
        if mtrx[l - 1][m] not in [9, -1]:
            fill(mtrx, l - 1, m)  # , area)
        return
    for l in range(1, len(mtrx)-1):
        for m in range(1, len(mtrx[l])-1):
            area = 0
            fill(mtrx, l, m)
            areas.append(area)
    return areas





if __name__ == "__main__":
    with open("day9_task.txt", "r") as file:
        data = file.read()
    report = get_input_numbers(data)
    # print(report)
    print("------")
    print(get_risks_sum(report))
    mtrx = report.copy()
    x = flood_fill(mtrx)
    print("------")
    # for m in mtrx:
    #     print(m)
    print("------")
    x.sort()
    print("areas : ", reduce(lambda x, y: x*y, (x[-3:])))
    # print(f"The answer for the 1st task is: {get_power_consumption(report)}")
    # print(f"The answer for the 2nd task is: {get_life_support_rating(report)}")
