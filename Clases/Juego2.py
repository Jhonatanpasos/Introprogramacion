
import random
#------Entradas-------#
MENSAJE_SALUDAR = """
    Bienvenido 
        a este programa
    ¡¡¡juguemos!!!"""
MENSAJE_SEGUNDO_NIVEL = "Felicidades pasaste el primer nivel ahora ve por el último!!"
MENSAJE_CALIENTE = "Estas caliente"
MENSAJE_FRIO = "Estas Frio"
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
NumeroOcultoDos = random.randint (1,10)
vidas = None

dificultad = int (input(PREGUNTA_DIFICULTAD))
while (dificultad !=1 and dificultad !=2 and dificultad !=3):
    print ("ingresa una opción valida")
    dificultad = int (input (PREGUNTA_DIFICULTAD))

if (dificultad == 1):
    print ("Nivel facil")
    vidas = 10
elif (dificultad == 2):
    print ("Nivel moderado")
    vidas = 6
else:
    print ("Nivel dificil...buena suerte")
    vidas = 3

NumeroIngresado = int (input (PREGUNTAR_NUMERO))
while (NumeroIngresado != NumeroOculto and vidas>1):
    if (NumeroIngresado > NumeroOculto):
        print (MENSAJE_CALIENTE)
    else:
        print(MENSAJE_FRIO)
    vidas -=1
    print (f"te quedan {vidas} vidas")
    NumeroIngresado = int (input (PREGUNTAR_FALLIDA))
if(vidas >= 0 and NumeroIngresado == NumeroOculto):
    print (MENSAJE_SEGUNDO_NIVEL)
    NumeroIngresado = int (input(PREGUNTAR_NUMERO))
    while (NumeroIngresado != NumeroOcultoDos and vidas>1):
        if (NumeroIngresado > NumeroOcultoDos):
            print (MENSAJE_CALIENTE)
        else:
            print(MENSAJE_FRIO)
        vidas -=1
        print (f'te quedan {vidas} vidas')
        numeroIngresado =int(input(PREGUNTAR_FALLIDA))

if (vidas >= 0 and NumeroIngresado == NumeroOcultoDos ):
    print (MENSAJE_GANASTE)
else:
    print (MENSAJE_PERDISTE,"...el numero era el ", NumeroOculto, "...el numero dos era el ", NumeroOcultoDos)
