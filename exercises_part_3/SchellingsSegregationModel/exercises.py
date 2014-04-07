# coding=utf-8
from __future__ import division
import numpy as np
import exercises_part_3.SchellingsSegregationModel.my_classes as mc
import exercises_part_3.SchellingsSegregationModel.my_functions as mf
import matplotlib.pylab as plt


__author__ = 'stijn'

#region Exercise 1
print '\nExercise 1 - Schelling\'s Segregation Model:'

agents = np.concatenate(([mc.Agent('green') for x in range(250)],
                         [mc.Agent('orange') for x in range(250)]))

num_of_moves = 1
iteration = 0

while num_of_moves > 0:
    num_of_moves = 0
    for agent in agents:
        if not agent.is_happy(agents):
            agent.move(agents)
            num_of_moves += 1

    print 'iteration {0} -> {1} agents moved'.format(iteration, num_of_moves)
    iteration += 1

f, ax = plt.subplots(1)
mf.plot_agents(ax, agents)
plt.show()
#endregion