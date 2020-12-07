# Want to modify part 1 such that the graph tracks distance to node (edge weight) in vertex

# Then in is reachable, i want to check the reachability

import re
import networkx as nx


def extract_vertices(rule, bag_graph):
    # Extract base color
    base = rule[:rule.index('bags')-1]

    # Extract all possible bags that the base contains
    contents = rule[rule.index('contain')+len('contain')+1:-1]

    # Lazy handling of this. Create a vertex pair u,v with weighted edge where:
    # u is the base
    # vi exists for each bag i that the base contains
    # and the weight between u, vi is the frequency of bag i
    if contents != 'no other bags' and contents != 'no other bags.':
        for content in contents.split(','):
            # Determine bag type and frequency
            c = content.strip().split(' ')
            frequency, bag_type = int(c[0]), ' '.join(c[1:-1])

            # Create a weighted graph were the edge weight is determined by the bag frequency
            bag_graph.add_edge(base, bag_type, weight=frequency)

    return bag_graph

with open("Input.txt") as file:
    # Way to lazy to create my own directed weighted graph
    bags = nx.DiGraph()

    # create the graph
    for line in file:
        bags = extract_vertices(line, bags)

    # Recursively accumulate edge weights
    def acc_edge_weights(base, bag_graph):
        total = 0
        # Graph the key (base vertex) and all values (connected vertices with weights)
        for key, val in zip(bag_graph[base].keys(), bag_graph[base].values()):
            # The equation for the weight of the path to bag i is:
                # accumulated_weight = a, the weight accumulated by traversing from shiny gold
                # val = b, the current value of the bag
                # a*b + b == b(a+1)
            total +=  (acc_edge_weights(key, bag_graph) + 1) * val['weight']

        return total
    
    print(acc_edge_weights('shiny gold', bags))