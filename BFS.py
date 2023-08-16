from collections import defaultdict, deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        node, path = queue.popleft()

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))

    return None

# Input graph nodes and edges
graph = defaultdict(list)
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    u, v = input("Enter edge (u v): ").split()
    graph[u].append(v)
    graph[v].append(u)

# Input nodes
nodes = list(graph.keys())
print("Available nodes:", nodes)

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

if start_node not in nodes or goal_node not in nodes:
    print("Invalid nodes entered.")
else:
    path = bfs(graph, start_node, goal_node)
    if path:
        print("Path from", start_node, "to", goal_node, ":", " -> ".join(path))
    else:
        print("No path found from", start_node, "to", goal_node)
