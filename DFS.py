def dfs(graph, current_node, goal_node, visited, path):
    if current_node == goal_node:
        return True
    
    visited.add(current_node)
    
    for neighbor in graph.get(current_node, []):
        if neighbor not in visited:
            if dfs(graph, neighbor, goal_node, visited, path):
                path.append(neighbor)
                return True
    
    return False

def main():
    graph = {}
    
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        node1, node2 = input("Enter nodes for an edge (space-separated): ").split()
        if node1 not in graph:
            graph[node1] = []
        graph[node1].append(node2)
    
    # Input nodes
    nodes = list(graph.keys())
    print("Available nodes:", nodes)
    
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    
    visited_nodes = set()
    path = [start_node]
    
    if dfs(graph, start_node, goal_node, visited_nodes, path):
        print("Path from", start_node, "to", goal_node, ":", " -> ".join(path))
    else:
        print("No path found from", start_node, "to", goal_node)

if __name__ == "__main__":
    main()
