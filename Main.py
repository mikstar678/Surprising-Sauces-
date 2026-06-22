from sys import exit
import pygame
pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 700
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Surprising Sauces")
borat = pygame.image.load("Visit kazakhstan.png").convert_alpha()
Level1fatty = pygame.image.load("Fatguy1.png").convert_alpha()
Level1fatty = pygame.transform.scale(Level1fatty, (WIDTH, HEIGHT))
global pxpsize
pxpsize = 80
pixelpizza = pygame.image.load("pixelpizza.png").convert_alpha()
pixelpizza = pygame.transform.scale(pixelpizza, (pxpsize,pxpsize))
pixelpizzarect = pixelpizza.get_rect(center=(50,620))

y = 0
while y == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        pxpsize = 90
        pixelpizza = pygame.transform.scale(pixelpizza, (pxpsize, pxpsize))
    screen.fill("black")
    screen.blit(Level1fatty,(0,0,))
    screen.blit(pixelpizza,pixelpizzarect)
    pygame.display.update()
    clock.tick(FPS)
