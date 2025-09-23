import random
from collections import deque
from heapq import heappush, heappop


def generate_maze_prim(size, size_room, count_exit):
    maze = [['#' for _ in range(size)] for _ in range(size)]

    start_x, start_y = 1, 1
    maze[start_y][start_x] = ' '

    frontiers = []

    for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
        nx, ny = start_x + dx, start_y + dy
        if 0 < nx < size - 1 and 0 < ny < size - 1:
            heappush(frontiers, (random.random(), nx, ny, start_x, start_y))

    center_offset = (size_room // 2) % 2 + (size // 2) % 2
    room_half = size_room // 2
    size_half = size // 2

    room_start = size_half - room_half + center_offset - 1
    room_end = size_half + room_half + center_offset

    while frontiers:
        _, x, y, px, py = heappop(frontiers)

        if maze[y][x] == '#':

            maze[y][x] = ' '
            maze[(y + py) // 2][(x + px) // 2] = ' '

            for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
                nx, ny = x + dx, y + dy
                if (0 < nx < size - 1 and 0 < ny < size - 1
                        and not (room_start <= nx <= room_end
                                 and room_start <= ny <= room_end)
                        and maze[ny][nx] == '#'):
                    heappush(frontiers, (random.random(), nx, ny, x, y))

    for y in range(room_start, room_end):
        for x in range(room_start, room_end):
            maze[y][x] = '1'

    up = []
    down = []
    left = []
    right = []
    for i in range(room_start, room_end, 2):
        up.append([room_start-1, i])
        down.insert(0, [room_end, i])
        left.insert(0, [i, room_start-1])
        right.append([i, room_end])

    perimetr = up + right + down + left

    step = len(perimetr) / count_exit
    for i in range(count_exit):
        maze[perimetr[int(i * step)][0]][perimetr[int(i * step)][1]] = ' '


    for i in range(size):
        for j in (0, 1, size - 2, size - 1):
            maze[j][i] = ' '
            maze[i][j] = ' '

    maze = find_shortest_path(maze, (size_half - 1, 1), (size_half, size_half))
    maze = find_shortest_path(maze, (size_half - 1, size - 2), (size_half, size_half))
    maze = find_shortest_path(maze, (1, size_half), (size_half, size_half))
    maze = find_shortest_path(maze, (size - 2, size_half - 1), (size_half, size_half))

    return maze


def find_shortest_path(maze, start, end):
    rows = len(maze)
    cols = len(maze[0])

    if (start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols or
            end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols):
        return None

    if maze[start[0]][start[1]] == '#' or maze[end[0]][end[1]] == '#':
        return None

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    queue = deque([(start[0], start[1], [start])])
    visited = set([start])

    while queue:
        x, y, path = queue.popleft()

        if (x, y) == end:
            for x, y in path[1:-1]:
                maze[x][y] = '1'
            return maze

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if (0 <= new_x < rows and 0 <= new_y < cols and
                    (maze[new_x][new_y] == ' ' or maze[new_x][new_y] == '1') and (new_x, new_y) not in visited):
                new_path = path + [(new_x, new_y)]
                queue.append((new_x, new_y, new_path))
                visited.add((new_x, new_y))

    return None