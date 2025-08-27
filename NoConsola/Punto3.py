import math

# INGRESO DE COORDENADAS RECTANGULARES
x = 2
y = 3
z = 5
print("Coordenada X= ",x)
print("Coordenada Y= ",y)
print("Coordenada Z= ",z)

# CONVERSION A COORDENADAS CILINDRICAS 
rho = math.sqrt(x**2 + y**2)         # distancia radial
phi = math.atan2(y, x)               # angulo azimutal (maneja bien los cuadrantes)
z_cil = z                            # z se mantiene igual

# CONVERSION A COORDENADAS ESFERICAS
r = math.sqrt(x**2 + y**2 + z**2)    # distancia al origen
theta = math.acos(z / r) if r != 0 else 0   # angulo polar (con el eje z)
phi_esf = phi                        # mismo angulo 


print("\n--- Coordenadas Cilindricas ---")
print(f"ρ (rho) = {rho:.4f}")
print(f"φ (phi) = {math.degrees(phi):.4f}°")
print(f"z = {z_cil:.4f}")

print("\n--- Coordenadas Esfericas ---")
print(f"r = {r:.4f}")
print(f"θ (theta) = {math.degrees(theta):.4f}°")
print(f"φ (phi) = {math.degrees(phi_esf):.4f}°")
