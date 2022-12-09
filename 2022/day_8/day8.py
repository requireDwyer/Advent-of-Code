def is_visible(trees, i, j):
    current = trees[i][j]
    seen = 0
    # up
    vertical = i - 1
    while vertical >= 0:
        if current <= trees[vertical][j]:
            seen += 1
            break
        vertical -= 1
    # down
    vertical = i + 1
    while vertical < len(trees):
        if current <= trees[vertical][j]:
            seen += 1
            break
        vertical += 1
    # left
    horizontal = j - 1
    while horizontal >= 0:
        if current <= trees[i][horizontal]:
            seen += 1
            break
        horizontal -= 1
    # right
    horizontal = j + 1
    while horizontal < len(trees[i]):
        if current <= trees[i][horizontal]:
            seen += 1
            break
        horizontal += 1
    if seen == 4:
        return 0
    return 1


def part_one(file):
    with open(file) as file:
        trees = []
        for line in file:
            line = [int(x) for x in list(line.removesuffix("\n"))]
            trees.append(line)
        total_trees = len(trees) * 2
        total_trees += (len(trees[0]) - 2) * 2
        for i in range(1, len(trees) - 1):
            for j in range(1, len(trees[i]) - 1):
                total_trees += is_visible(trees, i, j)
        return total_trees


def scenic_score(trees, i, j):
    current = trees[i][j]
    # up
    score = 1
    count = 0
    vertical = i - 1
    while vertical >= 0:
        if current <= trees[vertical][j]:
            count += 1
            break
        count += 1
        vertical -= 1
    score *= count
    count = 0
    # down
    vertical = i + 1
    while vertical < len(trees):
        if current <= trees[vertical][j]:
            count += 1
            break
        count += 1
        vertical += 1
    score *= count
    count = 0
    # left
    horizontal = j - 1
    while horizontal >= 0:
        if current <= trees[i][horizontal]:
            count += 1
            break
        count += 1
        horizontal -= 1
    score *= count
    count = 0
    # right
    horizontal = j + 1
    while horizontal < len(trees[i]):
        if current <= trees[i][horizontal]:
            count += 1
            break
        count += 1
        horizontal += 1
    score *= count
    return score


def part_two(file):
    with open(file) as file:
        trees = []
        for line in file:
            line = [int(x) for x in list(line.removesuffix("\n"))]
            trees.append(line)
        maximum = float("-inf")
        for i in range(1, len(trees) - 1):
            for j in range(1, len(trees[i]) - 1):
                maximum = max(scenic_score(trees, i, j), maximum)
        return maximum


print(part_one("sample.txt"))
print(part_one("day8.txt"))

print(part_two("sample.txt"))
print(part_two("day8.txt"))
