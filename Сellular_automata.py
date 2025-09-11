import random

def generate_maze_cellular(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]

    def cellular():
        for y in range(1, height - 1):
            for x in range(1, width - 1):
                maze[y][x] = '#' if random.random() < 0.4 else ' '

        for _ in range(5):
            new_maze = [row[:] for row in maze]

            for y in range(1, height - 1):
                for x in range(1, width - 1):
                    wall_count = 0
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            if dx == 0 and dy == 0:
                                continue
                            if maze[y + dy][x + dx] == '#':
                                wall_count += 1

                    if maze[y][x] == '#' and wall_count < 3:
                        new_maze[y][x] = ' '
                    elif maze[y][x] == ' ' and wall_count > 4:
                        new_maze[y][x] = '#'

            maze[:] = new_maze

    cellular()
    return maze