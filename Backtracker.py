import random


def generate_maze_backtracker(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]

    def punch(x, y):
        maze[y][x] = ' '

        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == '#':
                maze[y + dy // 2][x + dx // 2] = ' '
                punch(nx, ny)

    punch(1, 1)
    return maze