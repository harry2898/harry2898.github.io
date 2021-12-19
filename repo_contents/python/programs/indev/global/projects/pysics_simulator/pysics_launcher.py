import pygame

from pysics_utils.color_constants import *
from launcher.configs.default_launcher_config import *


def draw_window():
    WIN.fill(winBgColor)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(WIN_FPS_CAP)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        draw_window()
        
    
    
    pygame.quit()
    


    
if __name__ == "__main__":
    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption(title_caption)
    
    main()
