class Zoo:
    __animals = 0


    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []


    def add_animals(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1


    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name_of_zoo}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name_of_zoo}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name_of_zoo}: {', '.join(self.birds)}\n"

        result += f"Total animals: {Zoo.__animals}"
        return result

zoo_name = input()
zoo = Zoo(zoo_name)
number = int(input())

for x in range (number):
    command = input().split(" ")
    species = command[0]
    name = command[1]
    zoo.add_animals(species, name)

info = input()
print(zoo.get_info(info))