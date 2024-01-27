class Animal:
    def sonido (self):
        pass

class Gato(Animal):
    def sonido (self):
        return "Miaun"
    
class Perro (Animal):
    def sonido (self):
        return "guau"
    
def hacer_sonido(animal):
    print (animal.sonido())
    
gato = Gato()
perro = Perro()

hacer_sonido(perro)
print (perro.sonido())




