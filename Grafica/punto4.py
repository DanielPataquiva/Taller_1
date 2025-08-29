import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Ingreso de coordenadas del vector
x = float(input("Ingrese la coordenada X del vector: "))
y = float(input("Ingrese la coordenada Y del vector: "))
z = float(input("Ingrese la coordenada Z del vector: "))

# Crear figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujo de ejes
ax.quiver(0, 0, 0, x, y, z, color='r', arrow_length_ratio=0.1, linewidth=2)

# Configuración de ejes
ax.set_xlim([0, max(1, x+1)])
ax.set_ylim([0, max(1, y+1)])
ax.set_zlim([0, max(1, z+1)])

ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
ax.set_title('Vector en sistema de coordenadas 3D')

plt.show()