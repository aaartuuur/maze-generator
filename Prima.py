import random
from collections import deque
from heapq import heappush, heappop


class MazeGenerator:
    def __init__(self, size=21, size_room=5, count_exit=4):
        self.size = size
        self.size_room = size_room
        self.count_exit = count_exit
        self.maze = None

    def generate_maze_prim(self):
        size = self.size
        size_room = self.size_room
        count_exit = self.count_exit

        self.maze = [['#' for _ in range(size)] for _ in range(size)]
        center_offset = (size_room // 2) % 2 + (size // 2) % 2
        room_half = size_room // 2
        size_half = size // 2

        room_start = size_half - room_half + center_offset - 1
        room_end = size_half + room_half + center_offset
        start_x, start_y = room_start - 2, room_start - 2
        self.maze[start_y][start_x] = ' '

        frontiers = []

        for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
            nx, ny = start_x + dx, start_y + dy
            if 0 < nx < size - 1 and 0 < ny < size - 1:
                heappush(frontiers, (random.random(), nx, ny, start_x, start_y))

        while frontiers:
            _, x, y, px, py = heappop(frontiers)

            if self.maze[y][x] == '#':

                self.maze[y][x] = ' '
                self.maze[(y + py) // 2][(x + px) // 2] = ' '

                for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
                    nx, ny = x + dx, y + dy
                    if (0 < nx < size - 1 and 0 < ny < size - 1
                            and not (room_start <= nx <= room_end
                                     and room_start <= ny <= room_end)
                            and self.maze[ny][nx] == '#'):
                        heappush(frontiers, (random.random(), nx, ny, x, y))

        for y in range(room_start, room_end):
            for x in range(room_start, room_end):
                self.maze[y][x] = '1'

        up = []
        down = []
        left = []
        right = []
        for i in range(room_start, room_end, 2):
            up.append([room_start - 1, i])
            down.insert(0, [room_end, i])
            left.insert(0, [i, room_start - 1])
            right.append([i, room_end])

        perimetr = up + right + down + left

        step = len(perimetr) / count_exit
        for i in range(count_exit):
            self.maze[perimetr[int(i * step)][0]][perimetr[int(i * step)][1]] = ' '

        for i in range(size):
            for j in (0, 1, size - 2, size - 1):
                self.maze[j][i] = '#'
                self.maze[i][j] = '#'

        return self.maze

    def find_all_paths(self):
        size=self.size
        size_half=size//2
        count_input = 0
        incorrect_input = []

        for i in range(2, size - 3):
            if self.maze[i][2] == ' ':
                incorrect_input.append(self.find_shortest_path((i, 2), (size_half, size_half)))
                count_input += 1
            if self.maze[size - 3][i] == ' ':
                incorrect_input.append(self.find_shortest_path((size - 3, i), (size_half, size_half)))
                count_input += 1
            if self.maze[i][size - 3] == ' ':
                incorrect_input.append(self.find_shortest_path((i, size - 3), (size_half, size_half)))
                count_input += 1
            if self.maze[2][i] == ' ':
                incorrect_input.append(self.find_shortest_path((2, i), (size_half, size_half)))
                count_input += 1
        print("Всего входов: ", count_input)
        incorrect=0
        for start in incorrect_input:
            if start is not None:
                incorrect+=1
                self.find_shortest_path(start, (size_half, size_half))

    def find_shortest_path(self, start, end):
        if self.maze is None:
            return None

        rows = len(self.maze)
        cols = len(self.maze[0])

        if (start[0] < 0 or start[0] >= rows or start[1] < 0 or start[1] >= cols or
                end[0] < 0 or end[0] >= rows or end[1] < 0 or end[1] >= cols):
            return None

        if self.maze[start[0]][start[1]] == '#' or self.maze[end[0]][end[1]] == '#':
            return None

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        queue = deque([(start[0], start[1], [start])])
        visited = set([start])

        while queue:
            x, y, path = queue.popleft()

            if (x, y) == end:
                for x, y in path[0:-1]:
                    if self.maze[x][y] != 'f':
                        self.maze[x][y] = '1'
                return None

            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy

                if (0 <= new_x < rows and 0 <= new_y < cols and
                        (self.maze[new_x][new_y] == ' ' or self.maze[new_x][new_y] == '1' or self.maze[new_x][new_y] == 'f') and
                        (new_x, new_y) not in visited):
                    new_path = path + [(new_x, new_y)]
                    queue.append((new_x, new_y, new_path))
                    visited.add((new_x, new_y))

        #ломаем стенку если прохода нетБ
        y_end, x_end = path[-1]
        if 2 == y_end or y_end == self.size-3 or 2 == x_end or x_end == self.size-3:
            start_x, start_y = start
            center_x, center_y = end
            if abs(center_x - start_x) > abs(center_y - start_y):
                dx = 1 if center_x > start_x else -1 if center_x < start_x else 0
                dy = 0
            else:
                dx = 0
                dy = 1 if center_y > start_y else -1 if center_y < start_y else 0

            current_x, current_y = start_x + dx, start_y + dy

            while (0 <= current_x < rows and 0 <= current_y < cols):
                if self.maze[current_x][current_y] == '#':
                    self.maze[current_x][current_y] = 'f'
                    break
                current_x += dx
                current_y += dy
        else:
            y_before, x_before = path[-2]
            self.maze[min(max(2 * y_end - y_before, 0), self.size - 1)][
                min(max(2 * x_end - x_before, 0), self.size - 1)] = 'f'
        return start
