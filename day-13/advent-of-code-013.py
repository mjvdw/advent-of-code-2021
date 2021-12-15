class Instruction:
    def __init__(self, direction, coord):
        self.direction = direction
        self.coord = coord


class Grid:
    def __init__(self, coords):
        self.coords = coords
        self.grid = self.generate_grid_from_coords(self.coords)

    def generate_grid_from_coords(self, coords):
        pass

    # List of lists to represent the grid itself - go with True or False instead of # and .

    # Def to fold grid at line, either x or y (optional arguments?)


def get_content_from_file():
    with open("puzzle-input.txt") as f:
        content = f.readlines()
        content = [x.strip("\n") for x in content]

        split_index = content.index("")

        coords_raw = content[:split_index]
        coords = [[int(x.split(",")[0]),int(x.split(",")[1])] for x in coords_raw]
        grid = Grid(coords)

        instructions_raw = content[split_index:]
        instructions_raw.pop(0)
        instructions = []
        for i in instructions_raw:
            print(i)

        return grid, instructions


def part_one():
    grid, instructions = get_content_from_file()


if __name__ == "__main__":
    part_one()