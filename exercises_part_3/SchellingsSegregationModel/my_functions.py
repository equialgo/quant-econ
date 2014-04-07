from __future__ import division
# coding=utf-8
__author__ = 'stijn'


def plot_agents(ax, agents):
    for agent in agents:
        ax.plot(agent.location[0], agent.location[1], 'o', color=agent.type)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')