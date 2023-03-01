# ciclos

HARD_PASSWORD = "Kendymaster"

password = input("Cual es tu password?")

while password == HARD_PASSWORD:
    print("password incorrecto mivida")
    password = input("Escribe tu password otra vez more:")
    
print("Tu password es correcto mi cielo")

# Edad

edad = input("Cual es tu edad?")
edad = int(edad)

while edad < 18 :
    print("Es menor, espera in anio")
    edad = edad + 1
    print(edad)
print("Ya es mayor")