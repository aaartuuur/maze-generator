import random


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False


def generate_maze_kruskal(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]

    # Создаем список всех возможных стен
    edges = []
    for y in range(1, height - 1, 2):
        for x in range(1, width - 1, 2):
            maze[y][x] = ' '
            if x + 2 < width - 1:
                edges.append((x, y, x + 2, y))
            if y + 2 < height - 1:
                edges.append((x, y, x, y + 2))

    random.shuffle(edges)

    # Используем Union-Find для проверки циклов
    uf = UnionFind(width * height)

    for x1, y1, x2, y2 in edges:
        idx1 = y1 * width + x1
        idx2 = y2 * width + x2

        if uf.union(idx1, idx2):
            # Убираем стену между клетками
            maze[(y1 + y2) // 2][(x1 + x2) // 2] = ' '

    return maze