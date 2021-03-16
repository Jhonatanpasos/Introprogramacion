listaTemperaturaCorporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
PreguntaMenu = """
Bienvenido,  
    1 - Conversión de temperatura
    2 - Clasificación de temperatura
    3 - temperatura maxima y minima
    4 - Salir
Ingrese un numero para comenzar : """
PreguntaConversión = """
    C - mostrar la temperatura en Celsius
    K - Celsius a Kelvin
    F - Celsius a Fahrenheit. 
Ingrese una letra en Mayuscula de acuerdo a la temperatura que desea convertir : 
"""

#-------Mensajes-------#
MensajeCelsius = "Los datos de temperatura ya estan en grados Celsius, la coversión no es necesaria"
MensajeElección = "Usted ha elegido la opción {}"
MensajeErrorMenu = "Error, ingrese una opción valida"
MensajeSalida = "Gracias por usar el programa, ¡Buen dia!"

#--------Entrada al codigo---------#
opción = int (input (PreguntaMenu))

#--------Conversión de temperaturas----------#
listaFahrenheit = []
listaKelvin = []
for elemento in  listaTemperaturaCorporal:
    fahrenheit = round (elemento * 1.8) + 32
    listaFahrenheit.append(fahrenheit)
for elemento in  listaTemperaturaCorporal:
    kelvin = round (elemento + 273.15)
    listaKelvin.append(kelvin)

#----------Clasificación de temperaturas----------#
listaClasificacion = []
for elemento in listaTemperaturaCorporal:
    clasificacion = ""
    if (elemento < 36 ):
        clasificacion = "Hipotermia"
    elif (elemento >= 36 and elemento <= 37.5):
        clasificacion = "Temperatura en rango normal"
    elif (elemento >= 37.6):
        clasificacion = "Fiebre"
    else:
        clasificacion = "Datos imposibles"
    listaClasificacion.append(clasificacion)

#--------Temperatura maxima y minima-------#
maxima = max (listaTemperaturaCorporal)
minima = min (listaTemperaturaCorporal)

#---------Entrada al menu----------#
while (opción != 4) :
    if (opción == 1):
        print (MensajeElección.format(1))
        conversion = input(PreguntaConversión)
        if (conversion == 'C'):
            print (MensajeCelsius)
            print (listaTemperaturaCorporal)
        elif (conversion == 'F') :
            print (listaFahrenheit)
        elif (conversion == 'K') :
            print (listaKelvin)
        else :
            print (MensajeErrorMenu)
    elif (opción == 2):
        print (MensajeElección.format(2))
        print (listaClasificacion)
    elif (opción == 3):
        print (MensajeElección.format(3))
        print ('La temperatura máxima fue', maxima)
        print ('La temperatura mínima fue', minima)
    else:
        print (MensajeErrorMenu)
    opción = int (input (PreguntaMenu))
print (MensajeSalida)