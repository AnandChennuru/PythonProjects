import pygame

# Input height of wall
h = 5

# Initialising pygame
pygame.init()

# Game window
screen = pygame.display.set_mode((800,600))

# Game entities
wallImg = []
wallX = []
wallY = []
nw = 10
for i in range(nw):
    wallImg.append(pygame.image.load("imgs/wall.png"))
    wallX.append(0)
    wallY.append(0)

# Painting entities in window
def wall(x, y, i):
    screen.blit(wallImg[i], (x, y))

def build_wall(i, j, nw):
    while i < nw:
        j = 0
        while j < nw:
            wall(64*j,64*j, i)
            j += 1
        i += 1

# Game loop
running = True
while running:
    screen.fill((12,22,36))

    # Events inside window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # wall(wallX, wallY)

    build_wall(0,0, nw)

    pygame.display.update()