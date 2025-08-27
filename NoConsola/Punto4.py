
def resistencia_pt100(T):
    
    R0 = 100  # ohmios a 0 °C
    A = 3.9083e-3
    B = -5.775e-7
    C = -4.183e-12  # solo válido para T < 0°C

    if T >= 0:
        R = R0 * (1 + A*T + B*(T**2))
    else:
        R = R0 * (1 + A*T + B*(T**2) + C*(T-100)*(T**3))
    return R

if __name__ == "__main__":
# Programa principal
    temperatura = 110
    print("Temperatura en °C: ", temperatura)
    resistencia = resistencia_pt100(temperatura)
    print(f"La resistencia de la PT100 a {temperatura} °C es: {resistencia:.2f} Ω")
