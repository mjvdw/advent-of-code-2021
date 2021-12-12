class Floor:
    def __init__(self, map):
        self.map = map
        self.max_height = len(self.map) - 1
        self.max_width = len(self.map[0]) - 1
        
    def is_lowest(self, x, y):
        adjacent = list(map(lambda x : int(x) ,self.get_adjacent(x, y)))
        value = int(self.value(x, y))

        if value < min(adjacent):
            return True
        else:
            return False


    def get_adjacent(self, x, y):
        adjacent = []

        # Get values above and below.
        # Check whether value is in top or bottom row, otherwise take values above and below.
        if y == 0:
            adjacent.append(self.map[y+1][x])
        elif y == self.max_height:
            adjacent.append(self.map[y-1][x])
        else:
            adjacent.append(self.map[y-1][x])
            adjacent.append(self.map[y+1][x])

        # Get values left and right.
        # Check whether value is far left or far right, otherwise take both left and right.
        if x == 0:
            adjacent.append(self.map[y][x+1])
        elif x == self.max_width:
            adjacent.append(self.map[y][x-1])
        else:
            adjacent.append(self.map[y][x-1])
            adjacent.append(self.map[y][x+1])

        return adjacent

    
    def value(self, x, y):
        value = int(self.map[y][x])
        return value


def get_floor_map_from_file():
    with open("puzzle-input.txt") as f:
        content = f.readlines()
        content = [line.strip("\n") for line in content]
        return content

def part_one():
    floor = Floor(get_floor_map_from_file())

    height = len(floor.map)
    width = len(floor.map[0])

    total_risk_level = 0

    for y in range(height):
        for x in range(width):
            if floor.is_lowest(x, y):
                total_risk_level = total_risk_level + 1 + floor.value(x, y)
    
    print("Answer", total_risk_level)


if __name__ == "__main__":
    part_one()