from sys import exit
import pygame
pygame.init()
clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 700
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Surprising Sauces")
borat = pygame.image.load("Visit kazakhstan.png").convert_alpha()
cheatcode = input(str("enter cheat "))
y = 0
while y == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill("black")
    if cheatcode == ("i want to visit kazakhstan"):
        screen.blit(borat,(0,0))
    pygame.display.update()
    clock.tick(FPS)
