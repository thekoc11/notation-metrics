import data
from utils import distances
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import matplotlib as mpl
import pygraphviz as pgv

# Deprecated: GraphViz prove to be more flexible for my purposes.
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
    raise DeprecationWarning("This function is deprecated. Rework necessary if the use of NetworkX is absolutely needed")


### Global Variables, set for tests and reproducibility. DO NOT INVOKE THEM FROM OUTSIDE OF THIS SCRIPT!!
# data.compute_adjusted_melody()
labels = data.GetLabels()[0:6]
# dicts = data.GetAll()[0:6]
# adjusted_melodies = []
# for dic in dicts:
#     adjusted_melodies.append(dic["adjusted_melody"])

# Deprecated
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
    raise DeprecationWarning("This function is deprecated. Rework necessary if the use of NetworkX is absolutely needed")

def draw_weighted_graph(dist_matrix, pivot=400, data_labels=labels, pivot_max=True):
    """
    Returns a GraphViz code for drawing an undirected graph, with edge weights specified.
    :param dist_matrix: Distance matrix used for specifying the edges of the graph
    :param pivot: Pivot edge weight; everything above (or below) the pivot is displayed as a dotted line
    :param data_labels: The node names in the graph
    :param pivot_max: bool -> if true, it means that the specified pivot is the maximum threshold (i. e. everything
                    greater in magnitude than the pivot will be dotted), otherwise, it is considered as the minimum
                    threshold.
    :return: String -> prints a String that can be tested directly on https://dreampuf.github.io/GraphvizOnline/
    """
    G = pgv.AGraph(directed=False, strict=False)
    G.add_nodes_from(data_labels)
    for i in range(len(dist_matrix)):
        for j in range(i, len(dist_matrix)):
            if i != j and dist_matrix[i, j] > 0:
                if pivot_max:
                    style = 'solid' if dist_matrix[i, j] < pivot else 'dotted'
                else:
                    style = 'solid' if dist_matrix[i, j] > pivot else 'dotted'
                G.add_edge(data_labels[i], data_labels[j], weight=dist_matrix[i, j]/1000, label=dist_matrix[i, j], style=style)

    M = G.number_of_edges()

    edge_colors = range(2, M + 2)
    edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
    G.layout('dot')
    print(G.string())


def draw_directed_graph(dist_matrix, pivot=0.66, data_labels=labels, pivot_max=True):
    """
    Returns a GraphViz code for drawing a directed graph, without edge weights.
    :param dist_matrix: Distance matrix used for specifying the edges of the graph
    :param pivot: Pivot edge weight; everything above (or below) the pivot is displayed as a dotted line
    :param data_labels: The node names in the graph
    :param pivot_max: bool -> if true, it means that the specified pivot is the maximum threshold (i. e. everything
                    greater in magnitude than the pivot will be dotted), otherwise, it is considered as the minimum
                    threshold.
    :return: String -> prints a String that can be tested directly on https://dreampuf.github.io/GraphvizOnline/
    """
    G = pgv.AGraph(directed=True, strict=False, rankdir="TD")
    G.add_nodes_from(data_labels)
    for i in range(len(dist_matrix)):
        for ii in range(len(dist_matrix[i])):
            if i!= ii and dist_matrix[i, ii] > 0:
                style = 'solid' if dist_matrix[i, ii] < pivot and pivot_max else 'dotted'
                # this is probably because I was working on the specific compositions listed in data.py.
                ### TODO: Bypass/remove this hack completely
                if (i == 1 and ii == 3) or (i == 2 and ii == 3) or (i == 3 and ii == 1) or (i == 3 and ii == 2):
                    pass
                else:
                    G.add_edge(data_labels[i], data_labels[ii], weight=dist_matrix[i, ii], label=dist_matrix[i, ii], style=style)
                    if style == 'solid':
                        print("{} -> {} : {}".format(labels[i], data_labels[ii], dist_matrix[i, ii]))
    G.layout("dot")
    print(G.string())

def draw_causal_inference(dist_matrix, data_labels=labels, mela="Mayamalavagowla", janya=None, alt_labels=None):
    """
    Returns a GraphViz code for drawing a directed acyclic graph, without edge weights. This graph portrays the
    Causal Inference being sent from the dist_matrix
    :param dist_matrix: Distance matrix used for specifying the edges of the graph
    :param data_labels: The node names in the graph. This parameter represents the main labels (i.e. of the format
                        <song_name(raga_name)>)
    :param mela: Name of the Melakarta raga
    :param janya: Name of the Janya raga
    :param alt_labels: Alternate labels for nodes to be rendered in the final graph. When this param is not 'None',
                       the labels specified here will be displayed. This is sometimes useful, e.g. when we want to
                       represent songs as numbers to make the final DAGs a bit more squared.
    :return: no return value, however, prints GraphViz code for the required DAG, which can be verified at
             https://dreampuf.github.io/GraphvizOnline
    """
    # TODO: Add a try-catch logic here, so that the function returns 'True' if the DAG was successfully built, and prints the error otherwise
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

#
# if __name__ == '__main__':
#     list = ['a', 'b', 'c', 'd', 'e']
#     draw_netwrokx_shit()