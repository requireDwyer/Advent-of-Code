def fully_overlapping(file):
    with open(file) as file:
        overlapping = 0
        for line in file:
            line = line.removesuffix("\n").split(",")
            a, b = line[0].split("-")
            c, d = line[1].split("-")
            a, b, c, d, = (
                int(a),
                int(b),
                int(c),
                int(d),
            )
            if a <= c and b >= d:
                overlapping += 1
            elif a >= c and b <= d:
                overlapping += 1
        return overlapping


def overlapping(file):
    with open(file) as file:
        overlapping = 0
        for line in file:
            line = line.removesuffix("\n").split(",")
            a, b = line[0].split("-")
            c, d = line[1].split("-")
            a, b, c, d, = (
                int(a),
                int(b),
                int(c),
                int(d),
            )
            if not ((a < c and b < c) or (a > d and b > d)):
                overlapping += 1
        return overlapping


print(fully_overlapping("day4.txt"))

print(overlapping("day4.txt"))
