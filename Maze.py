import pygame
import sys

pygame.init()

# Window size
window_height = 300 #y
window_width = 400 #x


# Color options 
white =  (255, 255, 255)
pink =   (204, 0, 102)
green =  (0, 102, 102)
orange = (255, 128, 0)
black =  (0 , 0, 0)

# Creating display window
screen = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Abascal") 

""" 
Level display 
O   blocked cell
" " path cell
E   final point
"""
maze=[
    "OOOOOOOOOOOOOOOOOOOO",
    "OP                 O",
    "O   O    O    O    O",
    "O    O      OOO    O",
    "O  O OOO OO  OOOOO O",
    "O  O  O  OO      O O",
    "O  OO  O OOO OOO O O",
    "O OOOO    OO OE  O O",
    "O    OOOO OO OOO   O",
    "O OO    O OO       O",
    "O OO   OO  OOO     O",
    "O OO       OOOOOO  O",
    "O      OOE         O",
    "O             E    O",
    "OOOOOOOOOOOOOOOOOOOO",
]

# Wall list
walls = []

# End_point list
end_points = []

# Player list
players = []

# Wall class rectangle generator
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect= pygame.Rect(pos[0], pos[1], 20, 20)

class End_point(object):
    
    def __init__(self, pos):
        end_points.append(self)
        self.rect= pygame.Rect(pos[0], pos[1], 20, 20)

class Player(object):
    
    def __init__(self, pos):
        players.append(self)
        self.rect= pygame.Rect(pos[0], pos[1], 20, 20)
       

def collisions():
    if any(end_point.rect.colliderect(player.rect) for end_point in end_points):
        sys.exit()

# Parsing the maze string
# Variables representing the position 
x = 0 
y = 0
for row in maze:
    for col in row:
        if col == "O":
            Wall((x, y))
        if col == "E":
            End_point((x,y))
        if col == "P":
            Player((x,y))
        x += 20
    y += 20
    x = 0

clock = pygame.time.Clock()
while True:
    
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() 

    # Player movement in maze 
    keys = pygame.key.get_pressed()
    player_speed = 2

    if keys[pygame.K_UP]:
        player.rect.move_ip(0, -player_speed)
        if any(wall.rect.colliderect(player.rect) for wall in walls):
            player.rect.move_ip(0, player_speed)

    if keys[pygame.K_DOWN]:
        player.rect.move_ip(0, player_speed)
        if any(wall.rect.colliderect(player.rect) for wall in walls):
            player.rect.move_ip(0, -player_speed)

    if keys[pygame.K_LEFT]:
        player.rect.move_ip(-player_speed, 0)
        if any(wall.rect.colliderect(player.rect) for wall in walls):
            player.rect.move_ip(player_speed, 0)

    if keys[pygame.K_RIGHT]:
        player.rect.move_ip(player_speed, 0)
        if any(wall.rect.colliderect(player.rect) for wall in walls):
            player.rect.move_ip(-player_speed, 0)

    screen.fill(black)

    # Drawing walls
    for wall in walls:
        pygame.draw.rect(screen, pink, wall)
    
    # Drawing end_points
    for end_point in end_points:
        pygame.draw.rect(screen, green, end_point)

    # Drawing players
    for player in players:
        pygame.draw.rect(screen,orange,player.rect)

    collisions()

    # Update screen 
    pygame.display.update()

    

    