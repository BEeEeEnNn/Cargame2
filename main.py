import os

import pygame, time, math, sys, random

pygame.init()


#Alles mit "delta time": https://www.youtube.com/watch?v=OmkAUzvwsDk

single_timer = 0

#Videoserie:Pygame Car Racing Tutorial
def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft) #Fehlerbehebung Maske
    return new_rect.topleft

#ChatGPT/selber bearbeitet
def start_screen():
    font = pygame.font.SysFont(None, 100)
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT// 2 - 30, 200, 60)
    x = WIDTH

    while True:
        WIN.fill((144, 238, 144))
        WIN.blit(Startbildschirm, (0, 0))
        WIN.blit(Startbildschirm_Auto, (-x, 220)) #Selbst gemacht (Auto)
        WIN.blit(Startbildschirm_AutoBlau, (-x * 1.1, 350)) #Selbst gemacht (Auto)
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

def single_player_screen():
    font = pygame.font.SysFont(None, 100)
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 30, 200, 60)

    while True:
        WIN.fill((144, 238, 144)) # Grüner Hintergrund

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            sys.exit()
            if keys[pygame.K_BACKSPACE]:
                options_screen()  # Zurück zu Hauptmenü
                return
        pygame.display.flip()
#selber
def options_screen():
    font = pygame.font.SysFont(None, 100)
    button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 30, 200, 60)


    while True:
        WIN.fill((144, 238, 144))
        WIN.blit(Startbildschirm, (0, 0))
        button_single = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 30, 300, 60)
        button_multi = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 60)

        draw_text("Car Go Vroom Vroom 3", font, (0, 0, 0), WIN, WIDTH // 2, HEIGHT // 4)

        pygame.draw.rect(WIN, (0, 200, 0), button_single)
        pygame.draw.rect(WIN, (0, 200, 0), button_multi)
        draw_text("1 Spieler", pygame.font.SysFont(None, 40), (255, 255, 255), WIN, WIDTH // 2, HEIGHT // 2)
        draw_text("2 Spieler", pygame.font.SysFont(None, 40), (255, 255, 255), WIN, WIDTH // 2, HEIGHT // 2 + 80)
        multiplayer: bool #Nicht immer Multiplayer
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_single.collidepoint(event.pos): #Click zu Singleplayer
                    return False
                elif button_multi.collidepoint(event.pos): #Click zu Multiplayer
                    return True

        pygame.display.flip()

def map_screen():
    font = pygame.font.SysFont(None, 50)
    title_font = pygame.font.SysFont(None, 100)
    button_color = (0, 200, 0)
    text_color = (255, 255, 255)

    while True:
        WIN.fill((144, 238, 144))

        # Überschrift oben mittig
        title_surface = title_font.render("Wähle die Map", True, (0, 100, 0))
        WIN.blit(title_surface, (WIDTH // 2 - title_surface.get_width() // 2, 50))

        # Button-Positionen
        buttons = [
            pygame.Rect(WIDTH // 4 - 150, HEIGHT // 4, 300, 60),        # Map 1
            pygame.Rect(WIDTH // 2 + 150, HEIGHT // 4, 300, 60),        # Map 2
            pygame.Rect(WIDTH // 4 - 150, HEIGHT // 1.5, 300, 60),      # Map 3
            pygame.Rect(WIDTH // 2 + 150, HEIGHT // 1.5, 300, 60),      # Map 4
        ]

        # Text auf den Buttons
        button_labels = ["Map 1", "Map 2", "Map 3", "Map 4"]

        for i, rect in enumerate(buttons):
            pygame.draw.rect(WIN, button_color, rect)

            # Button-Text (mittig im Button)
            text_surface = font.render(button_labels[i], True, text_color)
            WIN.blit(text_surface, (rect.centerx - text_surface.get_width() // 2,rect.centery - text_surface.get_height() // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(buttons):
                    if rect.collidepoint(event.pos):
                        return i

        pygame.display.flip()



#Chatgpt/selber bearbeitet
def end_screen(multiplayer):
    font = pygame.font.SysFont(None, 100)
    button_restart = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 30, 300, 60)
    button_exit = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 60)
    button_options_screen = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 130, 300, 60)
    while True:
        WIN.fill((144, 238, 144))  # Schwarzer Hintergrund
        draw_text(player, font, (255, 255, 255), WIN, WIDTH// 2, HEIGHT // 4)
        pygame.mixer.music.stop()

        # Buttons zeichnen
        pygame.draw.rect(WIN, (0, 200, 0), button_restart)
        pygame.draw.rect(WIN, (200, 0, 0), button_exit)
        pygame.draw.rect(WIN, (0, 0, 200), button_options_screen)
        draw_text("Neustart", pygame.font.SysFont(None, 40), (255, 255, 255), WIN, WIDTH // 2, HEIGHT // 2)
        draw_text("Beenden", pygame.font.SysFont(None, 40), (255, 255, 255), WIN, WIDTH // 2, HEIGHT // 2 + 80)
        draw_text("Hauptmenü", pygame.font.SysFont(None, 40), (255, 255, 255), WIN, WIDTH // 2, HEIGHT // 2 + 160)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_restart.collidepoint(event.pos):
                    #Reset der Autos und Runden
                    lap_count = 0
                    lap_count2 = 0
                    player_car.reset()
                    player_car2.reset()
                    go_played = False
                    return False, multiplayer, map_screen()# Spiel wird neugestartet
                if button_exit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                if button_options_screen.collidepoint(event.pos): # Zurück zum options screen

                    return False, options_screen(), map_screen()
        pygame.display.flip()


#ChatGPT
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)
#ChatGPT / selber bearbeitet
def draw_lap_count(win, lap_count):
    font = pygame.font.SysFont(None, 50)  # Schriftart mit Größe 40
    text = f"Runde: {lap_count+1}""/3" # Text der Runde
    # Zeichne den Text an einer gut sichtbaren Position
    draw_text(text, font, (255, 0, 0), win, 2000 // 2, 50)  # Weisser Text bei Position (Mitte oben)
#selber bearbeitet
def draw_lap_count2(win, lap_count2):
    font = pygame.font.SysFont(None, 50)  # Schriftart mit Größe 40
    text = f"Runde: {lap_count2+1}""/3"  # Text der Runde
    # Zeichne den Text an einer gut sichtbaren Position (z.B. oben links)
    draw_text(text, font, (0, 255, 0), win, 200 // 2, 50)  # Weißer Text bei Position (Mitte oben)
#ChatGPT
def draw_timer(win, single_timer):
    font = pygame.font.SysFont(None, 50)  # Schriftart mit Größe 40
    text = f"Zeit:{single_timer}"
    # Zeichne den Text an einer gut sichtbaren Position (z.B. oben links)
    draw_text(text, font, (255, 0, 0), win, 1130 // 2, 25)  # Weißer Text bei Position (Mitte oben)

def draw_reset(win):
    font = pygame.font.SysFont(None, 25)  # Schriftart mit Größe 40
    text = "'ENTER' für reset"
    draw_text(text, font, (255, 255, 255), win, 1130 // 2, 600)

def draw_back2menu(win):
    font = pygame.font.SysFont(None, 25)  # Schriftart mit Größe 40
    text = "'BACKSPACE' für Hauptmenü"
    draw_text(text, font, (255, 255, 255), win, 1130 // 2, 630)

#selber
def timer_reset():
    global single_timer
    single_timer = 0

#ChatGPT/Selber/Ray
def start_countdown(win, images, player_car, player_car2, multiplayer, lap_count, lap_count2, go_s, countdown_s):

    countdown_s.set_volume(1)
    countdown_s.play()
    font = pygame.font.SysFont(None, 100)

    for i in range(3, 1, -1):  # Countdown von 3 bis 1
        draw(win, images, player_car, player_car2, multiplayer, 0, lap_count, lap_count2)  # Strecke & Autos zeichnen
        draw_text(str(i), font, (255, 255, 255), win, WIDTH // 2, HEIGHT // 2)  # Countdown-Zahl
        pygame.display.update()
        pygame.time.delay(1000)  # 1 Sekunde warten
    for i in range(1, 0, -1):  # Countdown von 3 bis 1
        draw(win, images, player_car, player_car2, multiplayer, 0, lap_count, lap_count2)  # Strecke & Autos zeichnen
        draw_text(str(i), font, (255, 255, 255), win, WIDTH // 2, HEIGHT // 2)  # Countdown-Zahl
        pygame.display.update()
        pygame.time.delay(1000)  # 1 Sekunde warten


    # "GO!" anzeigen
    go_s.play()
    go_s.set_volume(1)
    draw(win, images, player_car, player_car2, multiplayer, 0, lap_count, lap_count2)  # Strecke & Autos zeichnen
    draw_text("GO!", font, (0, 255, 0), win, WIDTH // 2, HEIGHT // 2)
    pygame.display.update()
    pygame.time.delay(1000)
    return True



# Alle Bilder importiert
#alles selber
FINISH = scale_image(pygame.image.load("Sprites/finish.png"), 1.08)
FINISH_POSITION = (99, 325)
FINISH_MASK = pygame.mask.from_surface(FINISH)

GCAR = scale_image(pygame.image.load("Sprites/green-car.png"), 0.5)
BORDERS_1 = pygame.image.load("Sprites/Borders-Photoroom.png")
BORDERS_2 = pygame.image.load("Sprites/Track2border....png")
BORDERS_3 = pygame.image.load("Sprites/Border3-Photoroom.png")
BORDERS_4 = pygame.image.load("Sprites/Border4-Photoroom.png")
GRASS = scale_image(pygame.image.load("Sprites/Hintergrund neu.png"), 1)
PCAR = scale_image(pygame.image.load("Sprites/purple-car.png"), 0.8)
RCAR = scale_image(pygame.image.load("Sprites/red-car.png"), 0.5)
WCAR = scale_image(pygame.image.load("Sprites/white-car.png"), 0.8)
TRACK_1 = pygame.image.load("Sprites/Track-Photoroom.png")
TRACK_2 = pygame.image.load("Sprites/Track2...-Photoroom.png")
TRACK_3 = pygame.image.load("Sprites/Track3-Photoroom.png")
TRACK_4 = pygame.image.load("Sprites/Track4-Photoroom.png")
Startbildschirm = pygame.image.load("Sprites/Startbildschirm.png")
Startbildschirm.set_colorkey((0,0,0))
Startbildschirm_Auto = pygame.image.load("Sprites/Startbildschirm_Auto-fotor-bg-remover-20250326134022.png")
Startbildschirm_AutoBlau = pygame.image.load("Sprites/Startbildschirm_AutoBlau-fotor-bg-remover-2025032614154.png")

#Liste mit Tracks/Borders für die Auswahl der Maps
track_array = [TRACK_1, TRACK_2, TRACK_3, TRACK_4]
border_array = [BORDERS_1, BORDERS_2, BORDERS_3, BORDERS_4]

#Audiodateien
bust = pygame.mixer.Sound("Audio/Bust.mp3")
bounce_s = pygame.mixer.Sound("Audio/Bounce.mp3")
carcollision_s = pygame.mixer.Sound("Audio/Collision2.mp3")
finish_s = pygame.mixer.Sound("Audio/Player_wins.mp3")
countdown_s = pygame.mixer.Sound("Audio/321.mp3")
go_played = False
go_s = pygame.mixer.Sound("Audio/Go.mp3")
acceleration_s = pygame.mixer.Sound("Audio/Acceleration.mp3")
breaking_s = pygame.mixer.Sound("Audio/Breaking.mp3")
acceleration_s2 = pygame.mixer.Sound("Audio/Acceleration.mp3")
breaking_s2 = pygame.mixer.Sound("Audio/Breaking.mp3")
pygame.mixer.music.load("Audio/forward-312979.mp3")
pygame.mixer.music.set_volume(0.5)

#Channels für Audiowiedergabe
car1chanacc = pygame.mixer.Channel(0)
car2chanacc = pygame.mixer.Channel(1)
effectchan = pygame.mixer.Channel(2)
car1chandec = pygame.mixer.Channel(3)
car2chandec = pygame.mixer.Channel(4)
car1col = pygame.mixer.Channel(5)
car2col = pygame.mixer.Channel(6)

#Scalierung des Fensters basierend auf Grösse der Borders
WIDTH, HEIGHT = BORDERS_2.get_width(), BORDERS_2.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car go vroom vroom 3")
finish_timer = 0
finish_timer2 = 0
colliding_with_finish = False
colliding_with_finish_2 = False

#Delta Time
FPS = 60
last_time = time.time()

# Videoserie: Pygame Car Racing Tutorial
can_collide = True
class AbstractCar:

    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.last_vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.acceleration = 0.05
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
        #pygame.display.update()

    def move_forward(self, delta_time):
        self.last_vel = self.vel
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move(delta_time)

    def move_backward(self, delta_time):
        self.last_vel = self.vel
        self.vel = max(self.vel - self.acceleration, -self.max_vel / 2)#Selber geändert
        self.move(delta_time)

    def move(self, delta_time):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        

        self.y -= vertical * delta_time
        self.x -= horizontal * delta_time
        

    def reduce_speed(self, delta_time):
        if self.vel != 0:
            self.last_vel = self.vel
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move(delta_time)




    #Verbesserung durch Ray, ChatGPT und selber
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

    def handle_collision(self, mask, delta_time, bounce_s):
        if time.time() - self.last_collision_time > 0.1:
            collision_point = self.collide(mask)
            if collision_point:
                bounce_s.play()
                self.bounce(delta_time)
                self.last_collision_time = time.time()

    def reduce_speed(self, delta_time):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move(delta_time)

    def bounce(self, delta_time):
        if self.vel == 0:
            self.vel = self.last_vel
        self.vel = -self.vel / 1.5
        self.move(delta_time)

    #Von Chatgpt / selber geändert
    def car_bounce(self, delta_time):
            self.vel = -self.vel / 3
            self.move(delta_time)

    # selber
class PlayerCar2(AbstractCar):
    IMG = GCAR
    START_POS = (110, 230)

    def __init__(self, max_vel, rotation_vel):
            super().__init__(max_vel, rotation_vel)
            self.last_collision_time = 0

    def handle_collision(self, mask, delta_time, bounce_s):
            if time.time() - self.last_collision_time > 0.1:
                collision_point = self.collide(mask)
                if collision_point:
                    bounce_s.play()
                    self.bounce(delta_time)
                    self.last_collision_time = time.time()

    def reduce_speed(self, delta_time):
            self.vel = max(self.vel - self.acceleration / 2, 0)
            self.move(delta_time)

    def bounce(self, delta_time):
        if self.vel == 0:
            self.vel = self.last_vel
        self.vel = -self.vel / 1.5
        self.move(delta_time)

    def car_bounce(self, delta_time):
            self.vel = -self.vel / 1.5
            self.move(delta_time)


#Videoserie: Pygame Car Racing Tutorial
def draw(win, images, player_car, player_car2, multiplayer, single_timer, lap_count, lap_count2):
    for img, pos in images:
        win.blit(img, pos)
    player_car.draw(win)
    draw_reset(win)
    draw_back2menu(win)

    if not multiplayer:
        draw_timer(win, single_timer)
    if multiplayer:
        player_car2.draw(win)
        draw_lap_count(win, lap_count)
        draw_lap_count2(win, lap_count2)




running = True
clock = pygame.time.Clock()
player_car = PlayerCar(4.5, 2)
player_car2 = PlayerCar2(4.5, 2)

lap_count = 0
lap_count2 = 0

start_screen()
multiplayer = options_screen()

array_num = map_screen()
selected_track = track_array[array_num]
selected_border = border_array[array_num]
TRACK_BORDER_MASK = pygame.mask.from_surface(selected_border)
images = [(GRASS, (0, 0)), (selected_track, (0, 0)), (FINISH, FINISH_POSITION), (selected_border, (0, 0))]
single_timer = 0  # Timer nach dem Countdown starten
#Videoserie: Pygame Car Racing Tutorial
while running:
    if not pygame.mixer.music.get_busy() and go_played:
        pygame.mixer.music.play()
    if not go_played:
        go_played = start_countdown(WIN, images, player_car, player_car2, multiplayer, lap_count, lap_count2, go_s, countdown_s)
        last_time = time.time()
    delta_time = time.time() - last_time
    delta_time *= 60
    last_time = time.time()

    if not multiplayer and go_played:
        single_timer += 1/60 * delta_time




    draw(WIN, images, player_car, player_car2, multiplayer, round(single_timer, 1), lap_count, lap_count2)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    keys = pygame.key.get_pressed()
    moved = False
    if keys[pygame.K_6] and keys[pygame.K_9] and keys[pygame.K_y]:
        if not effectchan.get_busy():
            effectchan.play(bust) #Geheime Botschaft spielen


    if keys[pygame.K_LEFT]:
        player_car.rotate(delta_time, left=True) #Linksdrehung
    if keys[pygame.K_RIGHT]:
        player_car.rotate(delta_time, right=True) #Rechtsdrehung
    if keys[pygame.K_UP]:
        moved = True
        player_car.move_forward(delta_time) #Beschleunigung
        if not car1chanacc.get_busy():
            car1chanacc.play(acceleration_s) #Beschleunigung Sound spielen
    if keys[pygame.K_DOWN]:
        moved = True
        player_car.move_backward(delta_time) #Bremsen
        if not car1chandec.get_busy():
            car1chandec.play(breaking_s) #Bremsen Sound spielen
    if keys[pygame.K_ESCAPE]:
        running = False #Beenden wenn Escape gedrückt wird
    if keys[pygame.K_RETURN]: #Erneut spielen Funktion mithilfe der Enter-Taste
        if multiplayer:
            lap_count = 0
            lap_count2 = 0
            player_car2.reset() #Autos zurück zur Startposition
            player_car.reset()
            pygame.mixer.stop() #Musik stoppen
             #Timer neustarten
            player_car2.reset()
            go_played = False
        else:
            player_car.reset()
            pygame.mixer.stop()
            timer_reset()
            single_timer = 0
            finish_timer = 0
            finish_timer2 = 0
            go_played = False

    if keys[pygame.K_BACKSPACE]:
        timer_reset()
        single_timer = 0
        finish_timer = 0
        player_car.reset()
        if multiplayer:
            player_car2.reset()

            pygame.mixer.stop()
            pygame.mixer.music.stop()

        pygame.mixer.stop()
        pygame.mixer.music.stop()
        multiplayer = options_screen()
        array_num = map_screen()
        selected_track = track_array[array_num]
        selected_border = border_array[array_num]
        TRACK_BORDER_MASK = pygame.mask.from_surface(selected_border)
        images = [(GRASS, (0, 0)), (selected_track, (0, 0)), (FINISH, FINISH_POSITION), (selected_border, (0, 0))]
        go_played = False
    if not moved:
        player_car.reduce_speed(delta_time)


#Selber

    if multiplayer:
        moved2 = False
        if keys[pygame.K_a]:
            player_car2.rotate(delta_time, left=True)
        if keys[pygame.K_d]:
            player_car2.rotate(delta_time, right=True)
        if keys[pygame.K_w]:
            moved2 = True
            player_car2.move_forward(delta_time)
            if not car2chanacc.get_busy():
                car2chanacc.play(acceleration_s2)

        if keys[pygame.K_s]:
            moved2 = True
            player_car2.move_backward(delta_time)
            if not car2chandec.get_busy():
                car2chandec.play(breaking_s2)
        if not moved2:
            player_car2.reduce_speed(delta_time)

        if player_car2.collide(player_car.get_mask(), player_car.x, player_car.y):
            player_car.car_bounce(delta_time)
            if car2col.get_busy():
               car2col.play(carcollision_s)


    if player_car.collide(player_car2.get_mask(), player_car2.x, player_car2.y):
        player_car2.car_bounce(delta_time)
        if car1col.get_busy():
            car1col.play(carcollision_s)

    player_car.handle_collision(TRACK_BORDER_MASK, delta_time, bounce_s)

#Selber/ChatGPT/Ray hat geholfen
    finish_point_of_collision = player_car.collide(FINISH_MASK, *FINISH_POSITION)
    if finish_point_of_collision != None and colliding_with_finish == False:
        if finish_point_of_collision[1] == 0:
            player_car.reset()



        else:
            colliding_with_finish = True
            if multiplayer:
                lap_count += 1
            finish_timer = time.time()
            timer_reset()

    if colliding_with_finish:
        if time.time() - finish_timer > 3:
            colliding_with_finish = False
            finish_timer = 0
    if multiplayer:
        if lap_count == 3:
            player = "Spieler 1 gewinnt"
            finish_s.play()
            go_played, multiplayer, array_num = end_screen(multiplayer)
            selected_track = track_array[array_num]
            selected_border = border_array[array_num]
            TRACK_BORDER_MASK = pygame.mask.from_surface(selected_border)
            images = [(GRASS, (0, 0)), (selected_track, (0, 0)), (FINISH, FINISH_POSITION), (selected_border, (0, 0))]
            player_car.reset()
            player_car2.reset()
            lap_count = 0
            lap_count2 = 0

    if multiplayer:
        player_car2.handle_collision(TRACK_BORDER_MASK, delta_time, bounce_s)

        finish_point_of_collision = player_car2.collide(FINISH_MASK, *FINISH_POSITION)
        if finish_point_of_collision != None and colliding_with_finish_2 == False:
            if finish_point_of_collision[1] == 0:
                player_car2.reset()
            else:
                colliding_with_finish_2 = True
                lap_count2 += 1
                finish_timer2 = time.time()


        if colliding_with_finish_2:
            if time.time() - finish_timer2 > 3:
                colliding_with_finish_2 = False
                finish_timer2 = 0
        if lap_count2 == 3:
            player = "Spieler 2 gewinnt"
            finish_s.play()
            go_played, multiplayer,array_num = end_screen(multiplayer)
            selected_track = track_array[array_num]
            selected_border = border_array[array_num]
            TRACK_BORDER_MASK = pygame.mask.from_surface(selected_border)
            images = [(GRASS, (0, 0)), (selected_track, (0, 0)), (FINISH, FINISH_POSITION), (selected_border, (0, 0))]
            player_car.reset()
            player_car2.reset()
            lap_count = 0
            lap_count2 = 0


    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
