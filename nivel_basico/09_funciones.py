'''
--------Funciones--------

'''

#sintaxis para definir una función en phyton

def funcion_1(): #definimos la funcion
 #cuerpo de la funcion
    print('Hola dentro de la funcion :D')


#llamamos a la funcion
funcion_1()

def suma_numeros(numero_1,numero_2): #definimos la funcion con dos parametros
    resultado=numero_1+numero_2
    print('El resultado de la suma es :'+str(resultado))

# tener cuidado con el tipado debil de python
#ya que se pueden sumar tantos string como double o int
suma_numeros(5,6)
suma_numeros('5','6')
suma_numeros(5.5,6.5)


def area_circulo(radio): # definiciomos la funcion con un parametro
    pi=3.1416
    area=pi*radio**2
    print('El area del el triangulo es :'+str(area)+'cm^2')

area_circulo(4)

# retornar un valor en una funcion

def area_rectangulo(base,altura):
    area=base*altura
    return area

print('El area del rectangulo de la funcion es :'+str(area_rectangulo(12,2))+'cm^2')

#tambien lo puede almacernar en una variable
valor_1=area_rectangulo(12,2)
print('El area del rectangulo de la funcion es :'+str(valor_1)+'cm^2')

#funciones con strings

def nombre_completo(nombre,apellido):
    print(f'El nombre completo es :{nombre} {apellido}')

nombre_completo('Juan','Perez')

#funciones con valores default

def nombre_completo(nombre,apellido,segundo_nombre=''): #hay una variable default
    print(f'El nombre completo es :{nombre} {segundo_nombre} {apellido}')

nombre_completo('Juan','Perez',segundo_nombre='Carlos')

#ejercicio mas complejo

def buscar_numero_figonacci(numero):
    numero_fibonacci=0

    if numero==0:
        numero_fibonacci=0
    elif numero==1:
        umero_fibonacci=1
    else:
        numero_fibonacci=buscar_numero_figonacci(numero-1)+buscar_numero_figonacci(numero-2)



