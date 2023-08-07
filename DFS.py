from collections import defaultdict, deque

def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    traversal_order = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            traversal_order.append(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order

# Function to create a graph from user input
def create_graph():
    graph = defaultdict(list)
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        source, destination = input("Enter an edge (source destination): ").split()
        graph[source].append(destination)
        graph[destination].append(source)  # Assuming an undirected graph

    return graph

# Function to get the starting node from user input
def get_start_node(graph):
    valid_nodes = graph.keys()
    start_node = input(f"Enter the starting node ({', '.join(valid_nodes)}): ")

    while start_node not in valid_nodes:
        print("Invalid starting node. Please choose from the available nodes.")
        start_node = input(f"Enter the starting node ({', '.join(valid_nodes)}): ")

    return start_node

if __name__ == "__main__":
    # Create the graph from user input
    graph = create_graph()

    # Get the starting node from user input
    start_node = get_start_node(graph)

    # Performing DFS traversal
    result = dfs(graph, start_node)

    # Display the DFS traversal order
    print("DFS Traversal Order:", result)