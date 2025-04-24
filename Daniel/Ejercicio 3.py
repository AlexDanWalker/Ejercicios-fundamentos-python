#Calcular area rectangulo

base = float (input ("Escribe la base del rectangulo =>"))
altura = float (input ("EScribe la altura del rectangulo =>"))

area = base * altura 

print (f"El area del rectangulo es => {area}")

#Dado un precio y un porcentaje mostrar valor final a pagar

precio = float (input ("Escriba el precio del producto=>"))
descuento = float (input ("EScribe el porcentaje de descuento=>"))

Monto_descuento = precio * (descuento/100)
Total_precio = precio - Monto_descuento

print (f"El descuento es de:{Monto_descuento}")
print (f"El precio a pagar es:{Total_precio}")

#calcula el residuo de dividir dos números dados por el usuario.

Num1 = int (input ("Escribe el numero que va a ser dividido=>"))
Num2 = int (input ("Escribe el numero por el que sera dividido=>"))

resultado = Num1 / Num2
residuo = Num1 % Num2 

print (f"El resultado de la divison es {resultado} y el residuo de dividir los dos numeros es:{residuo}")

#Escribe una fórmula que use al menos tres operadores diferentes y muestre el resultado.

a = 15
b = 10
c = 69

resultado2 = (a+b) * c ** 2 - 4

print ("El resultado de la formula es:",resultado2)