# Minimum spanning tree (Kruskal algorithm)

This project implements the Kruskal algorithm for finding the minimum spanning tree in a weighted graph and displays the results on a graph using the `matplotlib` and `networkx` libraries.

## Usage.

1. Select the graph for which you want to find the minimum spanning tree.
2. Define the edges of the graph and their weights in the form of a list of `edges`.
3. Set the number of graph vertices in the variable `n`.
4. Run the code and it will find the minimum spanning tree and display it on the graph.

# Example of defining edges and running the algorithm

edges = [(1, 2, 13), (1, 8, 5), ...] # List of edges, where the first two numbers are the numbers of vertices, and the third number is the weight of the edge between them./n
n = 14 # Number of vertices /n
min_tree = kruskal_algorithm(edges, n) # Running the algorithm 

# Dependencies

1. matplotlib - https://matplotlib.org/    (pip install matplotlib)
2. networkx - https://networkx.org/    (pip install networkx)

