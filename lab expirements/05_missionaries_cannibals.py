"""
Day 1 - Program 5: Missionaries and Cannibals Problem (CO3)
Solved using Breadth-First Search.
State = (missionaries on left, cannibals on left, boat side)
boat side: 1 = left bank, 0 = right bank
"""
from collections import deque

TOTAL_M = 3
TOTAL_C = 3
BOAT_CAPACITY = 2


def is_valid(m, c):
    """Missionaries must never be outnumbered by cannibals on either bank."""
    if not (0 <= m <= TOTAL_M and 0 <= c <= TOTAL_C):
        return False
    if m != 0 and m < c:                       # left bank
        return False
    right_m, right_c = TOTAL_M - m, TOTAL_C - c
    if right_m != 0 and right_m < right_c:     # right bank
        return False
    return True


def get_successors(state):
    m, c, boat = state
    successors = []
    for dm in range(BOAT_CAPACITY + 1):
        for dc in range(BOAT_CAPACITY + 1 - dm):
            if dm + dc == 0:
                continue
            if boat == 1:   # boat moves left -> right
                new_state = (m - dm, c - dc, 0)
                action = f"Move {dm}M {dc}C  left -> right"
            else:           # boat moves right -> left
                new_state = (m + dm, c + dc, 1)
                action = f"Move {dm}M {dc}C  right -> left"
            if is_valid(new_state[0], new_state[1]):
                successors.append((new_state, action))
    return successors


def solve():
    start = (TOTAL_M, TOTAL_C, 1)
    goal = (0, 0, 0)
    queue = deque([(start, [(start, "Start")])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for nxt, action in get_successors(state):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [(nxt, action)]))
    return None


if __name__ == "__main__":
    solution = solve()
    if solution:
        print("State format: (M_left, C_left, Boat side [1=left, 0=right])\n")
        for step, (state, action) in enumerate(solution):
            print(f"Step {step:2d}: {state}   {action}")
        print(f"\nEveryone crossed safely in {len(solution) - 1} moves.")
    else:
        print("No solution found.")
