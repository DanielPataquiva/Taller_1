import numpy as np

# MATRICES
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matriz A:\n", A)
print("Matriz B:\n", B)

# SUMA
suma = A + B
print("\nSuma:\n", suma)

# RESTA
resta = A - B
print("\nResta:\n", resta)

# MULTIPLICACION
multiplicacion = A * B
print("\nMultiplicacion:\n", multiplicacion)

#PRODDUCTO PUNTO
producto_punto = np.dot(A, B)
print("\nProducto punto:\n", producto_punto)

# DIVISON
division = np.divide(A, B, out=np.full_like(A, np.nan, dtype=float), where=B != 0)
print("\nDivision:\n", division)

# PRODUCTO CRUZ (solo válido si son vectores 1D de 3 elementos)
vec1 = A[0]
vec2 = B[0]
producto_cruz = np.cross(vec1, vec2)
print("\nProducto cruz:\n", producto_cruz)

