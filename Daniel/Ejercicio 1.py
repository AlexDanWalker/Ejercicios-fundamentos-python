#Solicita el nombre y edad del usuario, luego imprime un saludo personalizado que incluya ambos datos.
#Pide al usuario que ingrese su comida favorita y su color favorito, luego imprime una frase con ambos.
#Solicita un número y muestra su doble y su triple.

name = input ("Ingresa tu nombre =>")
edad = input ("Ingresa tu edad =>")

print ("Hola",name,"de",edad, "años, dquiza ese sea tu numero de la suerte")

food = input ("¿Cual es tu comida favorita? =>")
color = input ("¿Cual es tu color favorito? =>")

print (food,"sin duda es un platillo delicioso, aunque nunca he visto un",food,"de color",color)

num = int (input("Por favor, digita un número => "))

doble = num * 2
triple = num * 3

print("El doble de", num, "es", doble, "y el triple es", triple)