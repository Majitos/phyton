#una clase abstracta no podemmos instanciar pero es como una  plantilla 
from abc import ABC, abstractclassmethod
# un metodo abstracto esta declarado pero no tiene una implementacion 
class Persona(ABC):
    @abstractclassmethod
    def __init__ (self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractclassmethod
    def hacer_actividad (self):
        pass
    def presentarse (self):
        print (f"hola, me llamo: {self.nombre} y tengo {self.edad}años")

# esto es una plantilla que nos permite crear personas
        
class Estudiante(Persona):
    def __init__ (self, nombre, edad, sexo, actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f"estoy estudiando: {self.actividad}")

class TRabajador(Persona):
    def __init__(self,nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
    
    def hacer_actividad(self):
        print(f"Actualmente estoy trabajando en el rubro de: {self.actividad}")

pedrito = Estudiante("Pedrito",21,"masculino","programacion")
dalto = TRabajador("Lucas",21,"masculino","programacion")

dalto.presentarse()
dalto.hacer_actividad()
pedrito.presentarse()
pedrito.hacer_actividad()



