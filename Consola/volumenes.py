# Programa para cálculo de volúmenes de sólidos geométricos

import math

print("Cálculo de Volúmenes")
print("1. Prisma rectangular")
print("2. Pirámide")
print("3. Cono truncado")
print("4. Cilindro")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    base = float(input("Ingrese el área de la base: "))
    altura = float(input("Ingrese la altura: "))
    volumen = base * altura
    print(f"El volumen del prisma es: {volumen:.3f}")

elif opcion == 2:
    base = float(input("Ingrese el área de la base: "))
    altura = float(input("Ingrese la altura: "))
    volumen = (base * altura) / 3
    print(f"El volumen de la pirámide es: {volumen:.2f}")

elif opcion == 3:
    r1 = float(input("Ingrese el radio mayor: "))
    r2 = float(input("Ingrese el radio menor: "))
    h = float(input("Ingrese la altura: "))
    volumen = (math.pi * h / 3) * (r1**2 + r2**2 + r1*r2)
    print(f"El volumen del cono truncado es: {volumen:.2f}")

elif opcion == 4:
    r = float(input("Ingrese el radio: "))
    h = float(input("Ingrese la altura: "))
    volumen = math.pi * r**2 * h
    print(f"El volumen del cilindro es: {volumen:.2f}")

else:
    print("Opción inválida")
