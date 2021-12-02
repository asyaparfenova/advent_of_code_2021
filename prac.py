"""This programm calculates the answer
for day 1 challenges of Advent of Code 2021"""

import re
#import numpy as np

def get_input_commands(input_data):
    '''extract lines from input text'''
    # line_re = r'(\d.+)'
    # input_lines = re.findall(line_re, input_data)
    input_lines = input_data.split('\n')
    result = []
    for il in input_lines:
        if il != "":
            res = il.split(" ")
            result.append([res[0], int(res[1])])
    return result

if __name__ == "__main__":
    with open('day2_ex.txt','r') as file:
        data = file.read()
    lines = get_input_commands(data)
    print(lines)
    # print(f"The answer for the 1st task is: {get_increases(mylist)}")
    # print(f"The answer for the 2nd task is: {get_triple_increases(mylist)}")
