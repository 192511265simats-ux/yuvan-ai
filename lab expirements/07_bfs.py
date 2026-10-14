"""
Day 1 - Program 7: Breadth-First Search (CO3)
Explores a graph level by level using a queue (FIFO).
"""
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}


def bfs(graph, start):
    visited = [start]
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited


def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(path + [neighbour])
    return None


if __name__ == "__main__":
    print("Graph (adjacency list):", graph)
    print("\nBFS traversal from A :", " -> ".join(bfs(graph, "A")))
    print("Shortest path A to F :", " -> ".join(bfs_shortest_path(graph, "A", "F")))
