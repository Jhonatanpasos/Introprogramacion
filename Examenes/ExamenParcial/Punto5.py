# Se sabe que la sucesión de Fibonacci sigue el siguiente patrón 0,1,1,2,3,5,8,13,21,34,55,89,144,….
# Se le pide como ingeniero biomédico, que dado un número n de la sucesión muestre en pantalla su 
# valor. Por ejemplo, si el usuario digita 3 se mostrará 1 y si el usuario digita 5 mostrará 3 si 
# ingresa 100 debe mostrar el número que le corresponda en la sucesión

def Fibonacci (sucesión):
    a = 0
    b = 1
    for sucesión in range (sucesión -1):
        c = a + b
        a = b
        b = c
    return (a)

Lista = [0,1,1,2,3,5,8,13,21,34,55,89,144,...]
numero = Fibonacci (5)
print (f"El numero correspondiente de la sucesión con la posición indicada es {numero}")