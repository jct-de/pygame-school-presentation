import pygame

pygame.init() # Initialisiert das Spiel
screen = pygame.display.set_mode((1280, 720)) ## Fenstergröße bestimmen
clock = pygame.time.Clock() # Holt sich den sleeper

# Variablensetzung
running = True
dt = 0


# In die mitte des Spiels positionieren
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)




# Das Hauptgeschehen des Spiels: in 60 FPS schritten - alle 16,6 Millisekunden
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Füllt den Hintergrund mti der Farbe Lila
    screen.fill("purple")

    # Gibt an der Spielerposition einen Kreis
    pygame.draw.circle(screen, "red", player_pos, 40)

    # Guckt, welche Tasten aktuell gedrückt werden
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # Gibt die Änderungen, die wir übergeben haben, an das Spiel weiter
    pygame.display.flip()


    # Definiert die Bildwiederholrate / die Ticks vom Spiel
    dt = clock.tick(60) / 1000

pygame.quit()