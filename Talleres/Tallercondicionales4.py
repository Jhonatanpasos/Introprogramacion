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


#Ejercicio 4 
print ("#"*20, "Convirtamos medidas", "#"*20)

#------Constantes------
Bienvenida = "¡Bienvenido! vamos a convertir medidas"
PreguntaMedida = "Ingrese la medida en centimetros (cm) : "
PreguntaConversión = """¿A que unidades desea hacer la conversión? : 
k - kilimetros
m - metros
mm - milimetros
Ingresa tu respuesta (la inical de la medida en minuscula) : """

#------Codigo de entrada------
medida = float (input (PreguntaMedida))
unidad = input (PreguntaConversión)
metros = medida *10**-2
kilometros = medida *10**-5
milimetros = medida *10
if (unidad == "k"):
    print (kilometros)
elif (unidad == "m"):
    print (metros)
elif (unidad == "mm"):
    print (milimetros)