
# Assignment: Zoo


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
        print("Age: " + self.age)
        print("Happiness Level: " + self.happiness_level)


class Tiger(Animal):
    def __init__(self):
        super()


class Tiger(Animal):
    def __init__(self):
        super()


class Tiger(Animal):
    def __init__(self):
        super()
