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



def generate_maze_backtracker_without_recursion(width, height, size_room = 0, exit_count = 0):
    maze = [['#' for _ in range(width)] for _ in range(height)]

    steck = [(1, 1)]

    while steck:
        x, y = steck[-1]
        maze[y][x] = ' '

        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)

        f = False
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 < nx < width - 1 and 0 < ny < height - 1
                    and not (width // 2 - size_room // 2 - (size_room//2)%2 <= nx <= width // 2 + size_room // 2 + (size_room//2+1)%2
                    and height//2-size_room//2 - (size_room//2+1)%2-1 <= ny <= height//2+size_room//2 +(size_room//2)%2)
                    and maze[ny][nx] == '#'):
                maze[y + dy // 2][x + dx // 2] = ' '
                steck.append((nx, ny))
                f = True
                break

        if not f:
            steck.pop()

    for y in range(height // 2 - size_room // 2 - (size_room // 2 + 1) % 2,
                   height // 2 + size_room // 2 + (size_room // 2) % 2):
        for x in range(width // 2 - size_room // 2 - (size_room // 2) % 2 + 1,
                       width // 2 + size_room // 2 + (size_room // 2 + 1) % 2 + 1):
            maze[y][x] = ' '

    for i in range(width):
        for j in (0, 1, height - 2, height - 1):
            maze[j][i] = ' '
            maze[i][j] = ' '

    maze[height // 2 - 1][width // 2 - size_room // 2 - (size_room // 2) % 2] = ' '
    maze[height // 2 - 1][width // 2 + size_room // 2 + (size_room // 2 + 1) % 2 + 1] = ' '
    maze[height // 2 - size_room // 2 - (size_room // 2 + 1) % 2 - 1][width // 2 + 1] = ' '
    maze[height // 2 + size_room // 2 + (size_room // 2) % 2][width // 2 + 1] = ' '
    return maze
