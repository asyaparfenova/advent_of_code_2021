"""This programm calculates the answer
for day 2 challenges of Advent of Code 2021"""

def get_data(input_data):
    """extract ..."""
    input_data = input_data.split("\n")
    # numbers = input_data.strip().split(",")
    # for i in range(len(numbers)):
    #     numbers[i] = int(numbers[i])
    # school_dict = EMPTY_SCHOOL_DICT.copy()
    # for n in numbers:
    #     school_dict[n] += 1
    template = input_data[0]
    pre_rules = input_data[2:]
    rules = {}
    for pr in pre_rules:
        if pr != "":
            res = pr.strip().split(" -> ")
            rules[res[0]]=res[1]
    return template, rules


def step(template, rules):
    """let..."""
    temp_new = ""
    for i in range(len(template) - 1):
        # print("Checking: ", template[i:i + 2])
        if template[i:i+2] in rules.keys():
            # print("BINGO!")
            temp_new += (template[i] + rules[template[i:i+2]])
            # print(temp_new)
        else:
            temp_new += template[i]
            # print(temp_new)
    temp_new += template[-1]
    return temp_new

def steps(template, rules, steps):
    for s in range(steps):
        print("Step ", s, " starting from ", template[:3], "... with length ", len(template))
        count_answer(template)
        template = step(template, rules)
    return template

def count_answer(template):
    counts = []
    for l in set(template):
        counts.append(template.count(l))
        print(l, " : ",template.count(l))
    return max(counts) - min(counts)

if __name__ == "__main__":
    with open("day14_ex.txt", "r") as file:
        data = file.read()
    result = get_data(data)
    template = result[0]
    rules = result[1]
    print(template)
    template = steps(template, rules, 7)
    print("---finally---")
    print(count_answer(template))

