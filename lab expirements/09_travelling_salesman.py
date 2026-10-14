"""
Day 1 - Program 9: Travelling Salesman Problem (CO4)
Brute-force approach: try every possible tour starting from city 0
and keep the one with the minimum total distance.
"""
from itertools import permutations

# Symmetric distance matrix between 4 cities (0, 1, 2, 3)
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]


def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += dist[tour[i]][tour[i + 1]]
    return cost


def tsp(dist, start=0):
    n = len(dist)
    cities = [c for c in range(n) if c != start]
    best_cost = float("inf")
    best_tour = None

    for perm in permutations(cities):
        tour = [start] + list(perm) + [start]   # return to the starting city
        cost = tour_cost(tour)
        if cost < best_cost:
            best_cost, best_tour = cost, tour
    return best_tour, best_cost


if __name__ == "__main__":
    print("Distance matrix:")
    for row in dist:
        print("  ", row)

    tour, cost = tsp(dist)
    print("\nShortest tour :", " -> ".join(map(str, tour)))
    print("Minimum cost  :", cost)
