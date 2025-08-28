import numpy as np
import matplotlib.pyplot as plt

def circuito_rc():
    print("=== SIMULACIÓN DE CIRCUITO RC ===")
    
    try:
        V = float(input("Ingrese el voltaje (V): "))
        C = float(input("Ingrese la capacitancia (μF): ")) * 1e-6 
        R = float(input("Ingrese la resistencia (Ω): "))
        tau = R * C
        print(f"\nConstante de tiempo (τ): {tau:.6f} segundos")
        t = np.linspace(0, 5*tau, 1000)
        
        # Ecuación de carga: Vc = V * (1 - e^(-t/RC))
        Vc_carga = V * (1 - np.exp(-t/(R*C)))
        
        # Ecuación de descarga: Vc = V * e^(-t/RC)
        Vc_descarga = V * np.exp(-t/(R*C))
        
        plt.figure(figsize=(12, 6))
        
        # Gráfica de carga
        plt.subplot(1, 2, 1)
        plt.plot(t, Vc_carga, 'b-', linewidth=2, label='Carga del capacitor')
        plt.axhline(y=V, color='r', linestyle='--', alpha=0.7, label=f'Voltaje máximo ({V} V)')
        plt.axvline(x=tau, color='g', linestyle='--', alpha=0.7, label=f'τ = {tau:.4f} s')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Voltaje en el capacitor (V)')
        plt.title('CARGA del Capacitor')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # Gráfica de descarga
        plt.subplot(1, 2, 2)
        plt.plot(t, Vc_descarga, 'r-', linewidth=2, label='Descarga del capacitor')
        plt.axhline(y=0, color='b', linestyle='--', alpha=0.7, label='Voltaje cero')
        plt.axvline(x=tau, color='g', linestyle='--', alpha=0.7, label=f'τ = {tau:.4f} s')
        plt.xlabel('Tiempo (s)')
        plt.ylabel('Voltaje en el capacitor (V)')
        plt.title('DESCARGA del Capacitor')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        plt.tight_layout()
        plt.show()
        
        print("\n=== INFORMACIÓN ADICIONAL ===")
        print(f"Tiempo para alcanzar 63.2% del voltaje máximo: {tau:.6f} s")
        print(f"Tiempo para alcanzar 95% del voltaje máximo: {3*tau:.6f} s")
        print(f"Tiempo para alcanzar 99.3% del voltaje máximo: {5*tau:.6f} s")
        
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    circuito_rc()