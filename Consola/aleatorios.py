# Programa que genera X números aleatorios en un rango

import random

print("\n--- Números Aleatorios ---")
cantidad = int(input("¿Cuántos números aleatorios desea generar?: "))
minimo = int(input("Ingrese el valor mínimo del rango: "))
maximo = int(input("Ingrese el valor máximo del rango: "))

print(f"\n{cantidad} números aleatorios en el rango [{minimo}, {maximo}]:")
for _ in range(cantidad):
    print(random.randint(minimo, maximo))
