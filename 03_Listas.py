##    Listas ##

#formas de declarar una lista

list_1=list()
list_2=[]
print('lista antes de tener elemetos:',len(list_1))

list_1=[56,78,54,12,34,23,45,23]

print('tamaño de lista con elementos: ',len(list_1))

#se le puede ingresar cualquier tipo de dato a la lista(dinamica) 

list_2=[21,1.79,'Josue','jd']

#los datos de na lista como en la mayoria de leguajes se enumeran 
#de 0 a n-1
#numeros positivos recorre la lista de izquiera a derecha 
#numeros negativos la recorre de derecha a izquierda

print('Lista numero dos:',list_2)
print("valor numero 2 de la lista: ",list_2[1])
print ("valor de la lista 3 pero al reves:",list_2[-2])
#resive un valor cualquiera y retorna la cantidad de elementos que hay en la lista de ese elemento

print(list_2.count(35))
print("En la lista numero uno se repite 23 esta cantidad de veces:",list_1.count(23))

#desempaquetar elementos de una lista en variables
#Para hacer esto se necesita una variable para cada elemeto
edad,altura,nombre,apodo =list_2

print("Nombre:",nombre)
print('Apodo:',apodo)

#funciones para usar en una lista :

#1) esta funcion agrega un valor al final de la lisa 

print('Lista antes de el agregado',list_2)
list_2.append("Ingenieria")
print('lista despues del agregado',list_2)

#2) esta funcion nos pide el incidice en donde queremos agregar un objeto y el objeto

list_2.insert(2,'verde')
print(list_2)

#3)Remove pide el objeto que desdea eliminar de la lista mientras este exista en la misma

list_2.remove('Ingenieria')
print(list_2)

#4) la funcion por defecto elimina el ultimo valor nada mas 
#este almacena el valor del indicie eliminado

print('lista antes:',list_1)

valor_eliminado=list_1.pop()
print(valor_eliminado)

print('despues',list_1)

#aunque uno tambien puede indciar el valor el cual quiere hacer pop

print(list_1.pop(2))
print(list_1)


#5)esta funcion vacia una lista por completo

copia_lista=list_1.copy()#retorna una copia de la lista 

list_1.clear()
print(list_1)
print(copia_lista)

#darle la vuelta los valores de una lista

copia_lista.reverse() # no olvidarse de los parentesis :x
print(copia_lista)

#6) el sort ordena predetrminadamente los valores de una lista de manera ascendete 
#sea alfabeticamente o numericamente

copia_lista.sort()
print(copia_lista)

