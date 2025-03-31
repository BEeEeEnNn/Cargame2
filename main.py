import pygame, time, math, sys, random

pygame.init()



def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)
    return new_rect.topleft

# Startbildschirm-Funktion
def start_screen():
    font = pygame.font.SysFont(None, 100)
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT// 2 - 30, 200, 60)
    x = WIDTH


    while True:
        WIN.fill((144, 238, 144))
        WIN.blit(Startbildschirm, (0, 0))
        WIN.blit(Startbildschirm_Auto, (-x , 220))
        WIN.blit(Startbildschirm_AutoBlau, (-x *1.1, 350))
        x += -5
        draw_text("Car Go Vroom Vroom 3", font, (0, 0, 0), WIN, WIDTH // 2, HEIGHT // 4)

        pygame.draw.rect(WIN, (0, 200, 0), button_rect)
        draw_text("Start", pygame.font.SysFont(None, 40), (255, 255, 255), WIN, WIDTH // 2, HEIGHT // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return

        pygame.display.flip()


def end_screen():
    font = pygame.font.SysFont(None, 100)
    button_restart = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 30, 300, 60)
    button_exit = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 60)

    while True:
        WIN.fill((144, 238, 144))  # Schwarzer Hintergrund
        draw_text(player, font, (255, 255, 255), WIN, WIDTH// 2, HEIGHT // 4)

        # Buttons zeichnen
        pygame.draw.rect(WIN, (0, 200, 0), button_restart)
        pygame.draw.rect(WIN, (200, 0, 0), button_exit)
        draw_text("Neustart", pygame.font.SysFont(None, 40), (255, 255, 255), WIN, WIDTH // 2, HEIGHT // 2)
        draw_text("Beenden", pygame.font.SysFont(None, 40), (255, 255, 255), WIN, WIDTH // 2, HEIGHT // 2 + 80)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_restart.collidepoint(event.pos):
                    return  # Spiel wird neugestartet
                if button_exit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def draw_lap_count(win, lap_count):
    font = pygame.font.SysFont(None, 50)  # Schriftart mit Größe 40
    text = f"Runde: {lap_count+1}""/3" # Text der Runde
    # Zeichne den Text an einer gut sichtbaren Position (z.B. oben links)
    draw_text(text, font, (255, 0, 0), win, 2000 // 2, 50)  # Weißer Text bei Position (Mitte oben)

def draw_lap_count2(win, lap_count2):
    font = pygame.font.SysFont(None, 50)  # Schriftart mit Größe 40
    text = f"Runde: {lap_count2+1}""/3"  # Text der Runde
    # Zeichne den Text an einer gut sichtbaren Position (z.B. oben links)
    draw_text(text, font, (0, 255, 0), win, 200 // 2, 50)  # Weißer Text bei Position (Mitte oben)

# Alle Bilder importiert
FINISH = scale_image(pygame.image.load("Sprites/finish.png"), 1.08)
FINISH_POSITION = (99, 325)
FINISH_MASK = pygame.mask.from_surface(FINISH)

GCAR = scale_image(pygame.image.load("Sprites/green-car.png"), 0.5)
BORDERS = pygame.image.load("Sprites/Borders-Photoroom.png")
GRASS = scale_image(pygame.image.load("Sprites/Hintergrund.png"), 1)
PCAR = scale_image(pygame.image.load("Sprites/purple-car.png"), 0.8)
RCAR = scale_image(pygame.image.load("Sprites/red-car.png"), 0.5)
WCAR = scale_image(pygame.image.load("Sprites/white-car.png"), 0.8)
TRACK = pygame.image.load("Sprites/Track-Photoroom.png")
Startbildschirm = pygame.image.load("Sprites/Startbildschirm.png")
Startbildschirm.set_colorkey((0,0,0))
Startbildschirm_Auto = pygame.image.load("Sprites/Startbildschirm_Auto-fotor-bg-remover-20250326134022.png")
Startbildschirm_AutoBlau = pygame.image.load("Sprites/Startbildschirm_AutoBlau-fotor-bg-remover-2025032614154.png")

TRACK_BORDER_MASK = pygame.mask.from_surface(BORDERS)

WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car go vroom vroom 3")
finish_timer = 0
finish_timer2 = 0
colliding_with_finish = False
colliding_with_finish_2 = False



FPS = 60

last_time = time.time()

can_collide = True
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

    def rotate(self,delta_time : float, left=False, right=False):
        if left:
            self.angle += self.rotation_vel * delta_time
        elif right:
            self.angle -= self.rotation_vel * delta_time

    def get_mask(self):
        rotated_image = pygame.transform.rotate(self.img, self.angle)
        return pygame.mask.from_surface(rotated_image)

    def draw(self, win):
        self.tleft = blit_rotate_center(win, self.img, (self.x, self.y), self.angle)
        


    pygame.display.update()

    def move_forward(self, delta_time):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move(delta_time)

    def move_backward(self, delta_time):
        self.vel = max(self.vel - self.acceleration, -self.max_vel / 2)
        self.move(delta_time)

    def move(self, delta_time):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        

        self.y -= vertical * delta_time
        self.x -= horizontal * delta_time
        

    def reduce_speed(self, delta_time):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move(delta_time)

    def collide(self, mask, x=0, y=0):
        car_mask = self.get_mask()
        offset = (int(self.tleft[0] - x), int(self.tleft[1] - y))
        point_of_intersection = mask.overlap(car_mask, offset)
        return point_of_intersection

    def reset(self):
        self.x, self.y = self.START_POS
        self.angle = 0
        self.vel = 0

class PlayerCar(AbstractCar):
    IMG = RCAR
    START_POS = (170, 270)

    def __init__(self, max_vel, rotation_vel):
        super().__init__(max_vel, rotation_vel)
        self.last_collision_time = 0

    def handle_collision(self, mask, delta_time):
        if time.time() - self.last_collision_time > 0.1:
            collision_point = self.collide(mask)
            if collision_point:
                self.bounce(delta_time)
                self.last_collision_time = time.time()

    def reduce_speed(self, delta_time):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move(delta_time)

    def bounce(self, delta_time):
        self.vel = -self.vel / 1.5
        self.move(delta_time)

    def car_bounce(self, delta_time):
            self.vel = -self.vel / 3
            self.move(delta_time)


class PlayerCar2(AbstractCar):
    IMG = GCAR
    START_POS = (110, 270)

    def __init__(self, max_vel, rotation_vel):
            super().__init__(max_vel, rotation_vel)
            self.last_collision_time = 0

    def handle_collision(self, mask, delta_time):
            if time.time() - self.last_collision_time > 0.1:
                collision_point = self.collide(mask)
                if collision_point:
                    self.bounce(delta_time)
                    self.last_collision_time = time.time()

    def reduce_speed(self, delta_time):
            self.vel = max(self.vel - self.acceleration / 2, 0)
            self.move(delta_time)

    def bounce(self, delta_time):
            self.vel = -self.vel / 1.5
            self.move(delta_time)

    def car_bounce(self, delta_time):
            self.vel = -self.vel / 1.5
            self.move(delta_time)



def draw(win, images, player_car, player_car2):
    for img, pos in images:
        win.blit(img, pos)
    player_car.draw(win)
    player_car2.draw(win)
    draw_lap_count(win, lap_count)
    draw_lap_count2(win, lap_count2)
    pygame.display.update()

running = True
clock = pygame.time.Clock()
images = [(GRASS, (0, 0)), (TRACK, (0, 0)), (FINISH, FINISH_POSITION), (BORDERS, (0, 0))]
player_car = PlayerCar(4, 2)
player_car2 = PlayerCar2(4, 2)

start_screen()

lap_count = 0
lap_count2 = 0

while running:

    delta_time = time.time() - last_time
    delta_time *= 60
    last_time = time.time()


    draw(WIN, images, player_car, player_car2)

    draw_lap_count(WIN, lap_count)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    keys = pygame.key.get_pressed()

    moved = False
    if keys[pygame.K_LEFT]:
        player_car.rotate(delta_time, left=True)
    if keys[pygame.K_RIGHT]:
        player_car.rotate(delta_time, right=True)
    if keys[pygame.K_UP]:
        moved = True
        player_car.move_forward(delta_time)
    elif keys[pygame.K_DOWN]:
        moved = True
        player_car.move_backward(delta_time)
    if not moved:
        player_car.reduce_speed(delta_time)

    moved2 = False
    if keys[pygame.K_a]:
        player_car2.rotate(delta_time, left=True)
    if keys[pygame.K_d]:
        player_car2.rotate(delta_time, right=True)
    if keys[pygame.K_w]:
        moved2 = True
        player_car2.move_forward(delta_time)
    elif keys[pygame.K_s]:
        moved2 = True
        player_car2.move_backward(delta_time)

    if not moved2:
        player_car2.reduce_speed(delta_time)

    if player_car.collide(player_car2.get_mask(), player_car2.x, player_car2.y):
        player_car2.car_bounce(delta_time)
    if player_car2.collide(player_car.get_mask(), player_car.x, player_car.y):
        player_car.car_bounce(delta_time)

    player_car.handle_collision(TRACK_BORDER_MASK, delta_time)

    finish_point_of_collision = player_car.collide(FINISH_MASK, *FINISH_POSITION)
    if finish_point_of_collision != None and colliding_with_finish == False:
        if finish_point_of_collision[1] == 0:
            player_car.reset()
        else:
            colliding_with_finish = True
            lap_count += 1
            finish_timer = time.time()

    if colliding_with_finish:
        if time.time() - finish_timer > 3:
            colliding_with_finish = False
            finish_timer = 0
    if lap_count == 3:
        player = "Spieler 1 gewinnt"
        end_screen()
        player_car.reset()
        player_car2.reset()
        lap_count = 0
        lap_count2 = 0

    player_car2.handle_collision(TRACK_BORDER_MASK, delta_time)

    finish_point_of_collision = player_car2.collide(FINISH_MASK, *FINISH_POSITION)
    if finish_point_of_collision != None and colliding_with_finish_2 == False:
        if finish_point_of_collision[1] == 0:
            player_car2.reset()
        else:
            colliding_with_finish_2 = True
            lap_count2 += 1
            finish_timer2 = time.time()
            print("I_work")

    if colliding_with_finish_2:
        if time.time() - finish_timer2 > 3:
            colliding_with_finish_2 = False
            finish_timer2 = 0
    if lap_count2 == 3:
        player = "Spieler 2 gewinnt"
        end_screen()
        player_car.reset()
        player_car2.reset()
        lap_count = 0
        lap_count2 = 0


    clock.tick(FPS)

pygame.quit()
