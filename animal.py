class Animal:
    def __init__(self, name, atomic_weight, group, period, density,
                 melting_point):
        self.name = name
        self.atomic_weight = atomic_weight
        self.group = group
        self.period = period
        self.density = density
        self.melting_point = melting_point
        self.options = [
            "atomic_weight", "group", "period", "density", "melting_point"
        ]

    def talk(self):
        print(self.name)
        print("atomic_weight:", self.atomic_weight, "feet")
        print("group:", self.group, "pounds")
        print("period:", self.period, "mph")
        print("density:", self.density, "years")
        print("melting_point:", self.melting_point)
        print("")


Hydrogen = Animal("Hydrogen", 1, 1, 1, 0, 14)
Helium = Animal("Helium", 4, 18, 1, 0, 0)
Lithium = Animal("Lithium", 7, 1, 2, 1, 454)
Beryllium = Animal("Beryllium", 9, 2, 2, 2, 1560)

Boron = Animal("Boron", 11, 13, 2, 2, 2349)
Carbon = Animal("Carbon", 12, 14, 2, 2, 400)
Nitrogen = Animal("Nitrogen", 14, 15, 2, 0, 63)

Hydrogen = Animal("Hydrogen", 1, 1, 1, 0, 14)
Hydrogen = Animal("Hydrogen", 1, 1, 1, 0, 14)
Hydrogen = Animal("Hydrogen", 1, 1, 1, 0, 14)
Hydrogen = Animal("Hydrogen", 1, 1, 1, 0, 14)
Hydrogen = Animal("Hydrogen", 1, 1, 1, 0, 14)
Hydrogen = Animal("Hydrogen", 1, 1, 1, 0, 14)
Hydrogen = Animal("Hydrogen", 1, 1, 1, 0, 14)
Hydrogen = Animal("Hydrogen", 1, 1, 1, 0, 14)
Hydrogen = Animal("Hydrogen", 1, 1, 1, 0, 14)
Hydrogen = Animal("Hydrogen", 1, 1, 1, 0, 14)
Hydrogen = Animal("Hydrogen", 1, 1, 1, 0, 14)
Hydrogen = Animal("Hydrogen", 1, 1, 1, 0, 14)
Hydrogen = Animal("Hydrogen", 1, 1, 1, 0, 14)
Hydrogen = Animal("Hydrogen", 1, 1, 1, 0, 14)

animals = [
    Hydrogen,
    Helium,
    Lithium,
    Beryllium,
    Boron,
    Carbon,
    Nitrogen,
]
