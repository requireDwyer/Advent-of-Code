def calculate_score(file):
    with open(file) as file:
        combinations = {
            "AX": 4,
            "AY": 8,
            "AZ": 3,
            "BX": 1,
            "BY": 5,
            "BZ": 9,
            "CX": 7,
            "CY": 2,
            "CZ": 6,
        }

        total = 0
        for line in file:
            current = line[0] + line[2]
            total += combinations[current]
        return total


def calculate_score2(file):
    with open(file) as file:
        combinations = {
            "AX": 3,
            "AY": 4,
            "AZ": 8,
            "BX": 1,
            "BY": 5,
            "BZ": 9,
            "CX": 2,
            "CY": 6,
            "CZ": 7,
        }

        total = 0
        for line in file:
            current = line[0] + line[2]
            total += combinations[current]
        return total


print(calculate_score("day2.txt"))
print(calculate_score2("day2.txt"))
