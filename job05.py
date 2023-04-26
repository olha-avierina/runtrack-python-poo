class Animal:
    def __init__(self, age, prenom):
        self.age = age
        self.prenom = prenom

    def vieillir(self):
        self.age += 1
        return self.age

    def nommer(self):
        return self.prenom


an = Animal(4, "Luna")
print("L`age de l`animale", 0)
print("L`age de l`animale", an.vieillir())
print("L`animal se nomme", an.nommer())
