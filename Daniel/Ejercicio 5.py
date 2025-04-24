#Pide al usuario su edad y si tiene licencia de conducción. Solo si ambas condiciones se cumplen, imprime que puede conducir.

edad = int (input("Escribe tu edad =>"))
licencia = input("¿Tienes licencia de conducir? (si/no)").strip().lower()

if edad >= 18 and licencia == 'si':
    print("Puedes conducir")
else:
    print("No puedes conducir")

#Solicita si una persona tiene experiencia laboral y título universitario. Usa operadores lógicos para decidir si puede aplicar a una oferta de trabajo.

experiencia = input("¿Tienes experiencia laboral? (si/no)").strip().lower()
titulo = input("¿Tienes titulo universitario? (si/no)").strip().lower()

if experiencia == 'si' and titulo == 'si':
    print("Puedes aplicar a la ofeta de trabajo")
else:
    print("No puedes aplicar a la ofeta de trabajo")

#Dado un número, determina si está en el rango de 10 a 50 (inclusive).

num = int(input("Escribe un numero"))

if 10 <= num <= 50:
    print(f"{num} está en el rango esperado.")
else:
    print(f"{num} no está en el rango esperado.")
