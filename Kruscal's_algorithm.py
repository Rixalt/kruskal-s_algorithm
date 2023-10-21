import matplotlib.pyplot as plt
import networkx as nx

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]

    def find(self, k):
        if self.parent[k] != k:
            self.parent[k] = self.find(self.parent[k])
        return self.parent[k]

    def union(self, a, b):
        self.parent[self.find(a)] = self.find(b)

def kruskal_algorithm(edges, n):
    min_tree = []
    ds = DisjointSet(n)

    for src, dest, weight in sorted(edges, key=lambda x: x[2]):
        if len(min_tree) == n - 1:
            break
        if ds.find(src) != ds.find(dest):
            min_tree.append((src, dest, weight))
            ds.union(src, dest)

    return min_tree

if __name__ == '__main__':
    edges = [(1, 2, 13), (1, 8, 5), (2, 8, 1), (9, 8, 78), (8, 11, 24),
             (9, 11, 56), (2, 10, 77), (2, 6, 9), (14, 7, 1), (6, 10, 2),
             (11, 14, 77), (6, 14, 56), (6, 13, 20), (6, 7, 10), (3, 14, 3),
             (3, 7, 7), (7, 13, 9), (13, 14, 13), (3, 4, 4), (4, 7, 1)]

    n = 14

    min_tree = kruskal_algorithm(edges, n)
    print(min_tree)

    G = nx.Graph()
    G.add_weighted_edges_from(min_tree)

    pos = nx.spring_layout(G, k=0.5, iterations=50)
    nx.draw(G, pos, with_labels=True, font_color='black', node_color='green', node_size=300, edge_color='red')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, font_size=10, font_family="Arial", edge_labels=labels)
    plt.show()
