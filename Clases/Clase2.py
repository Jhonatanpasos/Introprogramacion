pruebaV = True
pruebaF = False
print (pruebaV)
print (pruebaF)
pruebaV = pruebaF
print (pruebaV)
edad = 19
estatura = 1.72
peso = 45
NOMBRE = "Jhonatan Alexander Pasos Cortes"
print ("#"*10, "Mayoria de edad", "#"*10)
isMayorEdad = edad >= 18
print (isMayorEdad)
print ("#"*10, "Estatura bajo el promedio", "#"*10)
isMayorEstatura = estatura < 1.70
print (isMayorEstatura)
print ("#"*10, "peso diferente de 84", "#"*10)
isPesoDiferente = peso != 84
print (isPesoDiferente)
print ("#"*10, "Esta el apellido en nombre", "#"*10)
apellido = "Pasos"
isApellido = apellido in NOMBRE
print (isApellido)