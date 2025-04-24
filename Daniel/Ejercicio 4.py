#Pide dos números e indica cuál es mayor o si son iguales.
numero1 = int(input("Escribe un numero =>"))
numero2 = int(input("Escribe otro numero =>"))

if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
elif numero2 > numero1:
    print(f"{numero2} es mayor que {numero1}")
else:
    print("Ambos numero son iguales")

#Solicita una edad y determina si la persona es menor de edad (menor a 18).

edad = int(input("Escriba su edad => "))

if edad < 18 and edad > 0:
    print("Eres menor de edad")
elif edad >= 18:
    print("Eres mayor de edad")
else:
    print("La edad ingresada es inválida")

#Escribe un programa que compare dos cadenas de texto e indique si son iguales o distintas.

cadena1 = input("Escribe la primera cadena de texto. => ")
cadena2 = input("Escribe la segunda cadena de texto. => ") 

if cadena1 == cadena2: 
    print ("Las dos cadenas de texto son iguales.")
else:
    print ("Las dos cadenas de texto son diferentes.")
