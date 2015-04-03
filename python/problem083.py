#!/usr/bin/python

"""Problem 83: Path sum: four ways"""

from utils import open_data_file
from heapq import heappush, heappop


def main():
    with open_data_file("matrix.txt") as data_file:
        matrix = [[int(x) for x in line.split(",")] for line in data_file]

    size = len(matrix)

    distances = [[float("inf")]*size for i in range(size)]

    heap = []
    heappush(heap, (matrix[0][0], 0, 0))  # distance, row, col

    # Dijkstra's algorithm, simplified
    while heap:
        distance, row, col = heappop(heap)
        neighbors = []

        if row > 0:
            neighbors.append((distance+matrix[row-1][col], row-1, col)),  # up
        if col < size-1:
            neighbors.append((distance+matrix[row][col+1], row, col+1)),  # right
        if row < size-1:
            neighbors.append((distance+matrix[row+1][col], row+1, col)),  # down
        if col > 0:
            neighbors.append((distance+matrix[row][col-1], row, col-1)),  # left

        for node in neighbors:
            if node[0] < distances[node[1]][node[2]]:
                heappush(heap, node)
                distances[node[1]][node[2]] = node[0]

        if row == col == size-1:
            return distance

if __name__ == "__main__":
    print(main())