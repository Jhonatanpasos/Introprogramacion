#------Constantes------#
MENSAJE_BIENVENIDA = "Hola, espero que estes bien"
PREGUNTA_NUMERO_A = "Ingrese un numero A : "
PREGUNTA_NUMERO_B = "Ingrese un numero B : "
MENSAJE_MAYOR = "El numero A es mayor que el B"
MENSAJE_MENOR = "El numero A es menor que el B"
MENSAJE_IGUAL = "El numero A es igual que el B"

#-----Entrada de código-----#
print (MENSAJE_BIENVENIDA)
numeroA = int (input (PREGUNTA_NUMERO_A))
numeroB = int (input (PREGUNTA_NUMERO_B))
IsMayor = numeroA > numeroB
IsMenor = numeroA < numeroB

resultado = ""
if (IsMayor) :
    print (MENSAJE_MAYOR)
    resultado = MENSAJE_MAYOR
elif (IsMenor) :
    print (MENSAJE_MENOR)
    resultado = MENSAJE_MENOR
else:
    print (MENSAJE_IGUAL)
    resultado = MENSAJE_IGUAL

print (resultado)