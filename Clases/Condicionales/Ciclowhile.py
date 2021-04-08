#------Constantes--------
MENSAJE_SALUDAR = "¡Bienvenido! vamos a ahorrar para comprar un computador"
MENSAJE_AHORRO = "Llevas ahorrado..."
PREGUNTAR_VALOR_PCU = "¡Cuanto cuesta el computador que deseas comprar? : "
PREGUNTAR_CUANTO_TIENE = "¿Cuanto llevas ahorrado? : "

#-------Entrada a codigo-------
print (MENSAJE_SALUDAR)
valor = float (input (PREGUNTAR_VALOR_PCU))
ahorrado = float (input (PREGUNTAR_CUANTO_TIENE))

while (valor > ahorrado):
    print (MENSAJE_AHORRO, ahorrado, "te faltan ",  valor - ahorrado)
    ahorrado = ahorrado + 1000
print (valor == ahorrado)