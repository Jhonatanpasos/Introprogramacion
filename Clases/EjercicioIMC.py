#------constantes------#
PREGUNTA_ESTATURA = "¿Cual es tu estatura en metros (m)? : "
PREGUNTA_PES0 = "¿Cuanto pesas en kilogramos (kg)? : "
MENSAJE_BIENVENIDA = "Hola, ¿bienvenido! vamos a calcular tu IMC"
MENSAJE_DESPEDIDA = "Tu Indice de masa corporal (imc) es ..."

#------codigo entrada------#
print (MENSAJE_BIENVENIDA)
estatura = float (input (PREGUNTA_ESTATURA))
peso = float (input (PREGUNTA_PES0))
imc = peso/(estatura**2)
print (MENSAJE_DESPEDIDA, imc)

IsObeso = imc >= 30
print ("El resultado de la prueba de obesidad es ", IsObeso)