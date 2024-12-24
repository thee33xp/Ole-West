import pygame
from csv import reader

def get_font(size):
    return pygame.font.SysFont("Arial",size)
   
WIDTH = 640
H_W = WIDTH/2
HEIGHT = 480
H_H = HEIGHT/2
RES = (WIDTH,HEIGHT)

FPS = 60
TILE = 16

BLACK = (0,0,0)
GREY = (66,66,66)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

FLOOR_YELLOW = (238,202,132)

xgrid = WIDTH//TILE
ygrid = HEIGHT//TILE
def draw_grid(surf):
    #for x in range(0,xgrid):
        #pygame.draw.line(surf,GREEN,(0,TILE*x),(WIDTH,TILE*x))
    for y in range(0,ygrid):
        pygame.draw.line(surf,RED,(0,TILE*y),(TILE*y,HEIGHT))



def LOAD_CSV(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map,delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map