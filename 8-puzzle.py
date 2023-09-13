from heapq import heappop, heappush

def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                goal_position = [(x, y) for x in range(3) for y in range(3) if goal[x][y] == tile][0]
                distance += abs(i - goal_position[0]) + abs(j - goal_position[1])
    return distance

class Node:
    def __init__(self, state, g, h, parent):
        self.state = state
        self.g = g
        self.h = h
        self.parent = parent

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

def get_neighbors(state):
    neighbors = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    blank_x, blank_y = None, None
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                blank_x, blank_y = i, j
    for dx, dy in directions:
        new_x, new_y = blank_x + dx, blank_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[blank_x][blank_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[blank_x][blank_y]
            neighbors.append(new_state)
    return neighbors

def backtrack_solution(node):
    path = []
    while node is not None:
        path.append(node.state)
        node = node.parent
    path.reverse()
    return path

def input_puzzle(prompt):
    print(prompt)
    state = []
    for i in range(3):
        row = list(map(int, input().split()))
        state.append(row)
    return state

def solve_puzzle(start_state, goal_state):
    open_list = [Node(start_state, 0, manhattan_distance(start_state, goal_state), None)]
    closed_set = set()

    while open_list:
        current_node = heappop(open_list)
        current_state = current_node.state
        closed_set.add(tuple(map(tuple, current_state)))

        if current_state == goal_state:
            return backtrack_solution(current_node)

        for neighbor_state in get_neighbors(current_state):
            if tuple(map(tuple, neighbor_state)) not in closed_set:
                g = current_node.g + 1
                h = manhattan_distance(neighbor_state, goal_state)
                f = g + h
                heappush(open_list, Node(neighbor_state, g, h, current_node))

    return None  # No solution found

print("Enter the start state (3x3 grid, each row space-separated):")
start_state = input_puzzle("")

print("Enter the goal state (3x3 grid, each row space-separated):")
goal_state = input_puzzle("")

solution = solve_puzzle(start_state, goal_state)
if solution:
    print("Solution found:")
    for state in solution:
        for row in state:
            print(row)
        print()
else:
    print("No solution found.")
