class Persona:
    def __init__(self,nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar (self):
        print("hola, estoy hablando un poco")

class Empleado (Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        self.notas = notas
        self.universidad = universidad 

class PersonaNormal (Empleado, Estudiante):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad, autodenominacion):
        self.notasautodenominacion = autodenominacion
    
roberto = Empleado("Roberto",43,"argentino","programador",10000)
roberto.hablar()
