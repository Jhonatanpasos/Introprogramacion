#--------------------------------Ejercicios condicionales---------------------------------#
#1. Dados dos numeros, determine si son iguales o cual es el mayor
#2. Pida la edad del usuario y muestre en pantalla la siguiente información:
#       - Si tiene menos de 18 años diga que es menor de edad
#       - Desde 18 hasta 25 es joven 
#       - Desde 26 hasta 60 es adulto
#       - Mayor a 60 es adulto mayor
#3. Escriba un programa que pida el año actual y un año cualquiera, y que escriba cuantos 
#   años han pasado desde ese año, o cuantos años falta para llegar a ese año
#4. Escriba un programa que pida una distancia en cm y escriba esa distancia en km, m y cm

#Ejercicio 1
print ("#"*20, "Determinemos relaciones entre numeros", "#"*20)
#-----Constantes------
Bienvenida = "¡Bienvenido! vamos a determinar la relación entre dos nuemros"
Pregunta_A = "Ingrese un numero"
Pregunta_B = "Ingrese otro numero"
MensajeMayor = "El numero {} es mayor que el numero {}, ya que {} > {}"
MensajeIguales = "El numero {} es igual al numero {}, ya que {} == {}"
#-----Codigo de entrada-----
NumeroA = int (input (Pregunta_A))
NumeroB = int (input (Pregunta_B))
if (NumeroA > NumeroB):
    print (MensajeMayor.format ("A","B", NumeroA, NumeroB))
elif (NumeroB > NumeroA):
    print (MensajeMayor.format ("B","A", NumeroB, NumeroA))
else : 
    print (MensajeIguales.format ("A","B", NumeroA, NumeroB))


#Ejercicio 2
print ("#"*20, "¿Eres joven, adulto o adulto mayor?", "#"*20)

#Ejercicio 3
print ("#"*20, "¿Cual es la diferencia entre un año cualquiera y el actual?", "#"*20)

#Ejercicio 4 
print ("#"*20, "Convirtamos medidas", "#"*20)