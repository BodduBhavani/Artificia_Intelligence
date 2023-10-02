from itertools import permutations

# Function to calculate the total weight of a path in the graph
def calculatePathWeight(graph, path):
    total_weight = 0
    for i in range(len(path) - 1):
        from_vertex = path[i]
        to_vertex = path[i + 1]
        total_weight += graph[from_vertex][to_vertex]
    total_weight += graph[path[-1]][path[0]]  # Return to the starting point
    return total_weight

# Function to solve the Traveling Salesman Problem using a naive approach
def tsp_naive(graph):
    V = len(graph)
    min_weight = float('inf')
    optimal_path = []

    # Generate all possible permutations of cities
    all_permutations = permutations(range(V))

    for path in all_permutations:
        weight = calculatePathWeight(graph, path)
        if weight < min_weight:
            min_weight = weight
            optimal_path = list(path)

    return min_weight, optimal_path

# Function to get the user-provided graph as a list of edge weights
def getGraphFromUser(V):
    graph = []
    print("Enter the edge weights for the graph:")
    for i in range(V):
        row = [int(x) for x in input(f"Enter edge weights for vertex {i + 1} (e.g., 0 10 15 20): ").split()]
        graph.append(row)
    return graph

if __name__ == "__main__":
    # Get the user-provided value of 'V'
    V = int(input("Enter the number of vertices (V): "))

    # Get the user-provided graph as a list of edge weights
    user_graph = getGraphFromUser(V)

    # Calculate the total weight and print the optimal TSP path using the naive approach
    min_weight, optimal_path = tsp_naive(user_graph)
    print("Total Weight of Optimal TSP Path (Naive Approach):", min_weight)
    print("Optimal TSP Path (Naive Approach):", optimal_path)
