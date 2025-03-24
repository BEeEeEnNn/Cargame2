import pygame
import time
import math


def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft = top_left).center)
    win.blit(rotated_image, new_rect.topleft)

#Alle Bilder importiert
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

class AbstractCar:

    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win, ):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)


class PlayerCar(AbstractCar):
    IMG = RCAR
    START_POS = (180, 200)





def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)
    player_car.draw(win)
    pygame.display.update()

running = True
clock = pygame.time.Clock()
images = [(GRASS, (0,0)), (TRACK, (0,0))]
player_car = PlayerCar(4, 4)

while running:


    clock.tick(FPS)

    draw(WIN, images, player_car)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

pygame.quit()














































































