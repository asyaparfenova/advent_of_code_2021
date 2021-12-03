"""This programm calculates the answer
for day 3 challenges of Advent of Code 2021"""

import re


def get_input_numbers(input_data):
    """extract diagnostic report from input text
    input data (str): plain text read from txt file
    return: list of str"""
    num_re = r"([0-1]+)"
    input_numbers = re.findall(num_re, input_data)
    return input_numbers


def rate(report, rate_type):
    """generate gamma or epsilon rate
    report (list of str): diagnostic report
    rate_type (str): gamma or epsilon
    return: binary result in form of str"""
    pre_rate = []
    if rate_type == "gamma":
        rt = 1
    elif rate_type == "epsilon":
        rt = -1
    else:
        raise ValueError
    for n in range(len(report[0])):
        pre_rate.append(0)
    for r in report:
        for bul in range(len(r)):
            if r[bul] == "1":
                pre_rate[bul] += rt
            elif r[bul] == "0":
                pre_rate[bul] -= rt
    for bul in range(len(pre_rate)):
        if pre_rate[bul] > 0:
            pre_rate[bul] = "1"
        elif pre_rate[bul] < 0:
            pre_rate[bul] = "0"
        else:
            if rate_type == "gamma":
                pre_rate[bul] = "1"
            elif rate_type == "epsilon":
                pre_rate[bul] = "0"
            else:
                raise ValueError
    rate = "".join(pre_rate)
    return rate


def get_power_consumption(report):
    """generate power consumption by multiplying gamma rate and epsilon rate
    report (list of str): diagnostic report"""
    gamma_rate = int(rate(report, "gamma"), 2)
    epsilon_rate = int(rate(report, "epsilon"), 2)
    return gamma_rate * epsilon_rate


def rate_with_bit_criteria(report, criteria):
    """generate oxygen generator or CO2 scrubber rate
    report (list of str): diagnostic report
    criteria (str): oxygen or scrubber
    return: binary result in form of str"""
    if criteria == "oxygen":
        rate_type = "gamma"
    elif criteria == "scrubber":
        rate_type = "epsilon"
    for i in range(len(report[0])):
        pre_res = []
        if len(report) > 1:
            example = rate(report, rate_type)
            for num in report:
                if num[i] == example[i]:
                    pre_res.append(num)
            report = pre_res
    return report[0]


def get_life_support_rating(report):
    """generate life support rating by multiplying oxygen generator rate and CO2 scrubber rate
    report (list of str): diagnostic report"""
    oxygen_generator_rating = int(rate_with_bit_criteria(report, "oxygen"), 2)
    co2_scrubber_rating = int(rate_with_bit_criteria(report, "scrubber"), 2)
    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == "__main__":
    with open("day3_ex.txt", "r") as file:
        data = file.read()
    report = get_input_numbers(data)
    print(f"The answer for the 1st task is: {get_power_consumption(report)}")
    print(f"The answer for the 2nd task is: {get_life_support_rating(report)}")
