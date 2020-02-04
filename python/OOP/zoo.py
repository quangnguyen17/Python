
# Assignment: Zoo


class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self, name):
        self.animals.append(Lion(name))

    def add_tiger(self, name):
        self.animals.append(Tiger(name))

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()


class Animal:
    def __init__(self, name, age, health_level, happiness_level):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def feed(self, health_increment=10, happiness_increment=10):
        self.health_level += health_increment
        self.happiness_level += happiness_increment

    def display_info(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Happiness Level: " + str(self.happiness_level))


class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name, 0, 0, 0)
        self.habitats = ["Open grasslands", "Savannas", "Rainforests", "..."]

    def display_info(self):
        super().display_info()
        print("Habitats: " + str(self.habitats))


class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, 0, 0, 0)
        self.habitats = ["Open Grasslands", "Savanna", "Shrubland", "..."]

    def display_info(self):
        super().display_info()
        print("Habitats: " + str(self.habitats))


class Bear(Animal):
    def __init__(self, name):
        super().__init__(name, 0, 0, 0)
        self.habitats = ["Deserts", "Forests", "..."]

    def display_info(self):
        super().display_info()
        print("Habitats: " + str(self.habitats))


zoo1 = Zoo("John's Zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()
