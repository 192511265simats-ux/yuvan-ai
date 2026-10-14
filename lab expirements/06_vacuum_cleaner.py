"""
Day 1 - Program 6: Vacuum Cleaner Problem (CO3)
Simple reflex agent in a two-room world (A and B).
Rule: if the current room is dirty -> Suck; otherwise move to the other room.
"""


def vacuum_agent(location, status):
    """Percept = (location, status). Returns the action."""
    if status == "Dirty":
        return "Suck"
    return "Right" if location == "A" else "Left"


def run(world, location, max_steps=10):
    cost = 0
    print(f"Initial world: {world}, vacuum at room {location}\n")

    for step in range(1, max_steps + 1):
        if all(s == "Clean" for s in world.values()):
            print(f"\nBoth rooms are clean after {step - 1} steps. Total cost = {cost}")
            return

        status = world[location]
        action = vacuum_agent(location, status)
        print(f"Step {step}: Room {location} is {status:5s} -> Action: {action}")

        if action == "Suck":
            world[location] = "Clean"
        elif action == "Right":
            location = "B"
        else:
            location = "A"
        cost += 1

    print(f"\nFinal world: {world}, Total cost = {cost}")


if __name__ == "__main__":
    world = {"A": "Dirty", "B": "Dirty"}
    run(world, "A")
