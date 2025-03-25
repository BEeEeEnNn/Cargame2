import pygame
import sys

# Initialisierung von Pygame
pygame.init()

# Bildschirmgröße und Farben
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)

# Bildschirm erstellen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Autorennspiel")

# Schriftart und -größe
font = pygame.font.SysFont(None, 60)

# Funktion zur Anzeige von Text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Startbildschirm-Funktion
def start_screen():
    while True:
        screen.fill(WHITE)
        draw_text("Autorennspiel", font, BLACK, screen, WIDTH // 2, HEIGHT // 4)
        draw_text("[Drücke ENTER zum Starten]", pygame.font.SysFont(None, 40), GREEN, screen, WIDTH // 2, HEIGHT // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_game()

        pygame.display.flip()

# Spiel-Hauptfunktion
def main_game():
    running = True
    while running:
        screen.fill(GREEN)
        draw_text("Das Spiel läuft...", font, WHITE, screen, WIDTH // 2, HEIGHT // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Startbildschirm aufrufen
start_screen()
