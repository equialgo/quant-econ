from __future__ import division
__author__ = 'stijn'
import matplotlib.pylab as plt
import numpy as np


class Agent(object):

    def __init__(self, type):
        self.type = type
        self.location = np.random.random(2)

    def is_happy(self, agents):
        mask = (self != agents)
        distances = np.array([np.sqrt(np.sum((self.location-agent.location)**2)) for agent in agents[mask]])
        if np.sum(np.array([agent.type for agent in (agents[mask])[distances.argsort()[0:10]]]) == self.type) >= 5:
            return True
        else:
            return False

    def move(self, agents):
        happy = False
        while not happy:
            self.location = np.random.random(2)
            happy = self.is_happy(agents)


if __name__ == '__main__':
    agents = np.concatenate(([Agent('green') for x in range(10)], [Agent('orange') for x in range(10)]))
    f, a = plt.subplots(1,2)

    a[0].plot(agents[0].location[0], agents[0].location[1], 'x', color=agents[0].type)
    for agent in agents[1:]:
        a[0].plot(agent.location[0], agent.location[1], 'o', color=agent.type)
        dist = np.sqrt(np.sum((agents[0].location-agent.location)**2))
        circle = plt.Circle(agents[0].location, radius=dist, color=agent.type, fill=False)
        a[0].add_artist(circle)
    a[0].set_xlim(0, 1)
    a[0].set_ylim(0, 1)
    a[0].set_aspect('equal')

    print str(agents[0].location)+' '+agents[0].type+'\n'
    print agents[0].is_happy(agents)
    agents[0].move(agents)
    print agents[0].is_happy(agents)

    a[1].plot(agents[0].location[0], agents[0].location[1], 'x', color=agents[0].type)
    for agent in agents[1:]:
        a[1].plot(agent.location[0], agent.location[1], 'o', color=agent.type)
        dist = np.sqrt(np.sum((agents[0].location-agent.location)**2))
        circle = plt.Circle(agents[0].location, radius=dist, color=agent.type, fill=False)
        a[1].add_artist(circle)
    a[1].set_xlim(0, 1)
    a[1].set_ylim(0, 1)
    a[1].set_aspect('equal')
    plt.show()






