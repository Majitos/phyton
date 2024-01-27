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
print (D.mro())

# con D.mro () se puede ver el orden con el que se va a llamar un metodo