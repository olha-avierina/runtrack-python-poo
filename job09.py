class Student:
    def __init__(self, nome, prenome, numero, credit=0):
        self.nome = nome
        self.prenome = prenome
        self.numero = numero
        self.credit = credit
        self.level = self.studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.credit += credits
            self.level = self.studentEval()

    def studentEval(self):
        if self.credit >= 90:
            print("Exellant")
        elif self.credit >= 80:
            print("Trés bien")
        elif self.credit >= 70:
            print("Bien")
        elif self.credit >= 60:
            print("Passable")
        else:
            print("Insuffisant")

    def display_credit(self):
        print("Le nombre de credits de", self.prenome,
              "avec Identifiant", self.numero, "est", self.credit)

    def get_student_info(self):
        print(f"Nom : {self.nome}")
        print(f"Prénom : {self.prenome}")
        print(f"Identifiant : {self.numero}")


st = Student("Potter", "Harry", 1406, 60)
st.display_credit()
st.get_student_info()
