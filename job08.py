class Livre:
    def __init__(self, titre, auteur, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible

    def get_titre(self):
        return self.titre

    def get_auteur(self):
        return self.auteur

    def get_disponible(self):
        if self.disponible == True:
            print("Disponible")

    def verification(self):
        return True

    def emprunter(self):
        if self.disponible == False:
            print("Le livre", self.titre, "a ete emprunte")
        else:
            print("Desole le livre", self.titre, "n'est pas disponible")

    def rendre(self):
        if not self.disponible == True:
            print("Le livre", self.disponible, "a ete rendu")
        else:
            print("Error")


Li = Livre("Clone", "Anjey Joldac")
print("Titre", Li.get_titre())
print("Auteur", Li.get_auteur())
Li.get_disponible()
