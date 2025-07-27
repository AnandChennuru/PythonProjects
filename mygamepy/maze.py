import pygame
import math

# Initialise the pygame
pygame.init()

# Create the window
screen = pygame.display.set_mode((800, 600))

# Background and Walls
grassImg = pygame.image.load("imgs/grass.jpg")
grassImg = pygame.transform.scale(grassImg, (800,600))
wallImg = pygame.image.load("imgs/wall.png")
wallImg = pygame.transform.scale(wallImg,(40,40))
walls = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
         [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
         [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
         [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
tile_size = 40
wall_width = 1

# Title and Icon
pygame.display.set_caption("Tank Wars 2P")
icon = pygame.image.load("imgs/hero1.png")
pygame.display.set_icon(icon)

# Player 1
p1Img = pygame.image.load("imgs/hero1.png")
p1Img = pygame.transform.scale(p1Img,(64,64))
p1X = 50
p1Y = 50
p1X_change = 0
p1Y_change = 0

# Player 2
p2Img = pygame.image.load("imgs/hero2.png")
p2Img = pygame.transform.scale(p2Img,(64,64))
p2X = 50
p2Y = 450
p2X_change = 0
p2Y_change = 0

# Functions
# Drawing walls
def draw_walls():
    for row_ind, row in enumerate(walls):
        for col_ind, cell in enumerate(row):
            if cell == 1:
                wall_coords = []
                wallx = col_ind * tile_size
                wally = row_ind * tile_size
                screen.blit(wallImg,(wallx, wally))
                wall_coords.append((wallx, wally))
                return wall_coords

# Spawning Players
def players(x1, y1, x2, y2):
    screen.blit(p1Img, (x1, y1))
    screen.blit(p2Img, (x2, y2))


def wall_collision(x, y, x1, y1):
    dist = math.sqrt((math.pow(x - x1, 2)) + (math.pow(y - y1, 2)))
    if dist <= 32:
        return True
    return False


# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(grassImg, (0,0))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                p1X_change += -0.3
            if event.key == pygame.K_RIGHT:
                p1X_change += 0.3
            if event.key == pygame.K_UP:
                p1Y_change += -0.3
            if event.key == pygame.K_DOWN:
                p1Y_change += 0.3
            if event.key == pygame.K_a:
                p2X_change += -0.3
            if event.key == pygame.K_d:
                p2X_change += 0.3
            if event.key == pygame.K_w:
                p2Y_change += -0.3
            if event.key == pygame.K_s:
                p2Y_change += 0.3

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                p1X_change = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                p1Y_change = 0
            if event.key in [pygame.K_a, pygame.K_d]:
                p2X_change = 0
            if event.key in [pygame.K_w, pygame.K_s]:
                p2Y_change = 0


    p1X += p1X_change
    p1Y += p1Y_change
    p2X += p2X_change
    p2Y += p2Y_change

    # Boundaries
    if p1X > 768 or p1X < 0:
        p1X_change = 0
    if p1Y > 568 or p1Y < 0:
        p1Y_change = 0
    if p2X > 768 or p2X < 0:
        p2X_change = 0
    if p2Y > 568 or p2Y < 0:
        p2Y_change = 0


    if wall_collision(p1X, p2Y, wallx, wally):
        p1X_change = 0


    players(p1X, p1Y, p2X, p2Y)
    draw_walls()

    # frame update
    pygame.display.update()
