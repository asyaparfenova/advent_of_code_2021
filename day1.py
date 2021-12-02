"""This program calculates answers
for day-1 challenges of Advent-of-Code-2021"""

import numpy as np

def get_increases(measurements, n):
    """Count the number of times a depth measurement increases for sum of n measurements;
    n(int): sum of how many measurements are we taking for comparison
    measurements (list of int): measurements taken
    returnes (int): count of increases"""
    incr = 0
    for i in range(n, len(numbers)):
        if numbers[i] > numbers[i - n]:
            incr += 1
    return incr

if __name__ == "__main__":
    mylist = np.loadtxt("day1_task.txt", dtype=int)
    print(f"The answer for the 1st task is: {get_increases(mylist, 1)}")
    print(f"The answer for the 2nd task is: {get_increases(mylist, 3)}")
