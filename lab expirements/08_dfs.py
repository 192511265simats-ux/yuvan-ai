"""
Day 1 - Program 8: Depth-First Search (CO4)
Explores a graph as deep as possible before backtracking (recursive + iterative).
"""

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}


def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = []
    visited.append(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs_recursive(graph, neighbour, visited)
    return visited


def dfs_iterative(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # reverse so that the left-most neighbour is explored first
            stack.extend(reversed(graph[node]))
    return visited


if __name__ == "__main__":
    print("Graph (adjacency list):", graph)
    print("\nDFS (recursive) from A:", " -> ".join(dfs_recursive(graph, "A")))
    print("DFS (iterative) from A:", " -> ".join(dfs_iterative(graph, "A")))
