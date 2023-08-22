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
                raise ValueError(f'Disaster happened! Earth will be destroyed! {cells[i, j] = }')

def main():
    pygame.init()
    pygame.display.set_caption("Game of Life")
    WIDTH = 800
    HEIGHT = 600
    SIZE = 10
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    cells = np.zeros((HEIGHT//SIZE, WIDTH//SIZE))
    screen.fill(COLOR_DIE)
    update(screen, cells, SIZE)

    pygame.display.flip()
    pygame.display.update()

    running = False

    t0 = time.time()
    i = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, SIZE)
                    pygame.display.update()
                # if `s` is pressed, save the current state of the
                # game to a file named `save_width_height_size.npy`
                if event.key == pygame.K_s:
                    np.save(f'save_{WIDTH}_{HEIGHT}_{SIZE}.npy', cells)
            
            elif pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                x, y = x // SIZE, y // SIZE
                cells[y, x] = 1 - cells[y, x]
                update(screen, cells, SIZE)
                pygame.display.update()
                        
        screen.fill(COLOR_DIE)    
        
        if running:
            cells = step(cells)
            update(screen, cells, SIZE)
            pygame.display.update()
        # else:
        #     time.sleep(0.03)
        
        # i += 1
        # th = 100
        # if i == th:
        #     print(f"FPS: {th / (time.time() - t0)}")
        #     t0 = time.time()
        #     i = 0

if __name__ == '__main__':
    main()