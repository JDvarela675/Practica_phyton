# ----Operadores Logicos------

#concatenador
print('Hola'+'phyton')

print(3 != 4)

print('Hola'>='Bola') #verifica una ordenacion aflabetico EJEMPLO : A<B



##    STRINGS ##

str_1='Murcielago'

#operador length : este adiferencia de los demas va de 1 asta n

print('longitud de string 1:',len(str_1))

nombre,username,edad= 'josue','jd',35
#para parsear strings en phyton hay varias maneras ejemplo el punto format
#format() sirve para formatear datos y sustituir cadenas complejas ejemplo:.
print('Hola, mi nombre es: {} pero me llaman {} y mi edad es {}'.format(nombre,username,edad))

#o otra manera de hacerlo es de la siguiente forma:
print('hola mi nombre es %s pero me llaman %s y mi edad es %d' %(nombre,username,edad))

#NO Hacer
# print('Hola mi nombre es: '+nombre+'pero me llaman: '+username+' y mi edad es '+str(edad))


#Funciones de un string

lenguaje='flutter'

 #voltear el texto
lenguajes_reves=lenguaje[::-1]
print('texto al reves:',lenguajes_reves)

#hace que el primer caracter tenga letra mayuscula y las otras minuscula
print('Primera letramayuscula:',lenguaje.capitalize())

#pone todo el texto en mayusculas
print('Poner en mayusculas :',lenguaje.upper())

# ahora todo pero en minusculas
print('Poner en minusculas:',lenguaje.lower())

#cuenta cuantas letras hay en el arreglo de string
print('en el string hay estas cantidad de t: ',lenguaje.count('t'))

#ver si un string es numerico el valor es booleano

print('es numerico?',lenguaje.isnumeric())

#verificar si una cadena esta escrita en mayusculas
print('el texto esta en mayusculas: ?',lenguaje.isupper())




