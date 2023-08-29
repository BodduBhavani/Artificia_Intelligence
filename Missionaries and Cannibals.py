def valid_state(m_left, c_left, m_right, c_right):
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    return True

def print_state(m_left, c_left, m_right, c_right):
    print(f"Left side: {m_left}M {c_left}C | Right side: {m_right}M {c_right}C")

def solve(m_left, c_left, m_right, c_right):
    print("Initial state:")
    print_state(m_left, c_left, m_right, c_right)
    print("\n")

    visited_states = set()
    stack = [(m_left, c_left, m_right, c_right, None)]

    while stack:
        m_left, c_left, m_right, c_right, prev_action = stack.pop()

        if (m_left, c_left, m_right, c_right) in visited_states:
            continue
        
        visited_states.add((m_left, c_left, m_right, c_right))

        if m_left == 0 and c_left == 0:
            print("Goal state reached:")
            print_state(m_left, c_left, m_right, c_right)
            break

        for action in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
            if prev_action is not None and action[0] == -prev_action[0] and action[1] == -prev_action[1]:
                continue
            
            new_m_left = m_left - action[0]
            new_c_left = c_left - action[1]
            new_m_right = m_right + action[0]
            new_c_right = c_right + action[1]

            if valid_state(new_m_left, new_c_left, new_m_right, new_c_right):
                print(f"Move: {action[0]}M {action[1]}C")
                print_state(new_m_left, new_c_left, new_m_right, new_c_right)
                stack.append((new_m_left, new_c_left, new_m_right, new_c_right, action))

# Take user inputs for the number of missionaries and cannibals
m = int(input("Enter the number of missionaries: "))
c = int(input("Enter the number of cannibals: "))

# Initialize the problem with the user input values
solve(m, c, 0, 0)
