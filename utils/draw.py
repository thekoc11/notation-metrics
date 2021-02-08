import data
from utils import distances
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import matplotlib as mpl
import pygraphviz as pgv

# seed = 13648  # Seed random number generators for reproducibility
# G = nx.random_k_out_graph(10, 3, 0.5, seed=seed)
# pos = nx.spring_layout(G, seed=seed)
#
# node_sizes = [3 + 10 * i for i in range(len(G))]
# M = G.number_of_edges()
# edge_colors = range(2, M + 2)
# edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
# cmap = plt.cm.plasma
#
# nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color="indigo")
# edges = nx.draw_networkx_edges(
#     G,
#     pos,
#     node_size=node_sizes,
#     arrowstyle="->",
#     arrowsize=10,
#     edge_color=edge_colors,
#     edge_cmap=cmap,
#     width=2,
# )
# # set alpha value for each edge
# for i in range(M):
#     edges[i].set_alpha(edge_alphas[i])
#
# pc = mpl.collections.PatchCollection(edges, cmap=cmap)
# pc.set_array(edge_colors)
# plt.colorbar(pc)
#
# ax = plt.gca()
# ax.set_axis_off()
# plt.show()


data.compute_adjusted_melody()
labels = data.GetLabels()[0:6]
dicts = data.GetAll()[0:6]
adjusted_melodies = []
for dic in dicts:
    adjusted_melodies.append(dic["adjusted_melody"])


def draw_weighted_graph(dist_matrix, pivot=400):
    G = pgv.AGraph(directed=False, strict=False)
    G.add_nodes_from(labels)
    for i in range(len(dist_matrix)):
        for j in range(i, len(dist_matrix)):
            if i != j and dist_matrix[i, j] > 0:
                style = 'solid' if dist_matrix[i, j] < pivot else 'dotted'
                if (i == 1 and j == 3) or (i == 2 and j == 3) or (i == 3 and j == 1) or (i == 3 and j == 2):
                    pass
                else:
                    G.add_edge(labels[i], labels[j], weight=dist_matrix[i, j]/1000, label=dist_matrix[i, j], style=style)

    M = G.number_of_edges()

    edge_colors = range(2, M + 2)
    edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
    G.layout('dot')
    print(G.string())
def draw_directed_graph(dist_matrix, pivot = 0.66):
    G = pgv.AGraph(directed=True, strict=False, rankdir="TD")
    G.add_nodes_from(labels)
    for i in range(len(dist_matrix)):
        for ii in range(len(dist_matrix[i])):
            if i!= ii and dist_matrix[i, ii] > 0:
                style = 'solid' if dist_matrix[i, ii] < pivot else 'dotted'
                if (i == 1 and ii == 3) or (i == 2 and ii == 3) or (i == 3 and ii == 1) or (i == 3 and ii == 2):
                    pass
                else:
                    G.add_edge(labels[i], labels[ii], weight=dist_matrix[i, ii], label=dist_matrix[i, ii], style=style)
                    if style == 'solid':
                        print("{} -> {} : {}".format(labels[i], labels[ii], dist_matrix[i, ii]))
    G.layout("dot")
    print(G.string())

def draw_causal_inference(dist_matrix):
    G = pgv.AGraph(directed=True, strict=False, rankdir="TD")
    G.add_nodes_from(labels)
    for i in range(len(dist_matrix)):
        for ii in range(len(dist_matrix[i])):
            if i!= ii and dist_matrix[i, ii] > 0:
                style = 'solid'
                if (i == 1 and ii == 3) or (i == 2 and ii == 3) or (i == 3 and ii == 1) or (i == 3 and ii == 2):
                    pass
                else:
                    G.add_edge(labels[i], labels[ii], weight=dist_matrix[i, ii])
    G.layout("dot")
    print(G.string())
