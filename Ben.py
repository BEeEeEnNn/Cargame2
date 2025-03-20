import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))

sound = pygame.mixer.Sound("Bust.mp3")

sound.set_volume(0.5)

sound.set_volume(1)



lambopic = pygame.image.load("Lambo2.png").convert_alpha()
#lambopic = pygame.transform.flip(lambopic,1,0)
lambopic = pygame.transform.scale_by(lambopic,0.3)

font = pygame.font.Font(None, size=40 )
sound.play()
x = 640
clock = pygame.time.Clock()

running = True
while running:



    screen.fill((0,0,0))

    screen.blit(lambopic, (300, x))
    screen.blit(lambopic, (x, 500))

    x += -5
    text = font.render("Car go vroom vroom 3", True, (255,0,0))
    screen.blit(text, (170,320))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                sound.play()
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(60)

pygame.quit()












