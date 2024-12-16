#Varibles

my_variable_string= 'My string Variable :)'
print('Variable con valor string:',my_variable_string)

my_variable_int=10
print('Misma variable pero con valor entero:',my_variable_int)

my_variable_bool=False
print('Misma variable pero valor booleano:',my_variable_bool)

print(type(my_variable_bool))
print('este es el valor de :',False)

# transformando variable a un string con la funcion str
my_variable_to_string=str(my_variable_bool)
print(type(my_variable_to_string))

#funcion len sirve para medir el tamaño de un string
print(len(my_variable_to_string))

#Obtener datos (inputs):

nombre_completo=input("Digita tu nombre completo:")
ingresa_edad=input('cual es tu edad?:')

print('Nombre:',nombre_completo)
print('edad:',ingresa_edad)

# ¿Forzar el tipado de las variables?

adress :str = 'mi direccion'
adress=22

print(type(adress))


