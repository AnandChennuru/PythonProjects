import pygame
import math
import random

# Initialise the pygame
pygame.init()

# Create the window
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("imgs/stars.jpg")

# Title and Icon
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load("imgs/rocket.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("imgs/player.png")
playerX = 370
playerY = 500
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("imgs/enemy.png"))
    enemyX.append(random.randint(1, 735))
    enemyY.append(random.randint(50, 100))
    enemyX_change.append(0.3)
    enemyY_change.append(32)

# Bullet
# ready - cant see bullet
# fire - bullet will move
bulletImg = pygame.image.load("imgs/bullet.png")
bulletX = 0
bulletY = playerY
bulletX_change = 0
bulletY_change = 0.8
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def is_collision(x, y, x1, y1):
    distance = math.sqrt((math.pow(x - x1, 2)) + (math.pow(y - y1, 2)))
    if distance <= 27:
        return True
    else:
        return False
score = 0


# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # KEYSTROKES
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change += -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.4
            if (event.key == pygame.K_SPACE) and (bullet_state == "ready"):
                bulletX = playerX  # to set bullet at spaceship initially
                bullet_fire(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    # Border wall for player and enemy
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies):
        if enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        enemyX[i] += enemyX_change[i]

        # Collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = playerY
            bullet_state = "ready"
            enemyX[i] = random.randint(1, 735)
            enemyY[i] = random.randint(50, 100)
            score += 1
            print("Score:", score)

        enemy(enemyX[i], enemyY[i], i)

    # bullet reset from wall
    if bulletY <= 0:
        bulletY = playerY
        bullet_state = "ready"
    # bullet movement
    if bullet_state == "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)

    # frame update
    pygame.display.update()