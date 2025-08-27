# Programa que pregunta si desea continuar hasta que se escriba "No"

while True:
    respuesta = input("¿Desea continuar? (Si/No): ").strip().lower()
    if respuesta == "no":
        print("Programa finalizado.")
        break
    elif respuesta == "si":
        print("Continuamos...")
    else:
        print("Respuesta no válida, escriba 'Si' o 'No'.")
