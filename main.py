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
    return new_rect.topleft

#Alle Bilder importiert
FINISH = scale_image(pygame.image.load("Sprites/finish.png"),1.08)
FINISH_POSITION = (99, 325)
FINISH_MASK = pygame.mask.from_surface(FINISH)

GCAR = scale_image(pygame.image.load("Sprites/green-car.png"), 0.8)
BORDERS = pygame.image.load("Sprites/Borders-Photoroom.png")
GRASS = scale_image(pygame.image.load("Sprites/grass.jpg"), 2.5)
PCAR = scale_image(pygame.image.load("Sprites/purple-car.png"), 0.8)
RCAR = scale_image(pygame.image.load("Sprites/red-car.png"), 0.7)
WCAR = scale_image(pygame.image.load("Sprites/white-car.png"), 0.8)
TRACK = pygame.image.load("Sprites/Track-Photoroom.png")

TRACK_BORDER_MASK = pygame.mask.from_surface(BORDERS)

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
        self.acceleration = 0.1
        self.tleft = (0, 0)

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

#ChatGPT
    def get_mask(self):
        rotated_image = pygame.transform.rotate(self.img, self.angle)
        #pygame.transform.scale_by(rotated_image, 1.1)
        #new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=top_left).center)
        return pygame.mask.from_surface(rotated_image)


    def draw(self, win, ):
        self.tleft = blit_rotate_center(win, self.img, (self.x, self.y), self.angle)
        # DEBUG: Kollisionmaske des Autos zeichnen
        car_mask_surface = self.get_mask().to_surface(setcolor=(255, 0, 0, 100), unsetcolor=(0, 0, 0, 0))
        win.blit(car_mask_surface, (self.x, self.y))

    pygame.display.update()

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()


    def move_backward(self):
        self.vel = max(self.vel - self.acceleration, -self.max_vel/2)
        self.move()


    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal


    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration/2, 0)
        self.move()


    def collide(self, mask, x=0, y=0):
        car_mask = self.get_mask() #ChatGPT
        offset = (int(self.tleft[0] -x), int(self.tleft[1] - y))
        point_of_intersection = mask.overlap(car_mask, offset)
        print(point_of_intersection)
        return point_of_intersection


    def reset(self):
        self.x, self.y = self.START_POS
        self.angle = 0
        self.vel = 0


class PlayerCar(AbstractCar):
    IMG = RCAR
    START_POS = (142, 270)

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration/2, 0)
        self.move()

    def bounce(self):
        self.vel = - self.vel/1.5
        self.move()

def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)
    player_car.draw(win)
    pygame.display.update()

running = True
clock = pygame.time.Clock()
images = [(GRASS, (0,0)), (TRACK, (0,0)), (FINISH, FINISH_POSITION), (BORDERS, (0,0))]
player_car = PlayerCar(4, 2)

while running:

    clock.tick(FPS)

    draw(WIN, images, player_car)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    keys = pygame.key.get_pressed()

    moved = False
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player_car.rotate(left=True)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player_car.rotate(right=True)
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if not keys[pygame.K_s] and not keys[pygame.K_SPACE]:  # Prüft, ob S nicht gedrückt wird
            moved = True
            player_car.move_forward()
    elif keys[pygame.K_s] or keys[pygame.K_SPACE]:  # Benutze elif, um zu verhindern, dass beide aktiv sind
        moved = True
        player_car.move_backward()

    if not moved:
        player_car.reduce_speed()

    if player_car.collide(TRACK_BORDER_MASK) != None:
        player_car.bounce()

    finish_point_of_collision = player_car.collide(FINISH_MASK, *FINISH_POSITION)
    if finish_point_of_collision != None:
        if finish_point_of_collision[1] == 0:
            player_car.bounce()
        else:
            player_car.reset()



pygame.quit()














































































