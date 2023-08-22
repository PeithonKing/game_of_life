import numpy as np
import pygame
import time
from utils import step

COLOR_DIE = (0, 0, 0)
COLOR_ALIVE = (255, 255, 255)

def update(screen, cells, size):
    for i in range(cells.shape[0]):
        for j in range(cells.shape[1]):
            if cells[i, j] == 1:
                pygame.draw.rect(screen, COLOR_ALIVE, (j * size, i * size, size, size))
            elif cells[i, j] == 0:
                pygame.draw.rect(screen, COLOR_DIE, (j * size, i * size, size, size))
            else:
                raise ValueError(f'Disaster happened: {cells[i, j] = }')


def main():
    pygame.init()
    pygame.display.set_caption("Game of Life")
    screen = pygame.display.set_mode((800, 600))
    
    cells = np.zeros((60, 80))
    screen.fill(COLOR_DIE)
    update(screen, cells, 10)
    
    pygame.display.flip()
    pygame.display.update()
    
    running = False
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            
            elif pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                x, y = x // 10, y // 10
                cells[y, x] = 1 - cells[y, x]
                update(screen, cells, 10)
                pygame.display.update()
                        
        screen.fill(COLOR_DIE)    
        
        if running:
            cells = step(cells)
            update(screen, cells, 10)
            pygame.display.update()
            
        time.sleep(0.01)

if __name__ == '__main__':
	main()