class Persona:
    def __init__(self,nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hola Estoy Hablando")
    
class Empleado (Persona):
    pass
roberto = Persona ("Roberto",43,"argentino")

roberto.hablar()
print (roberto.nombre)
print (roberto.edad)
print (roberto.nacionalidad)