# coding=utf-8
from __future__ import division
import re
import numpy as np
import collections
__author__ = 'stijn'


#beginregrion
print '\nExercise 1 - Shortest Path'
# read webgraph data; each contains "a -> b;" data
graph_data = open('../../programs/graph.txt')
graph = collections.OrderedDict()
for line in graph_data:
    graph[re.findall('(node\d+),',  line)[0]] = {'to': re.findall('(node\d+)\s',  line),
                                                 'w': re.findall('(\d+\.\d+)',  line)}

nodes = np.array(graph.keys())
graph_data.close()

# function that convert node names to corresponding index in nodes array
to_idx = np.vectorize(lambda x: np.where(nodes == x))
start_state = to_idx('node0')[0]
stop_state = to_idx('node99')[0]

# Create cost matrix based on graph connections
# Non-transitions will have huge cost of Inf
# Begin and start states can transition on themselves with no cost!
c = np.ones((nodes.size, nodes.size))*np.Inf
# Set begin and start states to zero cost
c[start_state, start_state] = 0
c[stop_state, stop_state] = 0
for node in nodes:
    for to_node, weight in zip(graph[node]['to'], graph[node]['w']):
        c[tuple((to_idx(node), to_idx(to_node)))] = float(weight)

#Bellmann iteration
J_old = np.ones(len(nodes))*np.Inf
J_new = J_old.copy()
J_new[stop_state] = 0
while not(np.array_equal(J_old, J_new)):
    J_old = J_new.copy()
    J_new = np.min(J_old[np.newaxis][:]+c, axis=1)

J = J_new

#Path with minimum cost
path = [start_state]
path_cost = 0
c[start_state, start_state] = np.Inf  #set cost for staying in state 0 to Inf
while path[-1] != stop_state:
    path.append((J+c[path[-1]]).argmin())
    path_cost += c[path[-2]][path[-1]]

path_nodes = [nodes[node_idx] for node_idx in path]
print 'Path with the minimum cost of {0} or (J(0)={1}) is:'.format(path_cost, J[start_state])
for path_node in path_nodes:
    print '\t'+path_node
#endregion

