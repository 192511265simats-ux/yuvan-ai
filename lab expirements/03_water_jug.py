"""
Day 1 - Program 3: Water Jug Problem (CO2)
Solved using Breadth-First Search over (jug1, jug2) states.
"""
from collections import deque


def water_jug(cap1, cap2, target):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (a, b), path = queue.popleft()

        if a == target or b == target:
            return path

        pour_1_to_2 = min(a, cap2 - b)
        pour_2_to_1 = min(b, cap1 - a)

        next_states = [
            (cap1, b),                      # fill jug 1
            (a, cap2),                      # fill jug 2
            (0, b),                         # empty jug 1
            (a, 0),                         # empty jug 2
            (a - pour_1_to_2, b + pour_1_to_2),  # pour jug 1 -> jug 2
            (a + pour_2_to_1, b - pour_2_to_1),  # pour jug 2 -> jug 1
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [state]))
    return None


if __name__ == "__main__":
    cap1, cap2, target = 4, 3, 2
    print(f"Jug 1 capacity = {cap1}L, Jug 2 capacity = {cap2}L, Target = {target}L\n")

    solution = water_jug(cap1, cap2, target)
    if solution:
        print("Steps (Jug1, Jug2):")
        for i, state in enumerate(solution):
            print(f"  Step {i}: {state}")
        print(f"\nTarget reached in {len(solution) - 1} steps.")
    else:
        print("No solution possible.")
