#----- constantes-----#
MENSAJE_BIENVENIDA = "Hola, ¡Bienvenido!"
NUMERO1 = "Ingresa un numero entero  "
NUMERO2 = "Ingresa otro numero entero "
MENSAJE_VERIFICACIÓN = "¿El primer numero que ingresaste es mayor que el segundo?"
MENSAJE_SUMA = "El resultado de sumar los dos numeros ingresados es "
MENSAJE_RESTA = "El resultado de restarle el segundo numero ingresado al primero es "
MENSAJE_MULTIPLICACIÓN = "El resultado de multiplicar el primer numero ingresado por el segundo es "
MENSAJE_DIVISIÓN = "El resultado de dividir el primer numero por el segundo es "
MENSAJE_EXPONENTE = "El resultado de elevar el primer numero al segundo es "
MENSAJE_DESPEDIDA = "¡Muchas gracias por tu participación!"

#-----codigo entrada-----#
print (MENSAJE_BIENVENIDA)
a = int (input (NUMERO1))
b = int (input (NUMERO2))
#Verificamos si el primer numero ingresado es mayor que el segundo
IsMayor = a > b
print (MENSAJE_VERIFICACIÓN, IsMayor)
#Realizamos operaciones basicas con los numero ingresados
sumar = a + b
restar = a - b
multiplicar = a*b
dividir = a/b
exponente = a**b
print (MENSAJE_SUMA, sumar)
print (MENSAJE_RESTA, restar)
print (MENSAJE_MULTIPLICACIÓN, multiplicar)
print (MENSAJE_DIVISIÓN, dividir)
print (MENSAJE_EXPONENTE, exponente)
print (MENSAJE_DESPEDIDA)