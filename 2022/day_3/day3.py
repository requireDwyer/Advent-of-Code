def common_letter_half(file):
    with open(file) as file:
        total = 0
        for line in file:
            seen = set()
            for i in range(len(line) // 2):
                seen.add(line[i])

            for i in range(len(line) // 2, len(line)):
                if line[i] in seen:
                    total += letter_to_number(line[i])
                    break
        return total


def common_letter_three(file):
    with open(file) as file:
        seen = set()
        shared = set()
        total = 0
        count = 1
        for line in file:
            if count == 1:
                for letter in line:
                    seen.add(letter)
            if count == 2:
                for letter in line:
                    if letter in seen:
                        shared.add(letter)
            if count == 3:
                for letter in line:
                    if letter in shared:
                        total += letter_to_number(letter)
                        seen.clear()
                        shared.clear()
                        count = 0
            count += 1
        return total


def letter_to_number(letter):
    letter = ord(letter)
    if letter >= 97 and letter <= 122:
        return letter - 96
    return letter - 38


print(common_letter_half("day3.txt"))
print(common_letter_three("day3.txt"))
