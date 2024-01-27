class A:
    def hablar(self):
        print("Hola desde A")

class B(A):
    def hablar (self):
        print ("hola desde B")

class C(A):
    def hablar (self):
        print ("Hola desde C")

class D(B,C):
        def hablar (self):
             print ("Hola desde A")
d= D ()
C.hablar(d)

# la forma de ejecutar un metodo es llamandolo C.habla(d)