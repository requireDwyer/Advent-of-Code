# I could make this much better, but o_o
def signal(file):
    with open(file) as file:
        line = file.readline()
        for i in range(len(line) - 3):
            unique = set()
            is_unique = True

            for j in range(i, i + 4):
                char = line[j]
                if char in unique:
                    is_unique = False
                    continue
                else:
                    unique.add(char)

            if not is_unique:
                continue

            return i + 4


def message(file):
    with open(file) as file:
        line = file.readline()
        for i in range(len(line) - 13):
            unique = set()
            is_unique = True

            for j in range(i, i + 14):
                char = line[j]
                if char in unique:
                    is_unique = False
                    continue
                else:
                    unique.add(char)

            if not is_unique:
                continue

            return i + 14


print(signal("sample.txt"))
print(signal("day6.txt"))

print(message("sample.txt"))
print(message("day6.txt"))
