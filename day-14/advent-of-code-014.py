class Polymer():
    def __init__(self, polymer_string, pairs):
        self.polymer_string = polymer_string
        self.pairs = pairs

    def run_pair_insertion(self):
        insertion_values = []

        for i in range(len(self.polymer_string)-1):
            pair = self.polymer_string[i] + self.polymer_string[i+1]
            insertion_value = self.pairs[pair]
            insertion_values.append(insertion_value)

        new_polymer_list = list(zip(self.polymer_string, insertion_values))
        new_polymer_str = ""

        for element_pair in new_polymer_list:
            for element in element_pair:
                new_polymer_str += element
        
        self.polymer_string = new_polymer_str + self.polymer_string[-1]

    def count_all_element_occurrences(self):
        unique = list(set(self.polymer_string))
        count_dict = dict.fromkeys(unique, 0)
        
        for element in unique:
            count_dict[element] = self.polymer_string.count(element)

        return count_dict

    @property
    def most_common_element(self):
        occurrences = self.count_all_element_occurrences()
        most_common_element = max(occurrences, key=occurrences.get)
        return most_common_element

    @property
    def least_common_element(self):
        occurrences = self.count_all_element_occurrences()
        most_common_element = min(occurrences, key=occurrences.get)
        return most_common_element

    def get_element_occurrences(self, element):
        return self.polymer_string.count(element)


def get_content_from_file():
    with open("puzzle-input.txt") as f:
        content = f.readlines()
        
        template = content.pop(0).strip("\n")
        
        content.pop(0)  # Removing new line.
        pair_keys = []
        pair_values = []

        for pair in content:
            key_value = pair.strip("\n").split(" -> ")
            pair_keys.append(key_value[0])
            pair_values.append(key_value[1])

        pairs = dict(zip(pair_keys,pair_values))

        return template, pairs


def part_one():
    template, pairs = get_content_from_file()
    polymer = Polymer(template, pairs)

    i = 0
    while i < 10:
        polymer.run_pair_insertion()
        i += 1

    most_common_count = polymer.get_element_occurrences(polymer.most_common_element)
    least_common_count = polymer.get_element_occurrences(polymer.least_common_element)

    print("Answer", most_common_count - least_common_count)


if __name__ == "__main__":
    part_one()