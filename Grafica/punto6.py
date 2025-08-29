import cv2
import numpy as np

def obtener_contornos(ruta_imagen):
   
    img = cv2.imread(ruta_imagen)
    if img is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {ruta_imagen}")

   
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

  
    edges = cv2.Canny(blur, 50, 150)

  
    contornos, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

   
    coords = []
    for cnt in contornos:
        for punto in cnt:
            x, y = punto[0]
            coords.append((x, y))

    return coords, img, contornos


logo1 = "chevrolet.png"
logo2 = "hyundai.jpg"


coords1, img1, contornos1 = obtener_contornos(logo1)
coords2, img2, contornos2 = obtener_contornos(logo2)


print("Coordenadas contornos Logo 1 (Chevrolet):")
print(coords1[:50]) 

print("\nCoordenadas contornos Logo 2 (Hyundai):")
print(coords2[:50])


cv2.drawContours(img1, contornos1, -1, (0,255,0), 2)
cv2.drawContours(img2, contornos2, -1, (0,255,0), 2)

cv2.imshow("Contornos Chevrolet", img1)
cv2.imshow("Contornos Hyundai", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
