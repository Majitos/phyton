class Persona:
    def __init__(self,nombre,edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

dalto = Persona("lucas",21) 
nombre = dalto.get_nombe()
print(nombre)

# uso del un getter
