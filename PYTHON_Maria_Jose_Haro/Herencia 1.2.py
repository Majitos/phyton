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
    def hablar(self):
        print("NO")

        roberto = Empleado("Roberto",43,"argentino","programador",100000)
        roberto.hablar()
