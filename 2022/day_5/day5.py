from collections import deque


def crate_mover_9000(file):
    with open(file) as file:
        stacks = {}
        condition = True
        while condition:
            line = file.readline()
            line = line.removesuffix("\n")
            for i, char in enumerate(line):
                if ord(char) >= ord("A") and ord(char) <= ord("Z"):
                    index = (i - 1) // 4 + 1
                    if index in stacks:
                        stacks[index].appendleft(char)
                    else:
                        stacks[index] = deque([char])
                elif char == "1":
                    condition = False
                    break
        for line in file:
            if line == "\n":
                continue
            line = line.removesuffix("\n")
            line_words = line.split(" ")
            amount, a, b = int(line_words[1]), int(line_words[3]), int(line_words[5])
            for i in range(amount):
                letter = stacks[a].pop()
                stacks[b].append(letter)
        output = []
        for i in range(1, len(stacks) + 1):
            output.append(stacks[i][-1])
        return "".join(output)


def crate_mover_9001(file):
    with open(file) as file:
        stacks = {}
        condition = True
        while condition:
            line = file.readline()
            line = line.removesuffix("\n")
            for i, char in enumerate(line):
                if ord(char) >= ord("A") and ord(char) <= ord("Z"):
                    index = (i - 1) // 4 + 1
                    if index in stacks:
                        stacks[index].appendleft(char)
                    else:
                        stacks[index] = deque([char])
                elif char == "1":
                    condition = False
                    break
        for line in file:
            if line == "\n":
                continue
            line = line.removesuffix("\n")
            line_words = line.split(" ")
            amount, a, b = int(line_words[1]), int(line_words[3]), int(line_words[5])
            temp_deque = deque([])
            for i in range(amount):
                letter = stacks[a].pop()
                temp_deque.append(letter)
            for i in range(amount):
                letter = temp_deque.pop()
                stacks[b].append(letter)
        output = []
        for i in range(1, len(stacks) + 1):
            output.append(stacks[i][-1])
        return "".join(output)


print(crate_mover_9000("sample.txt"))
print(crate_mover_9000("day5.txt"))

print(crate_mover_9001("sample.txt"))
print(crate_mover_9001("day5.txt"))
