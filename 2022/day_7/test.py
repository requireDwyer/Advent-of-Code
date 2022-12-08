def part_one(file):
    with open(file) as file:
        path = []
        directories_total = {}
        for line in file:
            line = line.removesuffix("\n").split()

            # Find and update path
            is_cd_command = line[0] == "$" and line[1] == "cd"
            if is_cd_command:
                is_back = line[2] == ".."
                if is_back:
                    path.pop()
                else:
                    path.append(line[2])

            # Find lines with file size
            is_file_size = line[0] != "$" and line[0] != "dir"
            if is_file_size:
                file_size = int(line[0])
                # add file size to all directories in path
                for i in range(1, len(path) + 1):
                    directories_total["/".join(path[:i])] = (
                        directories_total.get("/".join(path[:i]), 0) + file_size
                    )

        # Sum directories with files size under 100,000
        total = 0
        for size in directories_total.values():
            if size <= 100000:
                total += size
        return total


def part_two(file):
    with open(file) as file:
        path = []
        directories_total = {}
        for line in file:
            line = line.removesuffix("\n").split()

            # Find and update path
            is_cd_command = line[0] == "$" and line[1] == "cd"
            if is_cd_command:
                is_back = line[2] == ".."
                if is_back:
                    path.pop()
                else:
                    path.append(line[2])

            # Find lines with file size
            is_file_size = line[0] != "$" and line[0] != "dir"
            if is_file_size:
                file_size = int(line[0])
                # add file size to all directories in path
                for i in range(1, len(path) + 1):
                    directories_total["/".join(path[:i])] = (
                        directories_total.get("/".join(path[:i]), 0) + file_size
                    )

        space = directories_total["/"] - 40000000
        best = float("inf")
        for size in directories_total.values():
            if size >= space:
                best = min(best, size)
        return best


print(part_one("day7.txt"))

print(part_two("day7.txt"))
