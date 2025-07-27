import pygame
import random

# Initialise the pygame
pygame.init()

# Create the window
screen = pygame.display.set_mode((800, 800))

# Title and Icon
pygame.display.set_caption("Fall Ball")
icon = pygame.image.load("imgs/ball64.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("imgs/bas128.png")
playerX = 350
playerY = 650
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pygame.image.load("imgs/ball64.png")
enemyX = random.randint(0,736)
enemyY = random.randint(50,100)
enemyX_change = 0
enemyY_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # KEYSTROKES
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                enemyY_change += 0.2
            if event.key == pygame.K_LEFT:
                playerX_change += -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    # Border wall for player and enemy
    if playerX <= 0:
        playerX = 0
    elif playerX >= 674:
        playerX = 674

    if enemyY >= 700:
        enemyY = 700
        enemyX = playerX + 20

    enemyY += enemyY_change
    enemy(enemyX, enemyY)

    player(playerX, playerY)



    # frame update
    pygame.display.update()
