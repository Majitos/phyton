from typing import Self


class celular:
    def __init__ (self, marca, modelo, camara):

        self.modelo = modelo 
        self.camara = camara
        self.marca = marca 
    def llamar (self):
        print(f'Estas haciendo un llamado desde un: {self.modelo}')
    def cortar (self):
        print(f'Cortaste la llamada desde tu: {self.modelo}')

celular1 = celular("Samsung","S23","48 MP")
celular2 = celular("Apple","Iphone 15 pro","12 MP")

celular1.cortar ()
celular2.llamar ()