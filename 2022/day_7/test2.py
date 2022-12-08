def part_one(file):
    with open(file) as file:
        for line in file:
            line = line.removesuffix("\n")
            print(line)


print(part_one("sample.txt"))

thing = {10: 15}
thing[5] = thing.get(11, 10)
print(thing)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1, len(array) + 1):
    print(array[:i])
