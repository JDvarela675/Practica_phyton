# -----------LOOPS-----------
#Otra forma de llamarlos y mayormente conocidos es bucle

#Bucle while:

value_1=0

#sintaxis de el while 

while value_1 <= 20:
    print(value_1)
    value_1+=2
    if(value_1==12): #rompe el ciclo por medio de un condicional
        print('se detiene el bucle')
        break

print('valor de value 1:',value_1)
print('------------------------------------')

lista_1=[ 35, 22, 43, 33, 21, 56, 44, 32, 67]

#for 
print('valores de ña listas:',lista_1)
for i in lista_1:
    print(i)

diccionario_1={'nombre':'juan','apellido':'perez','edad':25}

valor_1=0

print('contenido del diccionario:',diccionario_1)
for i in diccionario_1.values():
    print('valores del diccionario:',i)
    if i=='perez': # contidiconal dentro del bucle
        print('se detiene el bucle')
        break
else:
    print('a terminado el bucle')




