import itertools

# Function to calculate the total distance of a path
def calculate_total_distance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i+1]]
    return total_distance

# Input the number of nodes
num_nodes = int(input("Enter the number of nodes: "))

# Initialize an empty graph as a dictionary
graph = {}

# Input the connections and weights
for i in range(num_nodes):
    node_name = input(f"Enter the name of node {i+1}: ")
    num_outgoing_connections = int(input(f"Enter the number of connections from {node_name}: "))
    connections = {}
    for j in range(num_outgoing_connections):
        connected_node, weight = input(f"Enter connected node and weight: ").split()
        connections[connected_node] = int(weight)
    graph[node_name] = connections

# Ask for the starting position
start_node = input("Enter the starting node: ")

# Generate all possible permutations of nodes starting from the specified node
nodes = list(graph.keys())
nodes.remove(start_node)
permutations = itertools.permutations(nodes)

# Initialize variables to track the shortest path and distance
shortest_path = None
shortest_distance = float('inf')

# Initialize a list to store the remaining paths
remaining_paths = []

# Find the shortest path and calculate the remaining paths
for perm in permutations:
    current_path = [start_node] + list(perm) + [start_node]
    total_distance = calculate_total_distance(current_path, graph)
    if total_distance < shortest_distance:
        shortest_path = current_path
        shortest_distance = total_distance
    remaining_paths.append((list(perm), total_distance))

# Print the shortest path and distance
print(f"Shortest Path: {' -> '.join(shortest_path)}")
print(f"Shortest Distance: {shortest_distance}")

# Print the remaining paths with their distances
for path, distance in remaining_paths:
    print(f"Remaining Path from {start_node} to {path[-1]}: {' -> '.join([start_node] + path + [start_node])}")
    print(f"Remaining Distance: {distance}")


