# coding=utf-8
from __future__ import division
from operator import itemgetter
import re

import numpy as np
from matplotlib import pyplot as plt

from programs.mc_tools import sample_path, compute_stationary
import exercises_part_3.FiniteMarkovChains.my_functions as m


__author__ = 'stijn'

#region Exercise 1
print '\nExercise 1 - Ergodicity:'
# The term ergodic describes a random process for which the time average
# of one sequence of events is the same as the ensemble average. In other
# words, for a Markov chain, as one increases the steps, there exists a
# positive probability measure at step  n  that is independent of
# probability distribution at initial step 0 (Feller, 1971, p. 271).

# Define alpha and beta
alpha = beta = 0.1

# number of samples
N = 10000

#Transition matrix
P = np.array([[1-alpha, alpha], [beta, 1-beta]])

# gamma = [p,1-p] for stable distribution gamma = gamma*P
# p will equal probability of spending time in state X_t=0
p = beta/(alpha+beta)

fig, ax = plt.subplots()
ax.grid()
ax.hlines(0, 0, N, lw=2, alpha=0.6)
ax.set_ylim(-0.25, 0.25)

for X_0, color in zip((0, 1), ('blue', 'green')):
    # sampling
    X = sample_path(P, init=X_0, sample_size=N)
    # compute average time spent in X_t=0 for each t<=N
    X_bar = (X == 0).cumsum()/(np.arange(1, N+1, dtype=float))
    # == Plot == #
    ax.fill_between(range(N), np.zeros(N), X_bar - p, color=color, alpha=0.1)
    ax.plot(X_bar - p, color=color, label=r'$X_0 = \,x {} $'.format(X_0))
    ax.plot(X_bar - p, 'k-', alpha=0.6)  # Overlay in black--make lines clearer

ax.legend(loc='upper right')
plt.show()
#endregion

#beginregrion
print '/nExercise 2 - Markov page rank'
# read webgraph data; each contains "a -> b;" data
web_graph_data = open('../programs/web_graph_data.txt')
web_graph = np.array([re.findall('\w', line) for line in web_graph_data])
web_graph_data.close()

# retrieve all nodes
nodes = np.unique(web_graph)

# function that convert node names to corresponding index in nodes array
convert_to_idx = np.vectorize(lambda x: np.where(nodes == x))

#Create transition matrix based on graph connections
P = np.zeros((nodes.size, nodes.size))
for conn in web_graph:
    P[tuple(convert_to_idx(conn))] = 1

row_sums = P.sum(axis=1)
P = P / row_sums[:, np.newaxis]

#compute stationary state distribution
stationary = compute_stationary(P)

# ranking nodes from low to high
ranked_nodes = {node: ranking for node, ranking in zip(nodes, stationary)}

print('Rankings\n ***')
for name, rank in sorted(ranked_nodes.iteritems(), key=itemgetter(1), reverse=1):
    print('{0}: {1:.4}'.format(name, rank))
#endregion

#beginregrion
print '/nExercise 3 - AR(1) Markov approximation'
rho = 0.1
sigma_u = 0.2
x, P = m.approx_markov(rho, sigma_u, m=5, n=11)
N = 1000
X = sample_path(P, init=np.round(len(x)/2), sample_size=N)

fig, ax = plt.subplots()
ax.plot(range(N), x[X], 'k-', alpha=0.6)
plt.show()
#endregion