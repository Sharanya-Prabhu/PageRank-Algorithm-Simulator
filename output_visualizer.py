import networkx as nx
import matplotlib.pyplot as plt

# read in the output file
with open('output_reformatted.txt', 'r') as f:
    lines = f.readlines()

# create a NetworkX graph
G = nx.DiGraph()
for line in lines:

    try:
        node, pr, outlinks = line.strip().split(' ')
    except:
        node, pr= line.strip().split(' ')
        outlinks = None

    G.add_node(node, pr=float(pr))

    if outlinks is not None:
        outlinks = outlinks.split(',')
        for outlink in outlinks:
            G.add_edge(node, outlink)

# get the PageRank values and node labels
pr_values = nx.get_node_attributes(G, 'pr')
node_labels = {node: f"{node}\nPageRank: {pr:.3f}" for node, pr in pr_values.items()}

# scale the node sizes based on the PageRank values
node_sizes = [3000 * pr for pr in pr_values.values()]

# set the node label positions outside of the nodes
pos = nx.spring_layout(G, k=0.15)
pos_labels = {}
for node, coords in pos.items():
    pos_labels[node] = (coords[0], coords[1] + 0.07)

# draw the graph with adjusted node sizes, label positions, and arrow directions
nx.draw_networkx_nodes(G, pos, node_size=node_sizes)
nx.draw_networkx_edges(G, pos, arrows=True, width=1.5, alpha=0.8, arrowstyle='->,head_width=0.5,head_length=0.8')
nx.draw_networkx_labels(G, pos_labels, labels=node_labels, font_size=10)

plt.axis('off')
plt.show()


