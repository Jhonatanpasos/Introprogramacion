# Este quiz lo realizamos en conjunto Felipe Carmona y Jhonatan Pasos
#------------Punto 1--------------#

class ElementosDigitales():
    def __init__ (self, nombreEntrada, creadorEntrada, fechadepublicacionEntrada):
        self.nombre = nombreEntrada
        self.creador = creadorEntrada
        self.fechadepublicacion = fechadepublicacionEntrada
    def mostrarAtributos(self):
        print (f"Hola, la plataforma de {self.nombre}, fue inventada por {self.creador}, creada el {self.fechadepublicacion}")

cancion = ElementosDigitales ("YouTube", "Google", "14 de Febrero 2005")
cancion.mostrarAtributos ()

class Usuario():
    def __init__ (self, nombre, edad, sexo, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.nacionalidad = nacionalidad
    def mostrarUsuario (self, canción): 
        print (f"Hola, soy {self.nombre} y estoy escuchando {canción}")

persona1 = Usuario ("Miguel", 14, "Masculino", "Puertorriqueño")
persona1.mostrarUsuario ("Despacito")

class Pagina():
    def __init__ (self, tipodecontenido, formato, fechapublicacion): 
        self.tipodecontenido = tipodecontenido
        self.formato = formato
        self.fechapublicacion = fechapublicacion
    def mostrarPagina (self, contenido):
        print (f"{contenido} hace parte de la musica urbana")

pagina1 = Pagina ("musica urbana", "MOV", "13 de Enero 2017" )
pagina1.mostrarPagina ("Despacito")

#-----------Punto 2-----------#

class Cancion (ElementosDigitales):
    def __init__ (self, nombreEntrada, creadorEntrada, fechadepublicacionEntrada, generoEntrada, duracionEntrada):
        ElementosDigitales.__init__(self, nombreEntrada, creadorEntrada, fechadepublicacionEntrada)
        self.genero = generoEntrada
        self.duracion = duracionEntrada
    def NuevaCancion (self, nombrenuevacancionEntrada, fechacreacionEntrada):
        self.nombrenuevacancion = nombrenuevacancionEntrada
        self.fechacreacion = fechacreacionEntrada
        print (f"El nombre de la nueva cancion es {self.nombrenuevacancion}, creada el {self.fechacreacion}")
    def Reproduccion (self, numeroreproducciones):
        for reproducciones in range (numeroreproducciones):
            if (reproducciones == 0):
                veces = "vez"
            else:
                veces = "veces"
            print (f"{self.nombrenuevacancion} ha sonado {reproducciones + 1} {veces}")

nuevacancion1 = Cancion ("YouTube", "Google", "14 de Febrero 2005", "Urbano", "171 segundos" )
nuevacancion1.NuevaCancion ("Tu Veneno", "18 de Marzo 2021 por JBalvin")
nuevacancion1.Reproduccion (7)

class Artista (Usuario):
    def __init__ (self, nombre, edad, sexo, nacionalidad, generomusical, numerodecanciones, numerodealbums):
        Usuario.__init__ (self, nombre, edad, sexo, nacionalidad)
        self.generomusical = generomusical
        self.numerodecanciones = numerodecanciones
        self.numerodealbums = numerodealbums
        print (f"Su genero musical es {self.generomusical} y cuenta con {self.numerodecanciones} canciones y {self.numerodealbums} albums")
    def Concierto (self, ciudad):
        print (f"JBalvin dara un concierto en {ciudad}")

artista1 = Artista ("JBalvin", 35, "Masculino", "Colombiano", "Urbano", 80, 4)
artista1.Concierto ("Ibague")

