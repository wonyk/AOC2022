#!/usr/bin/env python3


def get_neighbours(grid, node, h, w, reverse=False):
    row, col = node
    max_height = grid[row][col] + 1
    min_height = grid[row][col] - 1

    reachable = []

    for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
        if 0 <= r < h and 0 <= c < w:
            if reverse and grid[r][c] >= min_height:
                reachable.append((r, c))
            elif not reverse and grid[r][c] <= max_height:
                reachable.append((r, c))
    return reachable


def bfs(grid, start, end, reverse):

    visited = set()
    queue = [(0, start)]
    h = len(grid)
    w = len(grid[0])

    while queue:
        dist, node = queue.pop(0)

        row, col = node

        if node == end or grid[row][col] == end:
            return dist

        if node not in visited:
            visited.add(node)

            for neighbour in get_neighbours(grid, node, h, w, reverse):
                if neighbour in visited:
                    continue
                queue.append((dist + 1, neighbour))

    print("Not found")
    return 0


def main():
    inp = open("input", "rb").read().splitlines()

    grid = [[c for c in line] for line in inp]

    start = None
    end = None

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == ord("S"):
                start = (i, j)
                grid[i][j] = ord("a")
            elif col == ord("E"):
                end = (i, j)
                grid[i][j] = ord("z")

    p1_result = bfs(grid, start, end, reverse=False)
    print(f"Part 1: {p1_result}")

    start = end
    end = ord("a")

    p2_result = bfs(grid, start, end, reverse=True)
    print(f"Part 2: {p2_result}")


if __name__ == "__main__":
    main()
