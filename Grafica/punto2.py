#para este punto ademas de la libreria usada en el punto uno para graficar, debido a su mayor complejidad
#debemos ultilizar la libreria scipy la cual extiende a numpy y nos ayuda a trabjar mejor
#temas matematicos, ciencias e ingenieria, se recomeinda instalar la libreia
#con el comando python -m pip install scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

print("ANÁLISIS DE SISTEMAS DE SEGUNDO ORDEN")
print("=" * 40)

print("\nIngrese los coeficientes de la función de transferencia:")
print("Formato: H(s) = K / (s² + a*s + b)")

K = float(input("Ganancia K: "))
a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))

omega_n = np.sqrt(b)
zeta = a / (2 * omega_n)

print(f"\nParámetros calculados:")
print(f"Frecuencia natural (ωn) = {omega_n:.3f}")
print(f"Coeficiente de amortiguamiento (ζ) = {zeta:.3f}")

if zeta == 0:
    tipo = "NO AMORTIGUADO"
    color = "blue"
elif 0 < zeta < 1:
    tipo = "SUBAMORTIGUADO"
    color = "green"
elif zeta == 1:
    tipo = "CRÍTICAMENTE AMORTIGUADO"
    color = "orange"
else:
    tipo = "SOBREAMORTIGUADO"
    color = "red"

print(f"\n🔹 SISTEMA: {tipo}")

num = [K]
den = [1, a, b]
sys = signal.TransferFunction(num, den)

t = np.linspace(0, 10, 500)
t, y = signal.step(sys, T=t)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(t, y, color=color, linewidth=2, label=f'Sistema {tipo.lower()}')
plt.axhline(y=K, color='black', linestyle='--', alpha=0.7, label='Valor final')

plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title(f'Respuesta al Escalón\nH(s) = {K}/(s² + {a}s + {b})')
plt.grid(True, alpha=0.3)
plt.legend()

# Mostrar información en la gráfica
textstr = f'ωn = {omega_n:.2f}\nζ = {zeta:.2f}\nTipo: {tipo}'
plt.text(0.7, 0.2, textstr, transform=plt.gca().transAxes, fontsize=10,
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
plt.show()

print(f"\nInformación adicional:")
print(f"Polos del sistema: {np.roots(den)}")
if zeta > 0:
    print(f"Tiempo aproximado de establecimiento: {4/(zeta*omega_n):.2f} s")