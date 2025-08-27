# Programa que describe tipos de robots y sus articulaciones

print("Tipos de Robots")
print("1. Robot Cilíndrico")
print("2. Robot Cartesiano")
print("3. Robot Esférico")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    print("Robot Cilíndrico → 2 articulaciones prismáticas y 1 rotacional")
elif opcion == 2:
    print("Robot Cartesiano → 3 articulaciones prismáticas")
elif opcion == 3:
    print("Robot Esférico → 2 articulaciones rotacionales y 1 prismática")
else:
    print("Opción inválida")
