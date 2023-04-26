class Livre:
    def __init__(self, titre, auteur, nombre):
        self.titre = titre
        self.auteur = auteur
        self.nombre = nombre

    def get_titre(self):
        return self.titre

    def set_titre(self, newtitre):
        self.titre = newtitre

    def get_auteur(self):
        return self.auteur

    def set_auteur(self, newauteur):
        self.auteur = newauteur

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, newnombre):
        self.nombre = newnombre
        if self.nombre < 0 or self.nombre == 0:
            print("Error: nombre is not valide")
        else:
            print("page", self.nombre)


Li = Livre("Clone", "Anjey Joldac", 10)
print("Titre", Li.get_titre())
print("Auteur", Li.get_auteur())
# print("Pages", Li.get_nombre())

Li.set_nombre(16)
