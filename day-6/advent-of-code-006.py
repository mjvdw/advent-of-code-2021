
class Fish:
    def __init__(self, spawn_state):
        self.spawn_state = spawn_state


def get_fish_data_from_file():
    with open('puzzle-input.txt') as f:
        content = f.readlines()[0].split(",")
        content = list(map(lambda x: int(x), content))
        fish = [Fish(spawn_state) for spawn_state in content]
        return fish


def part_one():
    fish = get_fish_data_from_file()
    print(fish)

if __name__ == "__main__":
    part_one()