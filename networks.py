# networkx creates network that helps in visualization
# matplotlib just for viewing purposes. 

import networkx as nx
import matplotlib.pyplot as plt
import random 


# These are the parameters that control how the network forms (refer to documentation)

n = 30     # shows the number of agents in the network 
k = 4      # Each node, how many neighbours does it connect to 
p = 0.2    # the randomness and rewiring that occurs in the network


# generating a network (in out case it is a small world network - watts-strogatz style)

Good = nx.watts_strogatz_graph(n, k, p)


# trying to visualize the network

nx.draw(Good, with_labels=True, node_color= 'blue', node_size = 420)
plt.title("Your watts-strogatz small world network")

plt.show()


# We shall have two opinions 
# 1 for closeminded and likes windows 
# 0 for openminded and likes linux 

for node in Good.nodes():
    Good.nodes[node]['Opinion'] = random.choice([0,1])

