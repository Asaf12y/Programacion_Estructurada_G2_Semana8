#Crea y Guardar un archivos
frase = input("Dime tu frase favorita: ")

with open("frases.txt", "w") as archivo:
    archivo.write(frase)

print("Archivo creado sastifactoriamente.")