listaDolares = [20000,30000,4000,2500,1000,7600]

#---------Preguntas------------#
PreguntaMenu = """
    1 - Conversión de dolares a otras monedas
    2 - Clasificación de ingresos mensuales
    3 - Ingresos maximo y minimo y el promedio
    4 - Salir
Bienvenido, ingrese un numero para comenzar : 
"""
PreguntaConversión = """
    C - mostrar la lista en pesos colombianos
    D - mostrar la lista en dólares
    E - mostrar la lista en euros
Ingrese una moneda a convertir : 
"""

#----------Mensajes-------------#
MensajeErrorMenu = "Error, ingrese una opción valida"
MensajeErrorConversión = "Error, ingrese una opción valida"
MensajeElecciónMenu = "Usted ha elegido la opción {}"
MensajeDolares = "Los datos ya estan en dolares"
MensajeSalida = "Gracias por usar el programa, ¡Buen dia!"

#----------Entrada al codigo---------#
menu = int (input (PreguntaMenu))

#----------Conversión de moneda--------#
listaPesosColombianos = []
listaEuros = []
for elemento in  listaDolares:
    pesos  = elemento * 3700
    listaPesosColombianos.append(pesos)
for elemento in  listaDolares:
    euros  = elemento * 0.84
    listaEuros.append(euros)

#----------Clasificación de ingresos mensuales----------#
listaClasificacion = []
for elemento in listaDolares:
    clasificacion = ''
    if (elemento < 1000 ):
        clasificacion = 'Ingresos bajos'
    elif (elemento >= 1000 and elemento < 7000):
        clasificacion = 'Ingresos medios'
    elif (elemento >= 7000 and elemento < 20000):
        clasificacion = 'Ingresos altos'
    else:
        clasificacion = 'Ingresos elevados'
    listaClasificacion.append(clasificacion)

#--------Ingresos maximos, minimos y promedio-------#
mayor = max (listaDolares)
menor = min (listaDolares)
acumulador = 0
for elemento in listaDolares :
    acumulador += elemento
promedio= acumulador/len(listaDolares)
promedioDolares = round (promedio,2)

#--------Entrada al menu--------#
while (menu != 4) :
    if (menu == 1):
        print(MensajeElecciónMenu.format(1))
        conversion = input(PreguntaConversión)
        if (conversion == 'C'):
            print (listaPesosColombianos)
        elif (conversion == 'E') :
            print (listaEuros)
        elif (conversion == 'D') :
            print (MensajeDolares)
            print (listaDolares)
        else :
            print (MensajeErrorConversión)
    elif (menu == 2):
        print(MensajeElecciónMenu.format(2))
        print (listaClasificacion)
    elif (menu == 3):
        print(MensajeElecciónMenu.format(3))
        print ('El ingreso máxima fue', mayor)
        print ('El ingreso mínima fue', menor)
        print ('El ingreso en promedio fue', promedioDolares)
    else:
        print (MensajeErrorMenu)
    menu = int (input (PreguntaMenu))
print (MensajeSalida)