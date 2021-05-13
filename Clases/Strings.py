texto = "Hola espero que todo ande bien"
lista = [1, 434, 53, 2, 2]
lista.sort()
print(lista)
lista.pop(2)
for elemento in lista:
    print (elemento)
for i in range (len(lista)):
    print(lista[i])

for letra in texto:
    print(letra)

print(texto[1])
palabras = texto.split(" ")
print (palabras)
eliminarE = texto.split("e")

print(eliminarE)