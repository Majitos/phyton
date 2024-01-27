class Estudiante:
    def __init__(self,nombre, edad, grado):
        self.nombre= nombre
        self.edad= edad
        self.grado= grado
    def estudiar(self):
        print ("Estudiando.........")
nombre = input("Escriba su nombre ")
edad = input("Que edad tiene: ")
grado = input("En que grado esta: ")

estudiante = Estudiante(nombre,edad,grado)

print (f"""Datos del estudiante: \n\n
       Nombre:  {estudiante.nombre} \n 
       Edad: {estudiante.edad} \n
       Grado: {estudiante.grado} \n
       """)
while True:

    estudiar = input ()
    if (estudiar.lower () == "estudiar"):
        estudiante.estudiar()

