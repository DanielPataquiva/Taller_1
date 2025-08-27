import numpy as np

# VECTORES
vector1 = np.array([2, 3, 4])
vector2 = np.array([5, 6, 7])
print ("Vector 1:", vector1)
print ("Vector 2:", vector2)

# SUMA
suma = vector1 + vector2
print("Suma:", suma)

# RESTA
resta = vector1 - vector2
print("Resta:", resta)

# MULTIPLICACION
multiplicacion = vector1 * vector2
print("Multiplicacion:", multiplicacion)

# DIVISION
division = np.divide(vector1, vector2, out=np.full_like(vector1, np.nan, dtype=float), where=vector2 != 0)
print("Division:", division)

# PRODUCTO PUNTO
producto_punto = np.dot(vector1, vector2)
print("Producto punto:", producto_punto)

# PRODUCTO CRUZ (solo válido para vectores de 3 elementos)
producto_cruz = np.cross(vector1, vector2)
print("Producto cruz:", producto_cruz)
