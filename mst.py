import matplotlib.pyplot as plt
import networkx as nx
from disjointsets import DisjointSets  

#input
V,E = map(int, input().split())
edge_list = []
for i in range(E):
    edge_list.append(tuple(map(int, input().split())))

s = DisjointSets(V)

def kruskal():
    edge_list.sort(key=lambda x: x[2])
    mst_edges = []
    total_cost = 0
    for edge in edge_list:
        u, v, w = edge
        if s.findset(u) != s.findset(v):
            s.union(u,v)
            total_cost += w
            mst_edges.append((u,v,w))

    return total_cost, mst_edges

total, mst_edges = kruskal()

G = nx.Graph()
for u, v, w in edge_list:
    G.add_edge(u, v, weight=w)

pos = nx.kamada_kawai_layout(G)

MST_G = G.copy()
edges_to_remove = set(edge_list) - set(mst_edges)
MST_G.remove_edges_from(edges_to_remove)

def draw_graph(edge_list, G):
    plt.figure(figsize=(10,6))
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, width=1.5, edge_color="gray")
    edge_labels = {(u, v): weight for u, v, weight in edge_list}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')
    plt.title("Graph Visualization with Weights")
    plt.axis('off')
    plt.show()

draw_graph(edge_list=edge_list, G=G)
draw_graph(edge_list=mst_edges,G=MST_G)