import math

def calcular_fuerzas(presion, diametro_piston, diametro_vastago):
    """
    Calcula la fuerza de avance y retroceso de un cilindro neumático de doble efecto.
    :param presion: presión de trabajo en Pascales (Pa)
    :param diametro_piston: diámetro del pistón en metros (m)
    :param diametro_vastago: diámetro del vástago en metros (m)
    :return: fuerzas de avance y retroceso en Newtons (N)
    """

    # Áreas
    area_piston = (math.pi * (diametro_piston ** 2)) / 4
    area_vastago = (math.pi * (diametro_vastago ** 2)) / 4

    # Fuerzas
    fuerza_avance = presion * area_piston
    fuerza_retroceso = presion * (area_piston - area_vastago)

    return fuerza_avance, fuerza_retroceso


if __name__ == "__main__":
    #print(" Calculo de Fuerza en Cilindro Neumatico de Doble Efecto ")

    # Ingreso de datos
    presion_bar = float(input("Ingrese la presión de trabajo [bar]: "))
    diametro_piston_mm = float(input("Ingrese el diámetro del pistón [mm]: "))
    diametro_vastago_mm = float(input("Ingrese el diámetro del vástago [mm]: "))

    # Conversión de unidades
    presion_pa = presion_bar * 1e5  # 1 bar = 100000 Pa
    diametro_piston_m = diametro_piston_mm / 1000
    diametro_vastago_m = diametro_vastago_mm / 1000

    # Calculo
    F_avance, F_retroceso = calcular_fuerzas(presion_pa, diametro_piston_m, diametro_vastago_m)

    # Resultados
    print(f"\nFuerza de avance: {F_avance:.2f} N")
    print(f"Fuerza de retroceso: {F_retroceso:.2f} N")
