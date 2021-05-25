#Crear una función que dada una lista de números enteros muestre el promedio, el máximo, el mínimo.

def numerosEnteros (lista):
    maximo = max (lista)
    minimo = min (lista)
    datos = 0
    for elemento in lista:
        datos += elemento
    tamañoLista = len (lista)
    promedio = datos / tamañoLista
    print (f"El número maximo es {maximo}")
    print (f"El numero minimo es {minimo}")
    print (f"El promedio es {promedio}")
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numerosEnteros (numeros)
