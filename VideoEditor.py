import pygame
from PIL import Image
import numpy as np
import cv2

density = ' _.,-=+:;cba!?0123456789$W#@Ñ'
invDensity = 'Ñ@#W$9876543210?!cba;:+=-,._ '

mode = input("Modo oscuro o claro? (O/C)")
while mode not in ["O","C"]:
    mode = input("Error. Modo oscuro o claro? (O/C)")
camera = cv2.VideoCapture(0)


# Inicializar Pygame
pygame.init()
pygame.font.init()

# Definir el tamaño de la ventana
width = 400
height = 400
window_size = (width, height)
window = pygame.display.set_mode(window_size)

# Crear una superficie para dibujar
surface = pygame.Surface((48, 48))

# Bucle principal del juego
running = True
while running:

    window.fill((0, 0, 0))

    # Capturar una imagen
    ret, frame = camera.read()

    # Verificar si la captura fue exitosa
    if not ret:
        print("Error")

    # Cambiar la resolución
    resized_frame = cv2.resize(frame, (48, 48))

    resized_array = np.array(resized_frame)
    
    # Actualizar la ventana de Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiar la superficie
    surface.fill((0, 0, 0))

    # Dibujar los cuadrados con los valores de r, g, b
    i=0
    row=0
    for rows in resized_array:
        pixel=0
        for pixels in rows:
            x = i % 48
            y = i // 48
            r=int(resized_array[row][pixel][0])
            g=int(resized_array[row][pixel][1])
            b=int(resized_array[row][pixel][2])
            color = ((r + g + b) // 3)
            color = (color*len(density))// 255
            if mode == "O":
                text = density[color]
            else:
                text = invDensity[color]
            font = pygame.font.Font(pygame.font.get_default_font(), 8)
            text_surface = font.render(text, True, (255,255,255))
            window.blit(text_surface, (x * 8, y * 8))
            i+=1
            pixel+=1
        row+=1
    # Actualizar la ventana
    pygame.display.update()

# Salir del programa
camera.release()
pygame.quit()







