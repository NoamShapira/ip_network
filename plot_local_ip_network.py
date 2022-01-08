import matplotlib.pyplot as plt
import networkx as nx
import pyshark

cap = pyshark.LiveCapture(interface="Wi-Fi")
packet_count = 500

print("capturing packets")
cap.sniff(packet_count=packet_count)
print("Done capturing packets")



# G = nx.Graph()
# connections = set()
# nodes = set()
# protocols = set()
#
# for p in cap:
#     try:
#         protocols.add(p.transport_layer)
#     except AttributeError as e:
#         pass
#     try:
#         nodes.add(p.ip.src)
#         nodes.add(p.ip.dst)
#         connections.add((p.ip.src, p.ip.dst))
#     except AttributeError as e:
#         pass
#
# print(protocols)
#
# G.add_nodes_from(nodes)
# G.add_edges_from(connections)
#
# plt.rcParams['figure.figsize'] = 150, 120
# pos = nx.spring_layout(G, scale=1.0, iterations=100)
# nx.draw(G, pos, node_color='c', edge_color='k', with_labels=True)
