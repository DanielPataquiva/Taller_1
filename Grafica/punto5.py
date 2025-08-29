import matplotlib.pyplot as plt
from matplotlib.text import TextPath
from matplotlib.patches import PathPatch
from matplotlib.font_manager import FontProperties


nombres = ["ANDRES", "DANIEL", "DAVID", "SEBASTIAN"]


nombre = [nombre[::1] for nombre in nombres]

font = FontProperties(family="DejaVu Sans", weight="bold")
font_size = 120
row_spacing = 1.2
stroke_width = 1.5

fig, ax = plt.subplots(figsize=(12, 6))

for row_idx, nombre in enumerate(nombre):
    tp = TextPath((0, -row_idx * row_spacing * font_size), nombre, size=font_size, prop=font)
    patch = PathPatch(tp, facecolor="none", edgecolor="black", linewidth=stroke_width)
    ax.add_patch(patch)

ax.set_xlim(0, max(len(n) for n in nombres) * font_size * 0.7)
ax.set_ylim(-len(nombres) * row_spacing * font_size - 50, font_size + 50)
ax.set_aspect("equal")
ax.axis("off")
#ax.set_title("Nombres grupo", pad=14)

plt.tight_layout()
plt.show()
