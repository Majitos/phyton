class MiClase:
    def __init__(self):
        self.__atributo_privado = "valor"

    def __hablar(self):
        print("hola como estas")

objeto = MiClase()
print (objeto.__atributo_privado())
print (objeto.__hablar())

# cuando un atributo es privado se coloca un guion bajo y si es muy privado se colocan 2 guiones, el encapsulamiento protege atributos privados
# getter obtenerdor o acceder setter definidor o establecer
# el encapsulamiento protege los atributos, mejora la legibilidad el mantenimiento y la evolucion
# muy privado es privado de otro lenguaje privado es protegido y publio es publico
# 

