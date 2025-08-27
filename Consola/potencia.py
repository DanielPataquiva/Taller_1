# Programa que calcula la potencia consumida en un circuito

print("Cálculo de Potencia")
corriente = float(input("Ingrese la corriente (A): "))
voltaje = float(input("Ingrese el voltaje (V): "))
potencia = corriente * voltaje
print(f"La potencia consumida es: {potencia:.2f} W")
