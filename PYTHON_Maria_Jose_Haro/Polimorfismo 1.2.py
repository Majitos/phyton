class Gato():
    def sonido (self):
        return "Miaun"
    
class Perro ():
    def sonido (self):
        return "guau"
    
def hacer_sonido(animal):
    print (animal.sonido())
    
gato = Gato()
perro = Perro()

hacer_sonido(perro)
print (perro.sonido())


# el mismo metodo funciona para ambos objetos 