# --- SETS  -----
#set es n tipo de dato en phyto de la clase set 
#formas de declarar un set
set_1=set()
set_2={} #esto inicialmente phyton lo interpreta como un diccionario

print(type(set_1))
print(type(set_2))


set_2={'Josue','Sandoval',21} #pero ahora lo esta tomando como un set 

print(type(set_2))

print(len(set_2))

set_2.add('JD')

print(set_2) #caracteristica 1 de los sets: no es una estructura ordenada 
#a diferencia de las listas y las tuplas estas lmacenan valores de manera desordenada

# SEGUNDA CARACTERISTICA DE LOS SETS : Estos no aceptan valores 
#repetidos
print(set_2)

#manera de comprobar que un elemento existe en un set 
print('JD' in set_2)
print('jd675' in set_2)

set_2.remove('JD')
print(set_2)

set_2.clear()
print(len(set_2))

''''
los sets nos pueden servir al momentos de que 
necesitemos una lista que no acepte repetido
 y no sea necesario tener un orden 

''' 

del set_2 # del es una operacon propia de phyton 

#al momento de usar del eliminamos la variable de nuestro promgrama 
#print(set_2) esto va a terminar dando un error ya que no esta definida

#concersion de la estrcutra de un set al de una lista 
set_1={'Josue','verde',21}

lista=list(set_1)

print(lista)
print(lista[0])


set_2={'C++','Java','Phyton','Dart'}

#unir sets 
set_unido=set_1.union(set_2)
print('Union de ambos sets',set_unido)