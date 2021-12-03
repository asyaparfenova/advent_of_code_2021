"""This programm calculates the answer
for day 1 challenges of Advent of Code 2021"""

import re


def get_input_numbers(input_data):
    '''extract input numbers from input data'''
    num_re = r'([0-1]+)'
    input_numbers = re.findall(num_re, input_data)
    return input_numbers


def func(numbers):
    pre_gamma = []
    pre_eps = []
    for n in range(len(numbers[1])):
        pre_gamma.append(0)
        pre_eps.append(0)
    # gamma = ""
    # eps = ""
    for num in numbers:
        for bul in range(len(num)):
            if num[bul] == "1":
                pre_gamma[bul] +=1
                pre_eps[bul] -= 1
                #print(pre_gamma, pre_eps)
            else:
                pre_gamma[bul] -=1
                pre_eps[bul] += 1
                #print(pre_gamma, pre_eps)
    for bul in range(len(num)):
        if pre_gamma[bul] > 0:
            pre_gamma[bul] = "1"
        else:
            pre_gamma[bul] = "0"
        if pre_eps[bul] > 0:
            pre_eps[bul] = "1"
        else:
            pre_eps[bul] = "0"
    gamma = int("".join(pre_gamma), 2)
    eps = int("".join(pre_eps), 2)
    return pre_gamma, pre_eps, gamma * eps

def func2(example, numbers):
    for i in range(len(example)):
        pre_res = []
        if len(numbers) > 1:
            print(len(numbers))
            for num in numbers:
                if num[i] == example[i]:
                    pre_res.append(num)
            numbers = pre_res
            print(numbers)
        else:
            return numbers
    return numbers



if __name__ == "__main__":
    with open('day3_ex.txt','r') as file:
        data = file.read()
    numbers = get_input_numbers(data)
    #print(numbers)
    print(f"The answer for the 1st task is: {func(numbers)[2]}")
    print(f"The answer for the 2nd task is: {func2(func(numbers)[0], numbers)}")
