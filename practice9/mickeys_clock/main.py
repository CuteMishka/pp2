import pygame
import datetime
from clock import rotate_hand

pygame.init()
W, H = 800, 600
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

mickey = pygame.image.load('images/main_mickey.png').convert_alpha()
hand_min = pygame.image.load('images/right_hand.png').convert_alpha()
hand_sec = pygame.image.load('images/left_hand.png').convert_alpha()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    angle_min = now.minute * 6
    angle_sec = now.second * 6

    screen.fill((255, 255, 255))
    screen.blit(mickey, (0, 0))

    surf_m, rect_m = rotate_hand(hand_min, angle_min, (W//2, H//2))
    surf_s, rect_s = rotate_hand(hand_sec, angle_sec, (W//2, H//2))

    screen.blit(surf_m, rect_m)
    screen.blit(surf_s, rect_s)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()