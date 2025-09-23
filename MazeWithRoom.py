import sys
import pygame
from Backtracker import generate_maze_backtracker, generate_maze_backtracker_without_recursion
from Prima import generate_maze_prim

pygame.init()


width, height = 83, 83
cell_size = 10
size_room = 5
count_exit = 4

screen_width = width * cell_size
screen_height = height * cell_size

screen = pygame.display.set_mode((screen_width, screen_height))

maze = generate_maze_prim(width, size_room, count_exit)

running = True
font = pygame.font.SysFont(None, 24)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for y in range(height):
        for x in range(width):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)

            if maze[y][x] == '#':
                pygame.draw.rect(screen, (0, 0, 155), rect)
            elif maze[y][x] == '1':
                pygame.draw.rect(screen, (255, 0, 155), rect)
            elif maze[y][x] == 'f':
                pygame.draw.rect(screen, (0, 255, 0), rect)
            else:
                pygame.draw.rect(screen, (255, 255, 255), rect)


            pygame.draw.rect(screen, (200, 200, 200), rect, 1)

    pygame.display.flip()

pygame.quit()
sys.exit()