#----------Sumar dos números -----------#
def sumar (a = 0, b = 0):
    suma = a + b 
    return suma

#----------Restar dos números -----------#
def restar (a = 0, b = 0):
    resta = a - b
    return resta

#----------Multiplicar dos números -----------#
def multiplicar (a = 0, b = 0):
    multiplica = a * b
    return multiplica

#----------dividir dos números -----------#
def dividir (a = 0, b = 1):
    divide = a / b
    return divide

#---------Elevar al exponente ----------#
def potencia (a = 0, b = 1):
    exponente = a**b
    return exponente

#---------Funciones dependientes de otras---------#
def calcular (operación, numeroA, numeroB):
    print (operación(numeroA, numeroB))