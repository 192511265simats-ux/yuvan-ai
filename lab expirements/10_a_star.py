"""
Day 1 - Program 10: A* Algorithm (CO4)
Finds the least-cost path using f(n) = g(n) + h(n), where
g(n) = cost from start to n, h(n) = heuristic estimate from n to goal.
"""
import heapq

# Weighted graph: node -> [(neighbour, edge cost), ...]
graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("B", 2), ("C", 5), ("D", 12)],
    "B": [("C", 2)],
    "C": [("D", 3), ("G", 7)],
    "D": [("G", 2)],
    "G": [],
}

# Heuristic values (estimated cost from each node to goal G)
heuristic = {"S": 7, "A": 6, "B": 4, "C": 4, "D": 2, "G": 0}


def a_star(graph, h, start, goal):
    open_list = [(h[start], 0, start, [start])]   # (f, g, node, path)
    best_g = {start: 0}

    while open_list:
        f, g, node, path = heapq.heappop(open_list)

        if node == goal:
            return path, g

        for neighbour, cost in graph[node]:
            new_g = g + cost
            if neighbour not in best_g or new_g < best_g[neighbour]:
                best_g[neighbour] = new_g
                heapq.heappush(open_list,
                               (new_g + h[neighbour], new_g, neighbour, path + [neighbour]))
    return None, float("inf")


if __name__ == "__main__":
    start, goal = "S", "G"
    path, cost = a_star(graph, heuristic, start, goal)

    if path:
        print(f"Start: {start}   Goal: {goal}")
        print("Path found :", " -> ".join(path))
        print("Total cost :", cost)
    else:
        print("No path found.")
