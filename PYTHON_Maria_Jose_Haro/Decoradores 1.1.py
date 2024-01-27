def decorador(funcion):
        def funcion_modificada():
                print ("Antes de llamar a la funcion")
                funcion()
                print("Despues de llamar a la funcion")
        return funcion_modificada
#def saludo():
#        print("Hola Dalto como andas")

#saludo_modificado = decorador(saludo)
#saludo_modificado()

@decorador
def saludo():
        print("Hola Dalto como esta")
saludo()














# decoradores property y para el seter utilizamos decorador atributo.seter- minuto 2:02
# un decorador es una funcion que decora a otra 
