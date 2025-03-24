import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animación Interactiva - Pygame")

# Colores y figuras
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
shapes = [{"rect": pygame.Rect(random.randint(100, 700), random.randint(100, 500), 80, 80), "color": random.choice(colors)} for _ in range(3)]

# Variables de control
running = True
dragging = None

# Bucle principal
while running:
    screen.fill((255, 255, 255))  # Fondo blanco
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detectar clic en una figura
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for shape in shapes:
                if shape["rect"].collidepoint(event.pos):
                    shape["color"] = random.choice(colors)  # Cambiar color
                    dragging = shape  # Mover figura

        # Soltar figura
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = None

        # Mover figura
        elif event.type == pygame.MOUSEMOTION and dragging:
            dragging["rect"].move_ip(event.rel)

    # Dibujar las figuras
    for shape in shapes:
        pygame.draw.rect(screen, shape["color"], shape["rect"])

    pygame.display.flip()  # Actualizar pantalla

pygame.quit()
