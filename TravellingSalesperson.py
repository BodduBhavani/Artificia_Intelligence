from sys import maxsize

# Function to calculate the total weight of a path in the graph
def calculatePathWeight(graph, path):
    V = len(graph)
    total_weight = 0
    for i in range(V - 1):
        from_vertex = path[i]
        to_vertex = path[i + 1]
        total_weight += graph[from_vertex][to_vertex]
    total_weight += graph[path[-1]][path[0]]  # Return to the starting point
    return total_weight

# Function to solve the Traveling Salesman Problem using dynamic programming
def tsp(graph):
    V = len(graph)
    # dp[mask][i] represents the minimum cost to reach vertex i, covering all vertices in the mask
    dp = [[maxsize] * V for _ in range(1 << V)]
    dp[1][0] = 0  # Starting from vertex 0

    for mask in range(1, 1 << V):
        for u in range(V):
            if (mask & (1 << u)) != 0:
                for v in range(V):
                    if u != v and (mask & (1 << v)) != 0:
                        dp[mask][u] = min(dp[mask][u], dp[mask ^ (1 << u)][v] + graph[v][u])

    # Find the minimum path from the last vertex back to vertex 0
    mask = (1 << V) - 1
    min_path = min(dp[mask][v] + graph[v][0] for v in range(1, V))

    return min_path

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

    # Calculate and print the total weight of the optimal TSP path
    result = tsp(user_graph)
    print("Total Weight of Optimal TSP Path:", result)
