import threading 
from random import randint #para generar numeros aleatorios
#semaforos

#ejercicios hay 10 niños y 3 pedazos de pastel
#los niños solo pueden comer si hay pasteL; hacer un programe que simule esto

num_niños = 10
num_pastel = 3

# creamos una semaforo con un isntancia de threading.Semaphore

semaforo1= threading.Semaphore(1)

#creamos una funcion para definir el comportamiento de los niños
def ninio(n):
    global num_pastel

    for i in range(1,3): #cada niño intenta comer 3 veces
        semaforo1.acquire() # poner en cola a los niños que viene llegando

        if num_pastel <= 0:
          print("Niño", n, "no hay pastel")
        else:
            print("Niño", n, "comiendo pastel")
            num_pastel -= 1
    
        semaforo1.release() #liberar el semaforo



