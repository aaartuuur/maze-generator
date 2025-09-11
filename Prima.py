import random
from heapq import heappush, heappop


def generate_maze_prim(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]

    start_x, start_y = 1, 1
    maze[start_y][start_x] = ' '

    frontiers = []

    for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
        nx, ny = start_x + dx, start_y + dy
        if 0 < nx < width - 1 and 0 < ny < height - 1:
            heappush(frontiers, (random.random(), nx, ny, start_x, start_y))
            #используется чтобы класть в кучу с помощью рандомного приоритета,
            # а не перемешивать после каждого нового элемента

    while frontiers:
        _, x, y, px, py = heappop(frontiers)

        if maze[y][x] == '#':

            maze[y][x] = ' '

            maze[(y + py) // 2][(x + px) // 2] = ' '

            for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
                nx, ny = x + dx, y + dy
                if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == '#':
                    heappush(frontiers, (random.random(), nx, ny, x, y))

    return maze