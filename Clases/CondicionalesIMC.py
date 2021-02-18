#------constantes------#
PREGUNTA_ESTATURA = "¿Cual es tu estatura en metros (m)? : "
PREGUNTA_PES0 = "¿Cuanto pesas en kilogramos (kg)? : "
MENSAJE_BIENVENIDA = "Hola, ¡bienvenido! vamos a calcular tu IMC"
MENSAJE_DESPEDIDA = "Tu Indice de masa corporal (imc) es ..."
MENSAJE_BAJO_PESO = "Tu imc esta por debajo de lo ideal"
MENSAJE_NORMAL = "Tu imc esta dentro de los rangos normales"
MENSAJE_SOBRE_PESO = "Tu imc indica que estas en sobre peso"
MENSAJE_OBESO = "Tu imc indica que tienes obsesidad"

#------codigo entrada------#
print (MENSAJE_BIENVENIDA)
estatura = float (input (PREGUNTA_ESTATURA))
peso = float (input (PREGUNTA_PES0))
imc = peso/(estatura**2)
isBajoPeso = imc < 18.5
isNormal = imc >= 18.5 and imc < 25
isSobrePeso = imc >= 25 and imc < 30
resultado =""
if (isBajoPeso):
    resultado = MENSAJE_BAJO_PESO
elif (isNormal):
    resultado = MENSAJE_NORMAL
elif (isSobrePeso):
    resultado = MENSAJE_SOBRE_PESO
else:
    resultado = MENSAJE_OBESO
print (MENSAJE_DESPEDIDA, imc)
print (resultado)