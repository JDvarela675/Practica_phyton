import threading

def hilo1(): # definiendo una funcion que imprime el alfabeto
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letra in alfabeto:
        print(letra)


def hilo2(): # definiendo una funcion que imprime los numeros del 0 al 9
   contador=0
   while contador<10:
       print(contador)
       contador+=1


d1 = threading.Thread(target=hilo1, args=()) #creando un hilo
d2 = threading.Thread(target=hilo1, args=())
d3 = threading.Thread(target=hilo1, args=())
d4 = threading.Thread(target=hilo2,args=())
d5 = threading.Thread(target=hilo2,args=())
d6 = threading.Thread(target=hilo2,args=())

print("Iniciando hilos")
d1.start()
d2.start()
d3.start()
d4.start()
d5.start()
d6.start()
