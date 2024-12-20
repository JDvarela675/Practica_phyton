#  ------Tuples -----
# es una colección ordenada e inmutable 
# de elementos del mismo o diferente tipo. 

#maneras de definir una tupla
tupla_1=tuple()
tupla_2=()

tupla_1=(21,1.79,'Josue','Sandoval',21)
tupla_2=(45,1.81,'Jose','Varela',18)

print(tupla_1)
print(type(tupla_1))

print(tupla_1[0])
print(tupla_1[-2])


"""""
Error de index en la tupla
print(tupla_1[4])
print(tupla_1[-6])

"""

#operaciones en una tupla

print("veces que esta el valor 21 en la tupla:",tupla_1.count(21))

# en index se queda con el primer valor encontrado en la tupla  
print('Josue esta en la posicion:',tupla_1.index('Josue'))

#la tupla es inmutable todos los valorees son constantes 
#tupla_1[1]=1.82

suma_tuplas=tupla_1+tupla_2
print('sumade las dos tuplas:',suma_tuplas)

print('elementos de la tupla del 3 a 6: ',suma_tuplas[3:6])
