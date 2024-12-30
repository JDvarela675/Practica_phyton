'''
--------------------Dicionarios--------------------

'''

# Un diccionario tiene una estructura de clave:valor
# como los hashmaps en java

#crear un diccionario
diccionario_1 = dict()
diccionario_2 = {}

print(type(diccionario_1))

#agregar elementos a un diccionario
#OJO: por el tipado devil de phyton, se pueden agregar claves con diferente valor o dynamicas
diccionario_2 = {'nombre':'jhonny joestar','Edad':19,'stand':'tusk','caracteristicas':'Protagonista'}
print(diccionario_2)

diccionario_1= {'nombre':'gyro zeppeli','Edad':20,'stand':'ball breaker','caracteristicas':
                {'Rubio','Ojos verdes','traje de vaquero','protagonista','dientes de oro'}}

ducionario_3={'nombre:':'diego brando', 'Edad':20, 'stand':'scary monsters','caracteristicas':
                {'rubio','ojos azules','traje de vaquero','antagonista','dientes de oro'}}

print(diccionario_1)
print(diccionario_2)

#medir el tamaño de un diccionario
print(len(diccionario_2))
print(len(diccionario_1['caracteristicas']))
#Acceder a un elemento de un diccionario
print(diccionario_2['nombre'])

#para buscar und ato dentro de un diccionario phyton busca por la clave
#si no existe la clave, phyton retornara un false
print('jhonny joestar' in diccionario_2)
print('nombre' in diccionario_2)

#metodos de los diccionarios
#items() retorna una lista de tuplas con la clave y el valor
print(diccionario_2.items())

#keys() retorna una lista con las claves de el diccionario
print(diccionario_2.keys())

#values() retorna una lista con los valores de el diccionario
print(diccionario_2.values())

#fromkeys() retorna un diccionario con las claves y valores que le pasemos
diccionario_3 = dict.fromkeys(diccionario_2, 'valor')


#Trabsformar un diccionario en una lista,tupla o set
#list()
print(list(diccionario_2))

#tuple()
print(tuple(diccionario_2))

#set()
print(set(diccionario_2))
