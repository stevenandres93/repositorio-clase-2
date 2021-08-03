class Persona:
    def __init__(self, edad, estatura, sexo, peso, color):
        self.edad = edad
        self.estatura = estatura
        self.sexo = sexo
        self.peso = peso
        self.color = color

    def crecer(self):
        self.estatura = self.estatura + 1

    def envejecer(self):
        self.edad = self.edad + 1


persona_1 = Persona(22, 180, "hombre", 80, "negro")
persona_2 = Persona(18, 150, "mujer", 60, "blanco")
persona_3 = Persona(35, 172, "indef", 180, "rojo")

print(persona_2.edad)
persona_2.envejecer()
print(persona_2.edad)