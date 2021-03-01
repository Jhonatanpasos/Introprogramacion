#-----Constantes------
MENSAJE_SALUDO = """
    Bienvenido
        a este programa
    ¡vamos a jugar!"""
PREGUNTAR_NUMERO = """
        En este juego debes acertar un número entero
        que va desde el 1-10, para lograrlo tienes tres
        intento...muchos exitos!
        comencemos, ingresa tu numero: 
"""
MENSAJE_FALLIDO = "Fallasteee...ingresa otro numero: "
MENSAJE_GANASTE = "¡Felicitaciones, ganaste!"
MENSAJE_PERDISTE = "Perdiste D:"
#------Entrada al codigo-------
NumeroOculto = 7
vidas = 3
print (MENSAJE_SALUDO)
NumeroIngresado = int (input (PREGUNTAR_NUMERO))
if (NumeroIngresado != NumeroOculto):
    vidas -=1
while (NumeroOculto != NumeroIngresado and vidas>0):
    NumeroIngresado = int (input (MENSAJE_FALLIDO))
    vidas -=1

if (vidas >= 0 and NumeroOculto == NumeroIngresado):
    print (MENSAJE_GANASTE)
    print ("Te queda(n)", vidas, "intento(s)")
else: 
    print (MENSAJE_PERDISTE, "el numero era el", NumeroOculto)