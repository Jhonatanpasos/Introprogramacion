# Punto3. (valor 1.0) Se sabe que un Dólar son 0.82 euros, indique a un usuario que ingrese su 
#                     dinero en dólares y su nombre, luego muestre en pantalla el nombre del usuario 
#                     y cuanto dinero tiene en dólares (recuerde validar que todos los datos ingresados 
#                     por el usuario sean del formato correcto).

def ConversorDolares ():
    isCorrectInfo = False
    while(isCorrectInfo == False):
        try:
            nombre = input ("Buenos dias, porfavor ingrese su nombre: ")
            assert (nombre.isalpha())
            isCorrectInfo = True
        except AssertionError:
            print ("Los datos ingresados no son validos, intente de nuevo")
        
    isCorrectInfo = False
    while(isCorrectInfo == False):
        try:
            dinero = float (input("Ingrese su dinero (en dolares): "))
            isCorrectInfo = True
        except ValueError:
            print("Los datos ingresados no son validos, intente de nuevo")

    print(f"Buenos dias {nombre}, dada tu cantidad ingresada en dolares, en euros tienes {dinero*0,82}")

ConversorDolares()
input("\nPresione una tecla para contiuar")
