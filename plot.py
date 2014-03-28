import networkx as nx
import matplotlib.pyplot as plt
import sys

left_nodes = []
right_nodes = []
mapping = dict()

c = 0
central_pt = 0
f = open( sys.argv[1] )
is_left_node = True

for line in f:
    line = line.rstrip()
    if line == "":
        central_pt = c-1
        is_left_node = False
        continue
    mapping[c] = line[ line.rfind('/') :: ]
    if is_left_node:
        left_nodes.append(c)
    else:
        right_nodes.append(c)
    c += 1

for key in mapping:
    print key,
    print mapping[key]

print central_pt

edges_from = []

for i in range(0, len(left_nodes)-1):
    edges_from.append( (left_nodes[i], left_nodes[i+1]) )
for i in range( len(right_nodes)-1, 0, -1):
    edges_from.append( (right_nodes[i], right_nodes[i-1]) )
edges_from.append( (right_nodes[0], central_pt) )

DG = nx.DiGraph()
DG.add_edges_from( edges_from )
DG = nx.relabel_nodes(DG,mapping)

pos = nx.spring_layout(DG)
nx.draw(DG,pos,node_size=0,alpha=0.4,edge_color='r',font_size=16)
plt.show()
