# Programa que genera X números aleatorios en un rango

import random

print("Numeros Aleatorios")
cantidad = int(input("¿Cuántos numeros aleatorios desea generar?: "))
minimo = int(input("Ingrese el valor mínimo del rango: "))
maximo = int(input("Ingrese el valor máximo del rango: "))

print(f"\n{cantidad} numeros aleatorios en el rango [{minimo}, {maximo}]:")
for _ in range(cantidad):
    print(random.randint(minimo, maximo))
