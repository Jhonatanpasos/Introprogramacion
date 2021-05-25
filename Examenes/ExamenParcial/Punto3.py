# Crear una función que calcule y devuelva el área de un triangulo recuerde que la
# formula del mismo es (base*altura) /2. Pida las entradas que considere necesarias

PreguntaBase = "Ingrese un valor para la base del triangulo: "
PrenguntaAltura = "Ingrese un valor para la altura del triangulo: "

base = float (input (PreguntaBase))
altura = float (input (PrenguntaAltura))

def áreaTriangulo ():
    área = (base*altura)/2
    return área
resultado = áreaTriangulo ()
print (f"El área del triangulo es {resultado}")