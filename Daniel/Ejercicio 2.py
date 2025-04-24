# Declarar una variable de cada tipo básico
entero = 10              # Tipo entero (int)
flotante = 3.14          # Tipo flotante (float)
cadena = "Hola mundo"    # Tipo cadena (str)
booleano = True          # Tipo booleano (bool)

print("Variables declaradas:")
print("Entero:", entero)
print("Flotante:", flotante)
print("Cadena:", cadena)
print("Booleano:", booleano)
print("-" * 40)

# Convertir una cadena con valor numérico a entero y realizar una suma
cadena_num = "25"
numero = int(cadena_num) + 5  # Suma 25 + 5
print("Resultado de la suma (cadena '25' + 5):", numero)
print("-" * 40)

# Convertir una entrada de texto a número flotante, multiplicarla por 2 y mostrar el resultado
entrada = input("Ingresa un número decimal: ")  # Por ejemplo: 4.5
numero_flotante = float(entrada)
resultado = numero_flotante * 2
print("El resultado de multiplicarlo por 2 es:", resultado)
print("-" * 40)

# Función que verifica si un string se puede convertir a número
def es_convertible_a_numero(texto):
    try:
        float(texto)  # También funciona con enteros
        return True
    except ValueError:
        return False

# Probar la función con algunos valores
print("¿'123' se puede convertir a número?", es_convertible_a_numero("123"))
print("¿'3.14' se puede convertir a número?", es_convertible_a_numero("3.14"))
print("¿'hola' se puede convertir a número?", es_convertible_a_numero("hola"))
4.5
