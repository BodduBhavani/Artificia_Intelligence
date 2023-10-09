import sys

def tsp(mask, city):
    # Base case: All cities visited
    if mask == (1 << n) - 1:
        return distance[city][0], [city, 0]  # Return the distance and path
    
    # Initialize minimum distance and path
    min_distance = sys.maxsize
    min_path = []
    
    # Try to visit unvisited cities
    for nxt_city in range(n):
        if (mask & (1 << nxt_city)) == 0:
            new_mask = mask | (1 << nxt_city)
            new_distance, new_path = tsp(new_mask, nxt_city)
            new_distance += distance[city][nxt_city]
            if new_distance < min_distance:
                min_distance = new_distance
                min_path = [city] + new_path
    
    return min_distance, min_path

# Get the number of vertices (cities) from the user
n = int(input("Enter the number of vertices (cities): "))

# Initialize the names of vertices
vertices = []
print("Enter the names of vertices:")
for i in range(n):
    name = input(f"Enter the name of vertex {i + 1}: ")
    vertices.append(name)

# Initialize a dictionary to store the ending vertices for each vertex
ending_vertices = {}
for vertex in vertices:
    ending_vertex_names = input(f"Enter the ending vertices for {vertex} (comma-separated, e.g., A,B,C): ").split(",")
    ending_vertices[vertex] = ending_vertex_names

# Initialize the distance matrix
distance = [[0] * n for _ in range(n)]
print("Enter the distances between vertices:")
for i in range(n):
    for j in range(n):
        if i != j:
            if vertices[j] in ending_vertices[vertices[i]]:
                dist = int(input(f"Enter the distance from {vertices[i]} to {vertices[j]}: "))
                distance[i][j] = dist

start_vertex_name = input("Enter the starting vertex: ")
start_city = vertices.index(start_vertex_name)  # Starting city
initial_mask = 1  # Starting with the first city visited

# Call the TSP function
result_distance, result_path = tsp(initial_mask, start_city)

# Print the minimum distance
print("Minimum Distance:", result_distance)

# Print the path of Vertices using arrow marks
print("Path of Vertices:")
for i, city in enumerate(result_path):
    if i < len(result_path) - 1:
        print(vertices[city], end=" -> ")
    else:
        print(vertices[city])
