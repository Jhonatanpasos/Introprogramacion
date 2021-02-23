# Como ingeniero biomédico se le pide desarrollar un programa que permita que el personal 
# de salud a cargo ingrese el nivel de triglicéridos y de homocisteína y al final muestre 
# en qué estado está (Óptimo, Sobre el límite óptimo, alto y muy alto) Valor 4.0

#-----Constantes-----
Bienvenida = "¡Bienvenido! vamos a verificar los valores del perfil lipidico"
PreguntaTriglicéridos = "Ingrese el nivel de triglicéridos del paciente (en mg/dL) : "
PreguntaHomocisteína = "Ingrese el nivel de homocisteína del paciente (en micromoles/L): "
MensajeTiglicéridos = "El resultado de triglicéridos fue {} "
MensajeHomocisteína = "El resultado de Homocisteína fue {}"

#-----Codigo de entrada-----
Triglicéridos = float(input (PreguntaTriglicéridos))
Homocisteína = float (input (PreguntaHomocisteína))
OptimoTri = Triglicéridos < 150
SobreLimiteTri = Triglicéridos >= 150 and Triglicéridos <= 199
AltoTri = Triglicéridos >= 200 and Triglicéridos <= 499
MuyAltoTri = Triglicéridos >= 500
OptimoHom = Homocisteína >= 2 and Homocisteína < 15
SobreLimiteHom = Homocisteína >= 15 and Homocisteína < 30
AltoHom = Homocisteína >= 30 and Homocisteína <= 100
MuyAltoHom = Homocisteína > 100
if (OptimoTri):
    print (MensajeTiglicéridos.format ("óptimo"))
elif (SobreLimiteTri):
    print (MensajeTiglicéridos.format ("sobre el limite óptimo"))
elif (AltoTri):
    print (MensajeTiglicéridos.format ("alto"))
else:
    print (MensajeTiglicéridos.format ("muy alto"))
if (OptimoHom):
    print (MensajeHomocisteína.format ("óptimo"))
elif (SobreLimiteHom):
    print (MensajeHomocisteína.format ("sobre el limite óptimo"))
elif (AltoHom):
    print (MensajeHomocisteína.format ("alto"))
else: 
    print (MensajeHomocisteína.format ("muy alto"))