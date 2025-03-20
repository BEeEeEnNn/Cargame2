import pygame
import time
import math

def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)


FINISH = pygame.image.load("finish.png")
GCAR = scale_image(pygame.image.load("green-car.png"), 0.8)
BORDERS = pygame.image.load("Borders-Photoroom.png")
GRASS = scale_image(pygame.image.load("grass.jpg"), 2.5)
PCAR = scale_image(pygame.image.load("purple-car.png"), 0.8)
RCAR = scale_image(pygame.image.load("red-car.png"),0.8)
WCAR = scale_image(pygame.image.load("white-car.png"), 0.8)
TRACK = pygame.image.load("Track-Photoroom.png")


WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car go vroom vroom 3")

FPS = 60

def draw(win, images):
    for img, pos in images:
        win.blit(img, pos)

running = True
clock = pygame.time.Clock()
images = [(GRASS, (0,0)), (TRACK, (0,0))]

while running:


    clock.tick(FPS)

    draw(WIN, images)
    pygame.display.update()




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

pygame.quit()














































































