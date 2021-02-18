#-----Constantes-----#
MENSAJE_BIENVENIDA = "Bienvenido al codigo"
MENSAJE_MAYOR_EDAD = "Eres mayor de edad, puedes continuar"
MENSAJE_MENOR_EDAD = "Eres menor de edad, no puedes continuar"
PREGUNTA_EDAD = "¿Que edad tienes? : "

#-----Entrada al codigo-----#
print (MENSAJE_BIENVENIDA)
edad = int (input (PREGUNTA_EDAD))
isMayor = edad >= 18
resultado = ""
if (isMayor):
    resultado = MENSAJE_MAYOR_EDAD
else:
    resultado = MENSAJE_MENOR_EDAD

print(resultado)