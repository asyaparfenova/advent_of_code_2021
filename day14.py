"""This programm calculates the answer
for day-14 challenges of Advent-of-Code-2021"""

def get_data(input_data):
    """extract ..."""
    input_data = input_data.split("\n")
    template = input_data[0]
    pre_rules = input_data[2:]
    rules = {}
    for pr in pre_rules:
        if pr != "":
            res = pr.strip().split(" -> ")
            rules[res[0]]=res[1]
    return template, rules

### PART 1

def step(template, rules):
    """let..."""
    temp_new = ""
    for i in range(len(template) - 1):
        if template[i:i+2] in rules.keys():
            temp_new += (template[i] + rules[template[i:i+2]])
        else:
            temp_new += template[i]
    temp_new += template[-1]
    return temp_new


def steps(template, rules, steps):
    for s in range(steps):
        #print("Step ", s, " starting from ", template[:3], "... with length ", len(template))
        template = step(template, rules)
    return template


def count_answer(template):
    counts = []
    for l in set(template):
        counts.append(template.count(l))
    return max(counts) - min(counts)

### PART 2

def get_couples_dict(template):
    couples_dict = {}
    for i in range(len(template) - 1):
        if template[i:i+2] in couples_dict.keys():
            couples_dict[template[i:i+2]] += 1
        else:
            couples_dict[template[i:i + 2]] = 1
    return couples_dict


def insert(couples_dict, rules):
    new_couples_dict = {}
    for couple in couples_dict.keys():
        if couple in rules.keys():
            new_couples = [couple[0] + rules[couple], rules[couple] + couple[1]]
            for nc in new_couples:
                if nc in new_couples_dict.keys():
                    if couple in couples_dict.keys():
                        new_couples_dict[nc] += couples_dict[couple]
                    else:
                        new_couples_dict[nc] += 1
                else:
                    if couple in couples_dict.keys():
                        new_couples_dict[nc] = couples_dict[couple]
                    else:
                        new_couples_dict[nc] = 1
    return new_couples_dict


def iterate(couples_dict, rules, steps):
    for s in range(steps):
        couples_dict = insert(couples_dict, rules)
    return couples_dict


def count_symbols(couples_dict, template):
    counts = {}
    for k in couples_dict.keys():
        if k[0] in counts:
            counts[k[0]] += couples_dict[k]
        else:
            counts[k[0]] = couples_dict[k]
    counts[template[-1]] += 1
    return counts


if __name__ == "__main__":
    with open("day14_task.txt", "r") as file:
        data = file.read()
    result = get_data(data)
    template = result[0]
    couples_dict = get_couples_dict(template)
    rules = result[1]

    print(f"Answer for the first task: {count_answer(steps(template, rules, 10))}")
    couples_dict = iterate(couples_dict, rules, 40)
    count = count_symbols(couples_dict, template)
    print(f"Answer for the first task: {max(count.values()) - min(count.values())}")

