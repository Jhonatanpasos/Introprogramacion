#Otorgamos un valor verdadero o falso a las variables de prueba
pruebaV = True
pruebaF = False
print (pruebaV)
print (pruebaF)
pruebaV = pruebaF
print (pruebaV)
#Le damos valores a las variables para la actividad
edad = 19
estatura = 1.72
peso = 45
NOMBRE = "Jhonatan Alexander Pasos Cortes"
#Separamos la primera sección para observar condicionales
print ("#"*10, "Mayoria de edad", "#"*10)
#Miramos si la edad introducida es mayor o igual a 18 
isMayorEdad = edad >= 18
print (isMayorEdad)
#Separamos la segunda sección para observar condicionales
print ("#"*10, "Estatura bajo el promedio", "#"*10)
#Miramos si la estatura es menor de 1.70
isMayorEstatura = estatura < 1.70
print (isMayorEstatura)
#Separamos la tercera sección para observar condicionales
print ("#"*10, "peso diferente de 84", "#"*10)
#Miramos si tiene un peso diferente a 84 kg
isPesoDiferente = peso != 84
print (isPesoDiferente)
#Separamos la cuarta sección para observar condicionales
print ("#"*10, "Esta el apellido en nombre", "#"*10)
#Miramos si el apellido "Pasos" esta en la varible nombre
apellido = "Pasos"
isApellido = apellido in NOMBRE
print (isApellido)