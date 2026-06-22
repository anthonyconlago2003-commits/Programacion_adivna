import math

print(" La máquina adivina tu número ")
print("Piensa un número del 1 al 100")

inferior = 1
superior = 100
intentos = 0

while True:
    intento = math.floor((inferior + superior) / 2)
    print(f"\nLa máquina adivina: {intento}")
    print("1 = Sí, acertaste")
    print("2 = El número es menor")
    print("3 = El número es mayor")
    
    respuesta = int(input("Tu respuesta: "))
    intentos += 1
    
    if respuesta == 1:
        print(f"\n¡Acerté en {intentos} intentos!")
        break
    elif respuesta == 2:
        superior = intento - 1
    elif respuesta == 3:
        inferior = intento + 1