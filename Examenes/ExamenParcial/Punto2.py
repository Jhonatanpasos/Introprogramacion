# Crear una función que dada tres listas del mismo tamaño las muestre en pantalla

def mostrarListas (lista):
    for elemento in lista:
        print (elemento)
numeros = [10, 20, 30, 40, 50]
colores = ["Verde", "Amarillo", "Azul", "violeta", "rojo"]
objetos = ["mesa", "silla", "escritorio", "plato", "celular"]
mostrarListas (numeros)
mostrarListas (colores)
mostrarListas (objetos)