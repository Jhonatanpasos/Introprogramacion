PruebaT = True
PruebaF = False
#Otorgamos valores a las variables persona 1
NombreA = "Mateo Gomez"
EstaturaA = 1.80
EdadA = 18
#Otorgamos valores a las variables persona 2
NombreB = "Jhonatan Pasos"
EstaturaB = 1.71
EdadB = 19
#Otorgamos valores a las variables persona 3
NombreC = "Elio Fernandez" 
EstaturaC = 1.79
EdadC = 21
#Miramos quien de los dos es mayor 
print ("#"*10, "¿Es Jhonatan pasos mayor a Mateo y menor a Elio?", "#"*10)
IsMayor = EdadA < EdadB < EdadC
print (IsMayor)
#Miramos si el apellido Gomez esta en el nombre de Jhonatan
print ("#"*10, "¿Esta el apellido gomez en el nombre de Jhonatan?", "#"*10)
apellido = "Gomez"
IsApellido = apellido in NombreB
print (IsApellido)
#Operamos entre variables
sumar = EdadA + EdadC + EdadB
print ("El resultado de sumar entre edades es", sumar)
restar = EdadA - EdadC
print ("El resultado de la resta entre la edad de Mateo y la de Elio es", restar)
multiplicar = EstaturaA*EstaturaB
print ("El resultado de la multiplicación entre la estatura de Mateo y la de Jhonatan es", multiplicar)
exponente = EdadB**EstaturaA
print (f"el resultado de elevar la edad de Jhonatan a la estatura de Mateo es {exponente}")