#-----Constantes------
#Definimos la preguta
PREGUNTA_NOMBRE = "¿Como te llamas? : "
PREGUNTA_EDAD = "¿Que edad tienes? : "
PREGUNTA_ESTATURA = "¿Cuanto mides? : "
MENSAJE_SALUDO = "Un gusto conocerte"

#-----Entrada al codigo-----
nombre = input (PREGUNTA_NOMBRE)
print (MENSAJE_SALUDO, nombre)

edad = int (input (PREGUNTA_EDAD))
#ponemos el int antes del input para convertir el dato de entrada en un numero entero ya que los inputs siempre dan un string (texto)
print (edad + 10)

estatura = float (input (PREGUNTA_ESTATURA))
#ponemos el float antes del input para convertir el dato de entrada en un numero con decimales ya que los inputs siempre dan un string (texto)
print (estatura)