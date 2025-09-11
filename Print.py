import pygame
import sys
from Backtracker import generate_maze_backtracker
from Kruskal import generate_maze_kruskal
from Prima import generate_maze_prim
from Сellular_automata import generate_maze_cellular


pygame.init()


width, height = 131, 81
cell_size = 10


# width, height = 41, 27
# cell_size = 30
# maze_back = generate_maze_backtracker(width, height)

screen_width = width * cell_size
screen_height = height * cell_size

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Генератор лабиринтов")

maze_prim = generate_maze_prim(width, height)
maze_kruskal = generate_maze_kruskal(width, height)
maze_automata = generate_maze_cellular(width, height)

current_maze = maze_prim
current_algorithm = "Алгоритм Прима"

running = True
font = pygame.font.SysFont(None, 24)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_maze = maze_prim
                current_algorithm = "Алгоритм Прима"
            elif event.key == pygame.K_2:
                current_maze = maze_automata
                current_algorithm = "Алгоритм клеточных автоматов"
            elif event.key == pygame.K_3:
                current_maze = maze_kruskal
                current_algorithm = "Алгоритм Крускала"
            elif event.key == pygame.K_4:
                current_maze = maze_back
                current_algorithm = "Рекурсивный бэктрекинг"

    # Очистка экрана
    screen.fill((0, 0, 0))

    # Отрисовка лабиринта
    for y in range(height):
        for x in range(width):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)

            if current_maze[y][x] == '#':  # Стена
                pygame.draw.rect(screen, (0, 0, 155), rect)
            else:  # Проход
                pygame.draw.rect(screen, (255, 255, 255), rect)

            # Сетка
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)

    text = font.render(current_algorithm, True, (255, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.flip()

pygame.quit()
sys.exit()