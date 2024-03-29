import pygame

from color_constants import *
from config import *



WIN = pygame.display.set_mode((WIDTH, HEIGHT))



pygame.display.set_caption(title_caption)


def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()    


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        draw_window()
        
    
    
    pygame.quit()
    
    
if __name__ == "__main__":
    main()
