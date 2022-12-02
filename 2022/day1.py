# Time: O(n)
# Space: O(1)
def max_elf_calories(file):
    with open(file) as file:
        current = 0
        max_calories = 0
        for line in file:
            if line != "\n":
                current += int(line)
            else:
                if current > max_calories:
                    max_calories = current
                current = 0
    return max_calories


# Time: O(n)
# Space: O(1)
def top_3_elf_calories_sum(file):
    with open(file) as file:
        current = 0
        first = 0
        second = 0
        third = 0
        for line in file:
            if line != "\n":
                current += int(line)
            else:
                if current > first:
                    third = second
                    second = first
                    first = current
                elif current > second:
                    third = second
                    second = current
                elif current > third:
                    third = current
                current = 0
        return first + second + third


print(max_elf_calories("./day1.txt"))
print(top_3_elf_calories_sum("./day1.txt"))
