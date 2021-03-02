
import random
#------Entradas-------#
MENSAJE_SALUDAR = """
    Bienvenido 
        a este programa
    ¡¡¡juguemos!!!"""
PREGUNTAR_NUMERO = """
    En este juego debes acertar un numero entero 
    que va desde el 1-10. Tienes varias vidas que 
    equivalen a un numero de intentos...no existe 
    vida 0...¡¡ Muchos exitos!!
    Ingresa tu numero: 
"""
PREGUNTA_DIFICULTAD = """
    1- Facil
    2- Moderado
    3- Dificil
"""
PREGUNTAR_FALLIDA = "Ahhhh! fallaste...ingresa otro numero: "
MENSAJE_GANASTE = "¡Felicidades, ganaste!"
MENSAJE_PERDISTE = "Perdiste, vuelve a intentarlo"

#-----Entrada al codigo-----#
NumeroOculto = random.randint (1,10)
vidas = None

dificultad = int (input(PREGUNTA_DIFICULTAD))
while (dificultad !=1 and dificultad !=2 and dificultad !=3):
    print ("ingresa una opción valida")
    dificultad = int (input (PREGUNTA_DIFICULTAD))

if (dificultad == 1):
    print ("Nivel facil")
    vidas = 5
elif (dificultad == 2):
    print ("Nivel moderado")
    vidas = 3
else:
    print ("Nivel dificil...buena suerte")
    vidas = 1

NumeroIngresado = int (input (PREGUNTAR_NUMERO))
while (NumeroIngresado != NumeroOculto and vidas>1):
    vidas -=1
    NumeroIngresado = int (input (PREGUNTAR_FALLIDA))
    print (f"te quedan {vidas} vidas")

if(vidas >= 0 and NumeroIngresado == NumeroOculto):
    print (MENSAJE_GANASTE)
else:
    print (MENSAJE_PERDISTE, "...el numero era el ", NumeroOculto)
