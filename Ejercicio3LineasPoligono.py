import pygame
import math

pygame.init()
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
reloj = pygame.time.Clock()
FONDO = (241, 238, 238)
LINEAS = (96, 249, 14)
centro_x = ancho // 2
centro_y = alto // 2
radio = 300
num_lados = 6
angulo = 2 * math.pi / num_lados
vertices = []
for i in range(num_lados):
    x = centro_x + radio * math.cos(i * angulo)
    y = centro_y + radio * math.sin(i * angulo)
    vertices.append((x, y))
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    pantalla.fill(FONDO)
    pygame.draw.polygon(pantalla, LINEAS, vertices, 2)
    for i in range(num_lados):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 3) % num_lados] 
        pygame.draw.line(pantalla, LINEAS, (x1, y1), (x2, y2), 2)

    pygame.display.flip()
    reloj.tick(60)
pygame.quit()
