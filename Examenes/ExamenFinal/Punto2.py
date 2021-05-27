#Punto2. (valor 1.0) Cree una clase humano con atributos nombre, sexo, edad y con la acción hablar 
#                    donde dado un mensaje se mostrará en pantalla. Luego cree una clase Doctor que 
#                    herede de humano y tenga la acción adicional de que dado una estatura y un peso 
#                    calcule el IMC y lo muestre en pantalla.

class Humano():
    def __init__ (self, nombreEntrada, edadEntrada, sexoEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.sexo = sexoEntrada

    def hablar (self, mensaje):
        print (f"Hola soy {self.nombre}, tengo {self.edad} años y tengo un mensaje que decir...", mensaje)

class Doctor (Humano):
    def calcularIMC (self, peso, estatura) :
        imc = peso/(estatura**2)
        print (f"Hola mi nombre es {self.nombre}, y procedere a calcular tu indice de masa corporal (imc)")
        print (imc)

humano = Humano ("Jhonatan", 19, "Masculino")
humano.hablar ("Muchas gracias profe, te agradezco por todo este semestre")
doctor = Doctor ("Jhonatan", 19,"Masculino")
doctor.calcularIMC (45, 1.72)
