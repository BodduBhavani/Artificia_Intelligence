def valid_state(state):
    m_left, c_left, m_right, c_right, side = state
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    return True

def print_state(state):
    m_left, c_left, m_right, c_right, side = state
    print(f"Left side: {m_left}M {c_left}C | Right side: {m_right}M {c_right}C | Boat: {'Left' if side == 0 else 'Right'}")

def solve(initial_state):
    m_left, c_left, _, _, _ = initial_state
    print("Initial state:")
    print_state(initial_state)
    print("\n")

    visited_states = set()
    stack = [(*initial_state, None)]

    while stack:
        m_left, c_left, m_right, c_right, side, prev_action = stack.pop()

        if (m_left, c_left, m_right, c_right, side) in visited_states:
            continue
        
        visited_states.add((m_left, c_left, m_right, c_right, side))

        if m_left == 0 and c_left == 0:
            print("Goal state reached:")
            print_state((m_left, c_left, m_right, c_right, side))
            break

        for action in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
            if prev_action is not None and action[0] == -prev_action[0] and action[1] == -prev_action[1]:
                continue
            
            new_m_left = m_left - action[0]
            new_c_left = c_left - action[1]
            new_m_right = m_right + action[0]
            new_c_right = c_right + action[1]
            new_side = 1 - side  # Toggle the side of the boat
            new_state = (new_m_left, new_c_left, new_m_right, new_c_right, new_side)

            if valid_state(new_state):
                if side == 0 and new_side == 1:
                    boat_direction = "from Left to Right"
                else:
                    boat_direction = "from Right to Left"
                
                print(f"Move Boat {boat_direction}: {action[0]}M {action[1]}C")
                print_state(new_state)
                stack.append((*new_state, action))

# Take user inputs for the number of missionaries and cannibals
m = int(input("Enter the number of missionaries: "))
c = int(input("Enter the number of cannibals: "))
initial_state = (m, c, 0, 0, 0)  # The boat starts on the left side

# Initialize the problem with the user input values
solve(initial_state)
