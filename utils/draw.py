import data
from utils import distances
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import matplotlib as mpl
import pygraphviz as pgv

def draw_netwrokx_shit():
    seed = 32767 # Seed random number generators for reproducibility
    G = nx.random_k_out_graph(10, 3, 0.5, seed=seed)
    pos = nx.spring_layout(G, seed=seed)

    node_sizes = [400 for i in range(len(G))]
    M = G.number_of_edges()
    edge_colors = range(2, M + 2)
    edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
    cmap = plt.cm.plasma

    nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color="white")
    edges = nx.draw_networkx_edges(
        G,
        pos,
        node_size=node_sizes,
        arrowstyle="->",
        arrowsize=10,
        edge_color=edge_colors,
        edge_cmap=cmap,
        width=2
    )
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    # set alpha value for each edge
    # for i in range(M):
    #     edges[i].set_alpha(edge_alphas[i])

    pc = mpl.collections.PatchCollection(edges, cmap=cmap)
    pc.set_array(edge_colors)
    plt.colorbar(pc)

    ax = plt.gca()
    ax.set_axis_off()
    plt.show()


# data.compute_adjusted_melody()
labels = data.GetLabels()[0:6]
# dicts = data.GetAll()[0:6]
# adjusted_melodies = []
# for dic in dicts:
#     adjusted_melodies.append(dic["adjusted_melody"])

def draw_causal_inference_networkx(dist_matrix, data_labels=labels, seed=13448):
    G = nx.DiGraph()
    num_labels = [i for i in range(len(data_labels))]
    G.add_nodes_from(num_labels, font_size=24)
    for i in range(len(dist_matrix)):
        for ii in range(len(dist_matrix[i])):
            if i!= ii and dist_matrix[i, ii] > 0:
                G.add_edge(num_labels[i], num_labels[ii], weight=dist_matrix[i, ii])

    pos = nx.spring_layout(G, seed=seed)

    nx.draw_networkx_nodes(G, pos, node_size=400, node_color='white')
    nx.draw_networkx_edges(
        G,
        pos,
        node_size=400,
        arrowstyle='->',
        arrowsize=10,
        width=2
    )
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

    ax = plt.gca()
    ax.collections[0].set_edgecolor('#000fff')
    ax.set_axis_off()
    plt.show()


def draw_weighted_graph(dist_matrix, pivot=400, data_labels=labels):
    G = pgv.AGraph(directed=False, strict=False)
    G.add_nodes_from(data_labels)
    for i in range(len(dist_matrix)):
        for j in range(i, len(dist_matrix)):
            if i != j and dist_matrix[i, j] > 0:
                style = 'solid' if dist_matrix[i, j] < pivot else 'dotted'
                G.add_edge(data_labels[i], data_labels[j], weight=dist_matrix[i, j]/1000, label=dist_matrix[i, j], style=style)

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

def draw_causal_inference(dist_matrix, data_labels=labels, mela="Mayamalavagowla", janya=None, alt_labels=None):
    G = pgv.AGraph(directed=True, strict=False, rankdir="TD")
    graph_labels = []
    if janya is not None:
        for l in data_labels:
            if mela in l:
                graph_labels.append(l.replace("({})".format(mela), ""))
            if janya in l:
                graph_labels.append(l.replace("({})".format(janya), ""))
    curr_labels = []

    if alt_labels is not None:
        G.add_nodes_from(alt_labels, fontsize=42)
        curr_labels = alt_labels
    elif janya is not None:
        G.add_nodes_from(graph_labels, fontsize=42)
        curr_labels = graph_labels
    else:
        G.add_nodes_from(data_labels, fontsize=42)
        curr_labels = data_labels

    for i in range(len(data_labels)):
        if mela in  data_labels[i] or "Mayamalavgowla" in data_labels[i]:
            G.get_node(curr_labels[i]).attr["color"] = "black"
            G.get_node(curr_labels[i]).attr["fontcolor"] = "white"
            G.get_node(curr_labels[i]).attr["style"] = "filled"

    for i in range(len(dist_matrix)):
        for ii in range(len(dist_matrix[i])):
            cond = (mela in data_labels[i] and mela not in data_labels[ii]) or (mela in data_labels[ii] and mela not in data_labels[i])
            if cond and (i!= ii and dist_matrix[i, ii] > 0):
                G.add_edge(curr_labels[i], curr_labels[ii], weight=dist_matrix[i, ii])
    G.layout("dot")
    print(G.string())


if __name__ == '__main__':
    list = ['a', 'b', 'c', 'd', 'e']
    draw_netwrokx_shit()