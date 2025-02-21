import matplotlib.pyplot as plt
from collections import defaultdict
import networkx as nx
import numpy as np


nodes = defaultdict(dict)
with open('eg2.txt', 'r') as infile:
    for line in infile.readlines()[1:]:
        line = map(int, line.split())
        src = line[0]
        dst = line[1]
        weight = line[2]
        nodes[src][dst]=weight

G = nx.Graph()

for i in nodes:
    for j in nodes[i]:
        G.add_edge(i, j, weight=nodes[i][j])

rs = nx.floyd_warshall(G)
for i in rs:
    for j in rs[i]:
        print ("%d\t%d\t%d" % (i, j, rs[i][j])

pos = nx.shell_layout(G)
nx.draw(G,pos, node_size=500, node_color='orange', edge_color='blue', width=1)
plt.axis('off')
plt.show()
