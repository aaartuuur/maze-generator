import sys
import pygame
import copy
from Prima import MazeGenerator


def main():
    pygame.init()

    width, height = 15, 15
    cell_size = 10
    size_room = 3
    count_exit = 4

    screen_width = width * cell_size * 2
    screen_height = height * cell_size

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Maze Generator")

    maze_gen = MazeGenerator(width + 4, size_room, count_exit)
    maze = maze_gen.generate_maze_prim()

    maze_without_pass = copy.deepcopy(maze)

    maze_gen.find_all_paths()
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        for y in range(2, height + 2):
            for x in range(2, width + 2):
                rect = pygame.Rect(
                    (x - 2) * cell_size,
                    (y - 2) * cell_size,
                    cell_size,
                    cell_size
                )

                if maze_without_pass[y][x] == '#':
                    pygame.draw.rect(screen, (0, 0, 155), rect)
                elif maze_without_pass[y][x] == '1':
                    pygame.draw.rect(screen, (255, 0, 155), rect)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), rect)

                pygame.draw.rect(screen, (200, 200, 200), rect, 1)

        for y in range(2, height + 2):
            for x in range(2, width + 2):
                rect = pygame.Rect(
                    (x - 2) * cell_size + width * cell_size,
                    (y - 2) * cell_size,
                    cell_size,
                    cell_size
                )

                if maze[y][x] == '#':
                    pygame.draw.rect(screen, (0, 0, 155), rect)
                elif maze[y][x] == '1':
                    pygame.draw.rect(screen, (255, 0, 155), rect)
                elif maze[y][x] == 'f':
                    pygame.draw.rect(screen, (0, 255, 0), rect)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), rect)

                pygame.draw.rect(screen, (200, 200, 200), rect, 1)

        line_x = width * cell_size
        pygame.draw.line(screen, (0, 0, 0), (line_x, 0), (line_x, screen_height), 3)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
