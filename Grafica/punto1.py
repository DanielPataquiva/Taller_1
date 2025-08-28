#se recomineda instalar al entorno de python la libreria de matplotlib,
#para que el codigo pueda ejecutarce correctamente y relaizar las graficas solicitadas.
# una manera de instalar la version adecuada y facil de matplotlib es con 
# el comando python -m pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np



def pt100_resistencia(temperatura):
    
    if temperatura < 0:
        R0 = 100.0
        A = 3.9083e-3
        B = -5.775e-7
        C = -4.183e-12
        return R0 * (1 + A * temperatura + B * temperatura**2 + C * (temperatura - 100) * temperatura**3)
    else:
        R0 = 100.0
        A = 3.9083e-3
        B = -5.775e-7
        return R0 * (1 + A * temperatura + B * temperatura**2)

temperaturas = np.linspace(-200, 200, 1000)
resistencias = [pt100_resistencia(temp) for temp in temperaturas]

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(temperaturas, resistencias, 'b-', linewidth=2, label='PT100')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Resistencia (Ω)')
plt.title('Comportamiento del Sensor PT100 (-200°C a 200°C)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

