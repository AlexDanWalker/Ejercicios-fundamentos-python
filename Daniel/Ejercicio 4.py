#Pide dos números e indica cuál es mayor o si son iguales.
numero1 = int (input ("Escribe un numero =>"))
numero2 = int (input ("Escribe otro numero =>"))

if numero1 > numero2:
    print (f"{numero1} es mayor que {numero2}")
elif numero2 > numero1:
    print (f"{numero2} es mayor que {numero1}")
else:
    print ("Ambos numero son iguales")