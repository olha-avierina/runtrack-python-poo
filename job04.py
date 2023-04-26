class Person:
    def __init__(self, nome, prenome):
        self.nome = nome
        self.prenom = prenome

    def SePresenter(self):
        return f"Je suis {self.nome}, {self.prenom}"


person1 = Person("Dupont", "Pierre")
print(person1.SePresenter())

person2 = Person("Delpesh", "Bruno")
print(person2.SePresenter())
