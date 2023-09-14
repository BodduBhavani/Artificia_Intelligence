from collections import deque

# Function to check if a state is valid
def is_valid_state(state, max_missionaries, max_cannibals):
    missionaries, cannibals, boat = state
    if (
        missionaries < 0
        or cannibals < 0
        or missionaries > max_missionaries
        or cannibals > max_cannibals
    ):
        return False
    if (
        missionaries < cannibals
        and missionaries > 0
    ):
        return False
    if (
        max_missionaries - missionaries < max_cannibals - cannibals
        and max_missionaries - missionaries > 0
    ):
        return False
    return True

# Function to generate valid next states
def generate_next_states(state, max_missionaries, max_cannibals):
    possible_moves = [
        (1, 0),  # Move 1 missionary
        (0, 1),  # Move 1 cannibal
        (2, 0),  # Move 2 missionaries
        (0, 2),  # Move 2 cannibals
        (1, 1),  # Move 1 missionary and 1 cannibal
    ]
    boat = state[2]
    next_states = []

    for move in possible_moves:
        if boat == 1:
            next_state = (
                state[0] - move[0],
                state[1] - move[1],
                0,
            )
        else:
            next_state = (
                state[0] + move[0],
                state[1] + move[1],
                1,
            )

        if (
            is_valid_state(next_state, max_missionaries, max_cannibals)
            and sum(move) > 0
            and sum(move) <= 2
        ):
            next_states.append((next_state, move))  # Include the move in next_states

    return next_states

# Breadth-First Search to solve the problem
def solve_missionaries_and_cannibals(max_missionaries, max_cannibals):
    start_state = (max_missionaries, max_cannibals, 1)
    goal_state = (0, 0, 0)
    visited = set()
    queue = deque([(start_state, [])])

    left_to_right = True  # Start with the boat moving from left to right

    while queue:
        current_state, path = queue.popleft()

        if current_state == goal_state:
            return path

        visited.add(current_state)

        for next_state, move in generate_next_states(
            current_state, max_missionaries, max_cannibals
        ):
            if next_state not in visited:
                new_path = path + [
                    (current_state, next_state, move)
                ]  # Add the boat movement
                queue.append((next_state, new_path))

        # Alternate the direction of the boat's movement
        left_to_right = not left_to_right

    return None

# Input the maximum number of missionaries and cannibals
print("The task is to move all of them to the right side of the river")
print("Rules:")
print("1. The boat can carry at most two people")
print("2. If cannibals number is greater than missionaries, then the cannibals would eat the missionaries")
print("3. The boat cannot cross the river by itself with no people on board")

max_missionaries = int(input("Enter the maximum number of missionaries: "))
max_cannibals = int(input("Enter the maximum number of cannibals: "))

if max_missionaries < 0 or max_cannibals < 0:
    print("Invalid input. The maximum number of missionaries and cannibals must be non-negative.")
else:
    solution = solve_missionaries_and_cannibals(max_missionaries, max_cannibals)

    if solution:
        print("Solution found:")
        for i, (from_state, to_state, move) in enumerate(solution):
            if i % 2 == 0:
                print(
                    f"Step {i + 1}: Move from left to right - {move} - {from_state} to {to_state}"
                )
            else:
                print(
                    f"Step {i + 1}: Move from right to left - {move} - {from_state} to {to_state}"
                )
    else:
        print("No solution found.")
