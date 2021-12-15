def get_content_from_file():
    with open("puzzle-input.txt") as f:
        content = f.readlines()
        grid = [x.strip("\n") for x in content]
        return grid


def part_one():
    grid = get_content_from_file()

    for line in grid:
        print(line)


if __name__ == "__main__":
    part_one()