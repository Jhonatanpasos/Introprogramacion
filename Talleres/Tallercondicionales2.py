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

#Ejercicio 2
print ("#"*20, "¿Eres joven, adulto o adulto mayor?", "#"*20)

#-----constantes-----
Bienvenida = "¡Bienvenido! vamos a mirar si eres joven o adulto"
Mensajeresultado = "De acuerdo a los datos ingresados, tu eres un {}"
PreguntaEdad = "Ingrese su edad : "

#-----Codigo de entrada-----
print (Bienvenida)
edad = int (input (PreguntaEdad))
if (edad < 18):
    print (Mensajeresultado.format ("menor de edad"))
elif (edad >= 18 and edad <= 25):
    print (Mensajeresultado.format ("adulto joven"))
elif (edad >= 26 and edad <= 60):
    print (Mensajeresultado.format ("adulto"))
else :
    print (Mensajeresultado.format ("adulto mayor"))