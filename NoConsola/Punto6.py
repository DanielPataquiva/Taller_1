import math

def calcular_fuerzas(presion, diametro_piston, diametro_vastago):
   
    # AREAS
    area_piston = (math.pi * (diametro_piston ** 2)) / 4
    area_vastago = (math.pi * (diametro_vastago ** 2)) / 4

    # FUERZAS
    fuerza_avance = presion * area_piston
    fuerza_retroceso = presion * (area_piston - area_vastago)

    return fuerza_avance, fuerza_retroceso


if __name__ == "__main__":

    # Ingreso de datos
    presion_bar = 87
    print("Presion de trabajo [bar]: ", presion_bar)
    diametro_piston_mm = 22
    print("Ingrese el diametro del piston [mm]: ", diametro_piston_mm)
    diametro_vastago_mm = 36
    print("Ingrese el diametro del vástago [mm]: ", diametro_vastago_mm)

    # Conversión de unidades
    presion_pa = presion_bar * 1e5  # 1 bar = 100000 Pa
    diametro_piston_m = diametro_piston_mm / 1000
    diametro_vastago_m = diametro_vastago_mm / 1000

    # Calculo
    F_avance, F_retroceso = calcular_fuerzas(presion_pa, diametro_piston_m, diametro_vastago_m)

    print(f"\nFuerza de avance: {F_avance:.2f} N")
    print(f"Fuerza de retroceso: {F_retroceso:.2f} N")
