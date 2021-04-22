# 1. Cree la clase Persona con id, nombre, edad y cree la función hablar la cual dado mensaje se muestra 
#    en pantalla y cree la clase caminar que dado una cantidad de pasos muestra en pantalla cuanto ha caminado

class Persona(): 
    def __init__ (self, nombreEntrada, edadEntrada, idEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.id = idEntrada

    def hablar (self, mensaje):
        print (f"Hola, mi nombre es {self.nombre}, tengo {self.edad} y espero estes bien")

    def caminar (self, pasos):
        for i in range (pasos):
            print (f"Hola he dado {i+1} pasos")

person = Persona ("Jhonatan", 19, 1000678238)
person.hablar(Persona)
person.caminar(24)

# 2. Herede la clase Persona y cree la clase Doctor el cual tendrá el nuevo atributo de especialidad y podrá 
#    ejecutar una nueva función, la cual es dado una enfermedad muestre en pantalla: procedo a tratar dicha enfermedad

class Doctor(Persona):
    def __init__ (self, nombreEntrada, edadEntrada, idEntrada, especialidadEntrada):
        Persona.__init__(self, nombreEntrada, edadEntrada, idEntrada)
        self.especialidad = especialidadEntrada
        
    def tratamiento (self, enfermedad):
        print (f"""Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy especialista en {self.especialidad}
                    asi que procederé a tratar tu {enfermedad}""")

Jhonatan = Doctor ("Jhonatan", 19, 1000229387, "cardiovascular")
Jhonatan.tratamiento ("Aterosclerosis")

# 3. Herede la clase Persona y cree la clase Nutricionista y cree un atributo que se refiera a la universidad 
#     en la que fue egresado. También una función que devuelva el IMC dado el peso y altura de un paciente

class Nutricionista(Persona):
    def __init__ (self, nombreEntrada, edadEntrada, idEntrada, universidadEntrada):
        Persona.__init__(self, nombreEntrada, edadEntrada, idEntrada)
        self.universidad = universidadEntrada
        
    def IMC (self, pesoEntrada, alturaEntrada):
        self.peso = pesoEntrada
        self.altura = alturaEntrada
        IMC = self.peso /(self.altura**2)
        print (f"""Hola, mi nombre es {self.nombre} y soy nutricionista egresado de la universidad {self.universidad}
            De acuerdo a tus registro, tu peso es {self.peso} kg y tu altura es {self.altura} cm
            Tus resultado del indice de masa corporal es {IMC}""")

Jhonatan = Nutricionista ("Jhonatan", 19, 1000938372, "CES")
Jhonatan.IMC (45, 1.74,)

# 4. Herede la clase Persona y cree la clase Abogado adicione dos atributos uno asociado a su especialidad y 
#    el otro a la universidad de la que egresó. Finalmente cree la función que dado un nombre y el caso de cliente 
#    el abogado diga : procedo a representar al cliente {nombre} en el caso {caso}