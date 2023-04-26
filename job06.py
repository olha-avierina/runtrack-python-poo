class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
# For longueur

    def Getlongueur(self):
        return self.__longueur

    def Setlonguer(self, newlongueur):
        self.__longueur = newlongueur
# For Largeur

    def Getlargeur(self):
        return self.__largeur

    def Setlargeur(self, newlargeur):
        self.__largeur = newlargeur


R = Rectangle(10, 5)

print(R.Getlongueur())
R.Setlonguer(15)
print(R.Getlongueur())

print(R.Getlargeur())
R.Setlargeur(7)
print(R.Getlargeur())
