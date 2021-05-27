# Punto4. (Valor 2.0) Un consultorio de neurología desea tener un archivo para el manejo de los 
#                     clientes, se pide que desarrolle un programa que en su primera ejecución cree 
#                     el archivo llamado pacientes.txt. Luego en cada ejecución se preguntará por 
#                     el nombre del paciente, una descripción de la enfermedad y el precio de la 
#                     consulta (se deben almacenar estos datos nuevos en el archivo pacientes.txt).

nombrePaciente = input ("Ingrese el nombre del paciente: ")
Enfermedad = input ("Ingrese una breve descripción de la patología: ")
precioConsulta = 0
nombreArchivo = "Pacientes.txt"

try:
    archivo = open (nombreArchivo)
except FileNotFoundError:
    archivo = open (nombreArchivo, "w", encoding="UTF-8")
    descripcionArchivo = "Datos pacientes consultorio neurología\n"
    archivo.writelines (descripcionArchivo)
    archivo.close()

isCorrectInfo = False
while (isCorrectInfo == False):
    try:
        precioConsulta = int (input("Ingrese el valor de la consulta: "))
        isCorrectInfo = True
    except ValueError:
        print ("Los datos ingresados son erroneos, intentelo de nuevo")

archivo = open (nombreArchivo, "a", encoding="UTF-8")
archivo.write (f"Paciente: {nombrePaciente}\n")
archivo.write (f"Descripción de la patología: {Enfermedad}\n")
archivo.write (f"Precio de la consulta: {precioConsulta}\n")
archivo.close()

