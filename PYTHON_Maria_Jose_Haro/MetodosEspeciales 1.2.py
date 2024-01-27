# init es un metodo especial que no se puede redefinir
class Persona:
    
    # es un metodo constructor __init__
    def __init__ (self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    # devuelve una representacion del objeto en una cadena de texto
    def __str__ (self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    
     # este metodo actua como la representacion de 
    def __repr__ (self):
        return f'Persona("{self.nombre}", {self.edad})'

    
dalto = Persona("lucas",21)

repre = repr(dalto)
resultado = eval (repre)
print (resultado.edad)