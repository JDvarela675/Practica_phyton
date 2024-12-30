# -------Condicionales-------

condicional_1= False

if condicional_1: #si la condicion es verdadera
    print('La condicion 1 es verdadera')


print('La condicion 1 es falsa')

# con numeros

condicional_2= 1

if condicional_2>=25:
    print('La condicion 2 es mayor o igual a 25')

else:
    print('La condicion 2 es menor a 25')


print('el programa sigue')

#con operadores logicos

condicional_3= 24
condicional_4= 9

if condicional_3>20 and condicional_4>10:
    print('Ambas condiciones son verdaderas')

else:
    print('Alguna de las condiciones es falsa')



#el else if en phyton es elif

if condicional_2 > 20 and condicional_2< 30:
    print('se cumple la primera condicion ')
elif condicional_2>30: #recordar que tiene que ir en el mismo espacio de tabulacion si no no copilara 
    print('se cumplio el segundo condicional ')
elif condicional_2 ==1:
    print('se cumplio el tercer condicional ')
else:
    print('no se cumplio ninguna condicion')


#condicionales con string 

condicional_string='Hola Mundo'



if len(condicional_string) == 0 :
    print('el string esta vacio')
elif condicional_string.lower()=='hola mundo':
    print('el string es igual a hola mundo')
else:
    print('el string condicional tiene el valor de:',condicional_string)