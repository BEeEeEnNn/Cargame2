import pygame, sys
from pygame.constants import QUIT

from pygame.locals import *

pygame.init()

sound = pygame.mixer.Sound("Audio/forward-312979.mp3")


HOCH = 500
BREIT = 500

FENSTER = pygame.display.set_mode((HOCH, BREIT))



White = (255, 255, 255)


Spielerbild = pygame.image.load("Sprites/Lego-Man-PNG-Image.png").convert_alpha()
Spielerbild = pygame.transform.scale_by(Spielerbild, 0.3)

Sprechblase = pygame.image.load("Sprites/OIP.jpg").convert_alpha()
Sprechblase = pygame.transform.scale_by(Sprechblase, 0.3)



while True:

    FENSTER.blit(Spielerbild, (150, 100))


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                FENSTER.blit(Sprechblase, (300, 0))
                sound.play()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()