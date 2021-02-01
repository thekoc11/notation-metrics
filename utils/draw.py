import pygraphviz as pgv

def draw_graph_symmetric(labels, weights, name=None):
    if weights.shape != (len(labels), len(labels)):
        raise AssertionError("Weights should be a matrix ox dimensions n x n where n = len(labels)")

    G = pgv.AGraph(strict=False, directed=False)
    G.add_nodes_from(labels)
    for i in range(len(labels)):
        for ii in range(len(labels)):
            if weights[i, ii] > 0:
                G.add_edge(labels[i], labels[ii], label=weights[i, ii])

    if name != None:
        G.graph_attr["label"] = name

    print("Saving graph as a PNG file ...")
    if name == None:
        n = "file"
    else:
        n = name
    G.draw("{}.png".format(n), prog="dot")
    print("file {}.png saved!".format(n))


