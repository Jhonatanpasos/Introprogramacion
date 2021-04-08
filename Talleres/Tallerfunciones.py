#1.Dada una lista muéstrela en pantalla elemento a elemento#
def mostrarElemento (lista):
    for elemento in lista :
        print (elemento)
ciudades = ["Medellin", "Miami", "Bogota", "Cali", "Londres"]
nombres = ["Mariana","Jhonatan", "Isabella", "Alejandro", "Samuel"]
mostrarElemento (ciudades)
mostrarElemento (nombres)

# Dada una lista de números enteros muestre en pantalla el 
# número más grande, el más pequeño y el promedio de la lista
def numerosEnteros (lista):
    maximo = max (lista)
    minimo = min (lista)
    datos = 0
    for elemento in lista:
        datos += elemento
    tamañoLista = len (lista)
    promedio = datos / tamañoLista
    print (f'el número mayor en la lista es el {maximo}, el menor {minimo} y el promedio {promedio}')
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
numerosEnteros (numeros)

# Salude n veces
def saludo (cantidad = 0):
    print ("Hola, "*cantidad)
saludo (3)

# Que devuelva todos los números pares de una lista de números enteros
def ListaPares (lista):
    pares = []
    for elemento in lista:
        if elemento % 2 == 0:
            pares.append (elemento)
    return pares

edades = [12,15,18,19,26,25,24,97]
edadesPares = ListaPares (edades)
print (edadesPares)

# Que devuelva únicamente los elementos mayores a 24
def numerosMayores (lista):
    mayores = []
    for elemento in lista:
        if elemento > 24:
            mayores.append (elemento)
    return mayores
edades = [23,22,12,45,17,33,77,18]
edadesMayores = numerosMayores (edades)
print (edadesMayores)

# Se sabe que el IMC se calcula dividiendo el peso por la altura al cuadrado, 
# realice una función que lo calcule.
def calcularIMC (peso, altura):
    return peso /(altura**2)
imc = calcularIMC (45, 1.73)
print (imc)

# Crea un función que sirva para despedirte del que esta ejecutando el código
def despedida ():
    print ("Hasta la proxima")
despedida()
