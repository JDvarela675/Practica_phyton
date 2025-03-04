#--------------------------Clases--------------------------
# Las clases son una forma de organizar y estructurar el código en Python.

#ejemplos de clases 

class Perro:
    def nombre(self, nombre): #self es una referencia a la instancia de la clase
        self.nombre = nombre

    def ladrar(self):
        print(f'{self.nombre} dice guau guau :3')

    

#instanciar una clase

perro1=Perro()
perro1.nombre('Firulais')
perro1.ladrar()

#otro ejemplo mas complejo
# para este ejemplo usaremos personajes de Jojo's Bizarre Adventure

class Personaje:
    def personaje(self,nombre,stand,parte):
        self.nombre = nombre
        self.stand = stand
        self.parte = parte
    
    def presentacion(self):
        print(f'soy {self.nombre} y soy un usario de stand')
        print(f'mi stand es {self.stand}')
    

joseph=Personaje()
joseph.personaje('Joseph Joestar','Hermit Purple','Stardust Crusaders')
joseph.presentacion()

gappy=Personaje()
gappy.personaje('Josuke Higashikata','Soft & Wet','JoJolion')
gappy.presentacion()

#--------------------------Herencia--------------------------
# La herencia es una forma de crear una nueva clase usando clases existentes.
# La nueva clase se llama clase derivada o subclase.

#ejemplo de herencia

class Animal:
    def animal(self, nombre):
        self.nombre = nombre

    def sonido(self):
        print('sonido de animal')

#la sintaxis la cual se usa para heredar una clase es la siguiente
#class NuevaClase(ClasePadre):
#ejemplo:
class Perro(Animal):
    def animal(self, nombre):
        return super().animal(nombre) 
    def sonido(self,):
        print('guau guau')


firulais=Perro()
firulais.animal('Firulais')
firulais.sonido()