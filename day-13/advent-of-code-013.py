class Instruction:
    def __init__(self, direction, coord):
        self.direction = direction
        self.coord = coord


class Grid:
    def __init__(self, coords):
        self.coords = coords
        self.grid = self.generate_grid_from_coords(self.coords)

    def generate_grid_from_coords(self, coords):
        height = []
        width = []
        
        for coord in coords:
            height.append(coord[0])
            width.append(coord[1])

        max_height = max(height)
        max_width = max(width)

        grid = []
        row = [False] * (max_width + 1)
        for i in range(max_height + 1):
            grid.append(row.copy())

        for coord in coords:
            grid[coord[0]][coord[1]] = True

        return grid

    def fold(self, instruction):
        pass


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
            i = i.strip("fold along ")
            direction = i[0]
            coord = int(i.split("=")[1])
            instructions.append(Instruction(direction, coord))

        return grid, instructions


def part_one():
    grid, instructions = get_content_from_file()

    print(grid.grid)

    for instruction in instructions:
        grid.fold(instruction)
        break    # Break after first iteration just for part one


if __name__ == "__main__":
    part_one()