import pygame
pygame.init()

pantalla = pygame.display.set_mode((500, 350))
pygame.display.set_caption("Ejercicio Pygame")

pantalla.fill((135, 206, 235))
pygame.draw.rect(pantalla, (34, 139, 34), (0, 280, 500, 70))
pygame.draw.rect(pantalla, (220, 50, 50), (60, 230, 40, 50))
pygame.draw.circle(pantalla, (255, 215, 0), (180, 210), 15)
pygame.draw.circle(pantalla, (255, 215, 0), (250, 210), 15)
pygame.draw.circle(pantalla, (255, 215, 0), (320, 210), 15)
fuente = pygame.font.SysFont("Arial", 26, bold=True)
texto = fuente.render("Puntos: 300", True, (255, 255, 255))
pantalla.blit(texto, (20, 15))
pygame.display.flip()
pygame.image.save(pantalla, "captura_pygame.png")
pygame.quit()
