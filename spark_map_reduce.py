import sys
from operator import add
from pyspark import SparkConf, SparkContext

# Set up Spark
conf = SparkConf().setMaster("local").setAppName("PageRank").set("spark.executor.memory", "1g")
sc = SparkContext(conf=conf)

# Read in the input file
input_file = "s3://pagerankbucket/spark-emr/web_Google_dataset.txt"
lines = sc.textFile(input_file)

# Split the input lines into node ID, PageRank, and outlinks
def parse_input_line(line):
    fields = line.split(" ")
    node_id = int(fields[0])
    page_rank = float(fields[1])
    outlinks = []
    if len(fields) > 2:
        outlinks = [int(x) for x in fields[2].split(",")]
    return (node_id, page_rank, outlinks)

# Mapper function to emit (node ID, PageRank, outlinks) tuples for each outlink
def emit_outlink(outlink, page_rank, outlinks):
    return (outlink, page_rank / len(outlinks), outlinks)

# Mapper function to emit (node ID, PageRank, outlinks) tuples for each node
def emit_node(node):
    node_id, page_rank, outlinks = node
    yield (node_id, page_rank, outlinks)
    for outlink in outlinks:
        yield emit_outlink(outlink, page_rank, outlinks)

# Reducer function to aggregate the PageRank scores and outlinks for each node
def aggregate_node(node1, node2):
    node_id = node1[0]
    page_rank = node1[1] + node2[1]
    outlinks = node1[2]
    if node2[2]:
        outlinks = node2[2]
    return (node_id, page_rank, outlinks)

# Iterate through the PageRank iterations
num_iterations = 3
for i in range(num_iterations):
    # Parse the input lines into (node ID, PageRank, outlinks) tuples
    nodes = lines.map(parse_input_line)

    # Emit (node ID, PageRank, outlinks) tuples for each node and outlink
    nodes = nodes.flatMap(emit_node)

    # Aggregate the PageRank scores and outlinks for each node
    nodes = nodes.reduceByKey(aggregate_node)

    # Calculate the new PageRank scores for each node
    damping_factor = 0.85
    new_nodes = nodes.flatMap(lambda node: ([(node[0], damping_factor * (node[1] / len(node[2])) + (1 - damping_factor)), (outlink, 0)] for outlink in node[2]))

    # Sum up the new PageRank scores for each node
    nodes = new_nodes.reduceByKey(lambda x, y: x + y)

# Get the top 10 nodes ranked by PageRank score
top_nodes = nodes.takeOrdered(3, key=lambda node: -node[1])

# Output the results with node ID, PageRank score, and outlinks
for node in top_nodes:
    outlinks = ",".join(str(outlink) for outlink in node[0][2])
    print("{}\t{}\t{}".format(node[0][0], node[1], outlinks))
