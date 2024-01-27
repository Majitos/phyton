# decorador deleter

class Persona:
    # constructor
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self._edad = edad

    # acceder a su valor
    @property
    def nombre(self):
        return self.__nombre
    # poder modificar
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre

dalto = Persona("Lucas",21)

nombre = dalto.nombre
print(nombre)

dalto.nombre = "majo"

nombre = dalto.nombre
print (nombre)

del dalto.nombre

print ("Ese es un ejempplo de mi clase de programacion ")