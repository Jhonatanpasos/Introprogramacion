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

#Ejercicio 3
print ("#"*20, "¿Cual es la diferencia entre un año cualquiera y el actual?", "#"*20)

#-----Constantes-----
Bienvenida = "¡Bienvenido! vamos sacar la diferencia entre dos años diferentes"
PreguntaAño = "¿En que año estamos? : "
PreguntaDiferente = "Ingrese otro año diferente : "
MensajeResultado = "{} {} años"
MensajeIguales = "Los años ingresados son iguales"

#-----Codigo de entrada-----
print (Bienvenida)
AñoActual = int (input (PreguntaAño))
AñoDiferente = int (input (PreguntaDiferente))
if (AñoActual > AñoDiferente): 
    resta = AñoActual - AñoDiferente
    print (MensajeResultado.format ("han pasado", resta))
elif (AñoDiferente > AñoActual):
    resta = AñoDiferente - AñoActual
    print (MensajeResultado.format ("faltan", resta))
else :
    print (MensajeIguales)