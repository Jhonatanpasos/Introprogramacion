#-----Constantes------
MENSAJE_SALUDO = """
    Bienvenido
        a este programa
    ¡vamos a jugar!"""
PREGUNTAR_NUMERO = """
        En este juego debes acertar un número entero
        que va desde el 1-10, la idea es que lo
        puedes intentar las veces que quieras..
        muchos exitos, ingresa tu numero 
"""
MENSAJE_FALLIDO = "Fallasteee...ingresa otro numero"
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
    NumeroIngresado = int (input (PREGUNTA_FALLIDA))
    vidas -=1

if (vidas > 0):
    print (MENSAJE_GANASTE)
    print (vidas)
else 
    print (MENSAJE_PERDISTE, "el numero era el", NumeroOculto )