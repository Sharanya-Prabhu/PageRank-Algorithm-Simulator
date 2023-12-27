import pandas as pd

# Read the edge list file into a DataFrame
df = pd.read_csv("web_Google_dataset.txt", sep="\t", comment="#", header=None, names=["source", "destination"])

# Get the list of unique node IDs
node_ids = sorted(list(set(df["source"]).union(set(df["destination"]))))

# Count the number of nodes in the graph
num_nodes = len(node_ids)

# Create an adjacency list and initial PageRank values
adj_list = {}
page_ranks = {}
uniform_score = 1 / num_nodes
for node_id in node_ids:
    adj_list[node_id] = []
    page_ranks[node_id] = uniform_score

# Populate the adjacency list and initial PageRank values
for index, row in df.iterrows():
    source = row["source"]
    destination = row["destination"]
    adj_list[source].append(destination)

# Write the adjacency list and initial PageRank values to a file
with open("web_Google.adj", "w") as f:
    for node_id, neighbors in adj_list.items():
        line = str(node_id) + " " + str(page_ranks[node_id]) + " " + ",".join(str(neighbor) for neighbor in neighbors) + "\n"
        f.write(line)
