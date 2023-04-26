class Voiture:
    def __init__(self, marque, modele, anee, kilométrage, en_marche=True, reservoir=50):
        self.marque = marque
        self.modele = modele
        self.anee = anee
        self.kilométrage = kilométrage
        self.en_marche = en_marche
        self.reservoir = reservoir

    def get_marque(self):
        return self._marque

    def set_marque(self, marque):
        self._marque = marque

    def get_modele(self):
        return self._modele

    def set_modele(self, modele):
        self._modele = modele

    def get_annee(self):
        return self._annee

    def set_annee(self, annee):
        self._annee = annee

    def get_kilométrage(self):
        return self.kilométrage

    def set_kilométrage(self, kilométrage):
        self.kilométrage = kilométrage

    def get_en_marche(self):
        return self.en_marche

    def demarrer(self):
        if self.verifier_plein():
            self.en_marche = True
            print("La voiture demarre")
        else:
            print("le reservoir est presque vide")

    def arreter(self):
        self.en_marche = False
        print("la voiture s'arrete")

    def verifier_plein(self):
        return self.reservoir > 5


vo = Voiture("BMW", "Grand turismo", 2017, 300,)
vo.demarrer()
