from collections import defaultdict

def dfs(graph, current_node, goal_node, visited, path):
    if current_node == goal_node:
        return path

    visited.add(current_node)

    for neighbor in graph[current_node]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal_node, visited, path + [neighbor])
            if new_path:
                return new_path

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
    path = dfs(graph, start_node, goal_node, set(), [start_node])
    if path:
        print("Path from", start_node, "to", goal_node, ":", " -> ".join(path))
    else:
        print("No path found from", start_node, "to", goal_node)
