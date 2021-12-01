'''This programm calculates the answer
for day 1 challenges of Advent of Code 2021'''

import numpy as np

def get_increases(numbers):
    '''Count the number of times a depth measurement increases;
    numbers: list'''
    incr = 0
    for i in range(1,len(numbers)):
        if numbers[i] > numbers[i-1]:
            incr += 1
    return incr

def get_triple_increases(numbers):
    '''Count the number of times the sum of measurements in this three-measurement-sliding window increases;
    numbers: list'''
    incr = 0
    for i in range(3,len(numbers)):
        if numbers[i]+numbers[i-1]+numbers[i-2] > numbers[i-1]+numbers[i-2]+numbers[i-3]:
            incr += 1
    return incr

if __name__ == "__main__":
    mylist = np.loadtxt("day1_task.txt", dtype=int)
    print(f'The answer for the 1st task is: {get_increases(mylist)}')
    print(f'The answer for the 2nd task is: {get_triple_increases(mylist)}')