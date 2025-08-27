import numpy as np

def rotacion_x(angulo_grados):
    theta = np.radians(angulo_grados)
    R = np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])
    return np.round(R, 4)  # redondear a 4 decimales

def rotacion_y(angulo_grados):
    theta = np.radians(angulo_grados)
    R = np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])
    return np.round(R, 4)

def rotacion_z(angulo_grados):
    theta = np.radians(angulo_grados)
    R = np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])
    return np.round(R, 4)


if __name__ == "__main__":
    angulo = float(input("Ingrese el ángulo en grados: "))

    print("\nMatriz de rotación en X:")
    print(rotacion_x(angulo))

    print("\nMatriz de rotación en Y:")
    print(rotacion_y(angulo))

    print("\nMatriz de rotación en Z:")
    print(rotacion_z(angulo))
