
import random

numero_secreto = random.randint(0,100)
cant_intentos = 0
cant_maxintentos = 5
adivinado = False

print("Bienvenido al juego de adivinar el numero secreto")

while not adivinado and cant_intentos < cant_maxintentos:
    entrada = input("inroduce un numero del 1 al 99 ")
    numero = int(entrada)

    if numero == numero_secreto:
        print ("adivinaste el numero Felicitaciones")
        adivinado = True

    elif numero < numero_secreto:

        print ("el numero es mayor al ingresado")
    else:
        
        print ("el numero es menor al ingresado")
    cant_intentos +=1
                        
if not cant_intentos<cant_maxintentos:    
    print("no adivinaste en los 5 intenos")
