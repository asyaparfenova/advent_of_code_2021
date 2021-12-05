"""This programm calculates the answer
for day 2 challenges of Advent of Code 2021"""


def get_input_commands(input_data):
    """extract instructions che from input text
    input data (str): plain text read from txt file"""
    input_lines = input_data.split("\n")
    result = []
    for il in input_lines:
        if il != "":
            res = il.split(" -> ")
            result.append([[int(res[0].split(',')[0]), int(res[0].split(',')[1])],[int(res[1].split(',')[0]), int(res[1].split(',')[1])]])
    return result

def get_line_coordinates(end_coordinates):
    result = []
    for ec in end_coordinates:
        line = []
        if ec[0][0] == ec[1][0] and ec[0][1] < ec[1][1]:
            for i in range(ec[0][1], ec[1][1] + 1):
                line.append([ec[0][0], i])
        elif ec[0][0] == ec[1][0] and ec[0][1] > ec[1][1]:
            for i in range(ec[1][1], ec[0][1] + 1):
                line.append([ec[0][0], i])
        elif ec[0][1] == ec[1][1] and ec[0][0] < ec[1][0]:
            for i in range(ec[0][0], ec[1][0] + 1):
                line.append([i, ec[0][1]])
        elif ec[0][1] == ec[1][1] and ec[0][0] > ec[1][0]:
            for i in range(ec[1][0], ec[0][0] + 1):
                line.append([i, ec[0][1]])
        if line != []:
            result.append(line)
    return(result)

# def get_line_coordinates2(end_coordinates):
#     result = []
#     for ec in end_coordinates:
#         line = []
#         if ec[0][0] == ec[1][0] and ec[0][1] < ec[1][1]:
#             print("match: ", ec)
#             for i in range(ec[0][1], ec[1][1] + 1):
#                 line.append([ec[0][0], i])
#         elif ec[0][0] == ec[1][0] and ec[0][1] > ec[1][1]:
#             print("match: ", ec)
#             for i in range(ec[1][1], ec[0][1] + 1):
#                 line.append([ec[0][0], i])
#         elif ec[0][1] == ec[1][1] and ec[0][0] < ec[1][0]:
#             print("match: ", ec)
#             for i in range(ec[0][0], ec[1][0] + 1):
#                 line.append([i, ec[0][1]])
#         elif ec[0][1] == ec[1][1] and ec[0][0] > ec[1][0]:
#             print("match: ", ec)
#             for i in range(ec[1][0], ec[0][0] + 1):
#                 line.append([i, ec[0][1]])
#         # diagonals
#         elif ec[0][0] - ec[0][1] == ec[1][0] - ec[1][1] and ec[0][0] < ec[0][1]:
#             print("match: ", ec)
#             for i in range(ec[0][0], ec[0][1] + 1):
#                 line.append([ec[0][0] + i, ec[0][1] - i])
#         elif ec[0][0] - ec[0][1] == ec[1][0] - ec[1][1] and ec[0][0] > ec[0][1]:
#             print("match: ", ec)
#             for i in range(ec[0][1], ec[0][0] + 1):
#                 line.append([ec[0][0] - i, ec[0][1] + i])
#         elif ec[0][0] - ec[0][1] == ec[1][0] - ec[1][1] and ec[0][0] == ec[0][1]:
#             print("match: ", ec)
#             if ec[0][0] < ec[1][0]:
#                 for i in range(ec[0][0], ec[1][0] + 1):
#                     line.append([i,i])
#             else:
#                 for i in range(ec[1][0], ec[0][0] + 1):
#                     line.append([i,i])
#         elif ec[0][0] + ec[0][1] == ec[1][0] + ec[1][1] and ec[0][0] > ec[0][1]:
#             print("match: ", ec)
#             for i in range(ec[0][0] - ec[0][1] + 1):
#                 line.append([ec[0][0] - i, ec[0][1] + i])
#         elif ec[0][0] + ec[0][1] == ec[1][0] + ec[1][1] and ec[0][0] < ec[0][1]:
#             print("match: ", ec)
#             for i in range(ec[0][1] - ec[0][0] + 1):
#                 line.append([ec[0][0] + i, ec[0][1] - i])
#         elif ec[0][0] + ec[0][1] == ec[1][0] + ec[1][1] and ec[1][0] < ec[1][1]:
#             print("match: ", ec)
#             for i in range(ec[1][1] - ec[1][0] + 1):
#                 line.append([ec[1][0] + i, ec[1][1] - i])
#         elif ec[0][0] + ec[0][1] == ec[1][0] + ec[1][1] and ec[1][0] > ec[1][1]:
#             print("match: ", ec)
#             for i in range(ec[1][0] -ec[1][1] + 1):
#                 line.append([ec[1][0] - i, ec[1][1] + i])
#         else:
#             print("NOOO match: ", ec)
#         if line != []:
#             result.append(line)
#     print(" Total lines: ", len(result))
#     return(result)

def get_diagonals(end_coordinates):
    result = []
    for ec in end_coordinates:
        #print(ec)
        if ec[0][1] > ec[1][1]:
            ec.reverse()
        line = []
        if ec[0][0] - ec[1][0] == ec[1][1] - ec[0][1]:
            for i in range(ec[0][0] - ec[1][0] + 1):
                line.append([ec[0][0] - i,ec[0][1] + i])
        if ec[0][0] - ec[1][0] == ec[0][1] - ec[1][1]:
            for i in range(ec[1][0] - ec[0][0] + 1):
                line.append([ec[0][0] + i, ec[0][1] + i])
        # elif ec[0][0] == ec[1][0] and ec[0][1] > ec[1][1]:
        #     for i in range(ec[1][1], ec[0][1] + 1):
        #         line.append([ec[0][0], i])
        # elif ec[0][1] == ec[1][1] and ec[0][0] < ec[1][0]:
        #     for i in range(ec[0][0], ec[1][0] + 1):
        #         line.append([i, ec[0][1]])
        # elif ec[0][1] == ec[1][1] and ec[0][0] > ec[1][0]:
        #     for i in range(ec[1][0], ec[0][0] + 1):
        #         line.append([i, ec[0][1]])
        if line != []:
            result.append(line)
    return (result)


def get_overlaps(full_coordinates):
    vents = {}
    for fc in full_coordinates:
        print(f"_______checking {fc}_________")
        for dot in fc:
            dotstr = f"{dot[0]},{dot[1]}"
            if dotstr not in vents:
                vents[dotstr] = 1
            else:
                print(dotstr)
                vents[dotstr] += 1
        print(vents)
    result = 0
    for v in vents.values():
        if v > 1:
            result += 1
    return result



if __name__ == "__main__":
    with open("day5_task.txt", "r") as file:
        data = file.read()
    commands = get_input_commands(data)
    #print(commands)
    full_coordinates = get_line_coordinates(commands)
    for fc in full_coordinates:
        print("line: ", fc)
    print("----------")
    # full_coordinates2 = get_line_coordinates2(commands)
    # print("----------")
    # for fc in full_coordinates2:
    #     print(fc)
    print("----------")
    diagonals = get_diagonals(commands)
    for d in diagonals:
        print("diagonal: ", d)
    full_coordinates2 = full_coordinates + diagonals
    print(
        f"The answer for the 1st task is: {get_overlaps(full_coordinates)}"
    )
    print(
        f"The answer for the 2nd task is: {get_overlaps(full_coordinates2)}"
    )
