# networkx creates network that helps in visualization
# matplotlib just for viewing purposes. 

import networkx as nx
import matplotlib.pyplot as plt
import random 
import time 


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

# let us have a simple update sysmtem for the opinions 
#Defining a function would be better 

def update_opinion(G, conformity_strenght=0.5):
    new_opinion = {}
    neighbor_opinion = [Good.nodes[neighbor]['opinion'] for neighbor in Good.neighbors(node)]
    if neighbor_opinion:
        majority = round(sum(neighbor_opinion) / len(neighbor_opinion))
        # the agent likes the new opinion now due to bias 
        new_opinion[node] = (
            majority if random.random() < conformity_strenght else current 
        )
    for node, opinion in new_opinion.items():
        Good.nodes[node]['opinion'] = opinion

#####################################################################


import time

for t in range(10):  # 10 rounds of updates
    update_opinion(Good)
    opinion = [Good.nodes[n]['opinion'] for n in Goof.nodes()]
    print(f"Round {t+1}: {sum(opinion)} accept, {len(opinion) - sum(opinion)} reject")
    time.sleep(0.5)
