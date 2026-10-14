"""
Day 1 - Program 1: 8-Puzzle Problem (CO1)
Solved using the A* search algorithm with the Manhattan-distance heuristic.
0 represents the blank tile.
"""
import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def manhattan(state):
    """Sum of distances of every tile from its goal position."""
    dist = 0
    for idx, tile in enumerate(state):
        if tile != 0:
            goal_idx = GOAL.index(tile)
            dist += abs(idx // 3 - goal_idx // 3) + abs(idx % 3 - goal_idx % 3)
    return dist


def is_solvable(state):
    """A 3x3 puzzle is solvable only if the number of inversions is even."""
    tiles = [t for t in state if t != 0]
    inversions = sum(1 for i in range(len(tiles))
                     for j in range(i + 1, len(tiles)) if tiles[i] > tiles[j])
    return inversions % 2 == 0


def get_neighbors(state):
    """Generate all states reachable by sliding one tile into the blank."""
    neighbors = []
    blank = state.index(0)
    row, col = divmod(blank, 3)
    moves = {"Up": (-1, 0), "Down": (1, 0), "Left": (0, -1), "Right": (0, 1)}
    for name, (dr, dc) in moves.items():
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new = list(state)
            swap = nr * 3 + nc
            new[blank], new[swap] = new[swap], new[blank]
            neighbors.append((tuple(new), name))
    return neighbors


def solve(start):
    if not is_solvable(start):
        return None
    open_list = [(manhattan(start), 0, start, [])]
    visited = set()
    while open_list:
        f, g, state, path = heapq.heappop(open_list)
        if state == GOAL:
            return path, g
        if state in visited:
            continue
        visited.add(state)
        for nxt, move in get_neighbors(state):
            if nxt not in visited:
                heapq.heappush(open_list,
                               (g + 1 + manhattan(nxt), g + 1, nxt, path + [(move, nxt)]))
    return None


def print_state(state):
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x != 0 else "_" for x in state[i:i + 3]))
    print()


if __name__ == "__main__":
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)

    print("Initial state:")
    print_state(start_state)

    result = solve(start_state)
    if result is None:
        print("This puzzle is not solvable.")
    else:
        path, cost = result
        for step, (move, state) in enumerate(path, 1):
            print(f"Step {step}: Move blank {move}")
            print_state(state)
        print(f"Solved in {cost} moves.")
