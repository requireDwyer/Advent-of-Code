def small_files(file):
    with open(file) as file:
        directories = {}
        path = []
        for line in file:
            line = line.removesuffix("\n")
            if line[0] == "$" and line[2] == "c" and line[5] != ".":
                current_directory = line.split(" ")[2]
                path.append(current_directory)
                if current_directory not in directories:
                    directories[current_directory] = 0
            elif line[0] == "$" and line[2] == "c":
                path.pop()
            elif ord(line[0]) >= ord("0") and ord(line[0]) <= ord("9"):
                for directory in path:
                    directories[directory] += int(line.split(" ")[0])

        total = 0
        for amount in directories.values():
            if amount <= 100000:
                total += amount
        print(directories)
        return total


# print(small_files("sample.txt"))
# print("=====================")
print(small_files("day7.txt"))
# print(small_files("day7test.txt"))
# print(1581595 - 1324537)
