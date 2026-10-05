nombres = input("Dime tu nombre: ")
apellidos = input("Dime tus apellidos: ")
edad = input("Dime tu edad: ")
carrera = input("Dime tu carrera: ")

datos = f"Nombres: {nombres.title()}\nApellidos: {apellidos.title()}\nEdad: {edad}\nCarrera: {carrera.title()}"

with open("estudiante.txt", "w") as archivo:
    archivo.write(datos)

print("Guardado.")