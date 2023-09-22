
from collections import deque
def generatenextstates(state, m, n):
    m_left, c_left, boat, m_right, c_right = state
    moves = [(0, 1), (0, 2), (1,0), (2, 0), (1, 1)]
    possible_states = []

    for i in moves:
        if boat == 1:
            move_str = str(i[0]) + "M " + str(i[1]) + "C move from left to right"
            new_state = (m_left - i[0], c_left - i[1], 0, m_right + i[0], c_right + i[1])
        else:
            move_str = str(i[0]) + "M " + str(i[1]) + "C  move from right to left"
            new_state = (m_left + i[0], c_left + i[1], 1, m_right - i[0], c_right - i[1])

        if checkvalidstate(new_state, m, n):
            possible_states.append((new_state, move_str))

    return possible_states
def checkvalidstate(state, m, n):
    m_left, c_left, boat, m_right, c_right = state

    if (
        0 <= m_left <= m and
        0 <= c_left <= n and
        0 <= m_right <= m and
        0 <= c_right <= n and
        (m_left == 0 or m_left >= c_left) and
        (m_right == 0 or m_right >= c_right)):
        return True

    return False
def bfs(m, n):
    initial_state = (m, n, 1, 0, 0)
    visited = set()
    queue = deque()
    queue.append((initial_state, []))

    while queue:
        current_state, path = queue.popleft()
        visited.add(current_state)

        if checkfinalstate(current_state, m):
            return path

        for next_state, move_description in generatenextstates(current_state, m, n):
            if next_state not in visited:
                queue.append((next_state, path + [(next_state, move_description)]))
def checkfinalstate(state, m):
    return state == (0, 0, 0, m, m)
def  path(s):
    print("Initial state:")
    print("Boat position:left")
    print("left side of river:",m,"M",n,"C")
    print("right side of river:",0,"M",0,"C")
    for i in range(len(s)):
        state, move_description = s[i]
        m_left, c_left, boat, m_right, c_right = state
        if boat == 1:
            boat_position = "left"
        else:
            boat_position="right"
        print("Step", i + 1,":")
        print(move_description)
        print(" Left side of river:", m_left, "M", c_left, "C" )
        print("Right side of river:", m_right, "M", c_right, "C ")
        print(" Boat position:", boat_position)
m = int(input("Enter the number of missionaries (m): "))
n = int(input("Enter the number of cannibals (n): "))
solution = bfs(m, n)
if solution:
    print("Solution found!")
    path(solution)
else:
    print("No solution found")



