# 1. Cree la clase Torta con atributos forma, sabor, altura, también tendrá una función donde
#    muestre todos sus atributos.

class Torta ():
    def __init__ (self,formaEntrada, saborEntrada,alturaEntrada):
        self.forma = formaEntrada
        self.sabor = saborEntrada
        self.altura = alturaEntrada

    def mostrarAtributos (self):
        print (f"""Soy una torta de forma {self.forma}, tengo un sabor delicioso de {self.sabor}  
        y tengo una altura de {self.altura} cm""")

Postre = Torta ("redonda", "caramelo", 10)
Postre.mostrarAtributos ()

# 2. Cree una clase Estudiante donde tenga de atributos edad, nombre, id, carrera, semestre. 
#    También este estudiante tendrá una función donde dada una materia y una cantidad de tiempo 
#    muestra en pantalla que estudiará dicha materia en esa cantidad de tiempo

class Estudiante():
    def __init__ (self, nombreEntrada, edadEntrada,idEntrada, carreraEntrada, semestreEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.id = idEntrada
        self.carrera = carreraEntrada
        self.semestre = semestreEntrada

    def materia (self, materia,tiempo) :
        print (f"Hola mi nombre es {self.nombre} y voy a estudiar {materia} por {tiempo} horas")

estudiante = Estudiante ("Jhonatan", 19, 1000543789, "Ingeniería Biomédica", 3)
estudiante.materia ("Morfofisiología", 8)

# 3. Cree una clase Nutricionista donde tendrá los atributos de edad, nombre, universidad en la 
#    que se egresó. Tendrá una función que dado el peso y la altura de un paciente calcule el IMC.

class Nutricionista():
    def __init__ (self, nombreEntrada, edadEntrada, universidadEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.universidad = universidadEntrada

    def calcularIMC (self, peso, estatura) :
        imc = peso/(estatura**2)
        print (f"Hola mi nombre es {self.nombre}, tengo {self.edad} y egresé de la universidad {self.universidad}")
        print (imc)

nutrición = Nutricionista ("Jhonatan", 19, "CES")
nutrición.calcularIMC (45, 1.72)

