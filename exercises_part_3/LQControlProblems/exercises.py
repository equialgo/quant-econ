# coding=utf-8
from __future__ import division
import numpy as np
import matplotlib.pylab as plt
from programs.lqcontrol import LQ


__author__ = 'stijn'

PLOT_EXERCISE_1 = 1
PLOT_EXERCISE_2 = 1
PLOT_EXERCISE_3 = 1

#region Exercise 1
print '\nExercise 1 - Polynomial income:'

# LQ problem
# a_{t+1} = (1+r)*a_t - u_t - c_bar + m1*t + m2*t^2 + s*w_{t+1}
# u_t = (c_t-c_bar)
# C = \sum_{t=0}^T beta(c_t-c_bar)^2 + beta^T*q*a_T^2
# where last term of cost function denotes punishment for
# having capital at t=T (iow when dying!)
# the state vector becomes x_t = [a_t, 1, t, t**2]

# == model parameters == #
r = 0.05
beta = 1/(1 + r)
c_bar = 1.5
mu = 2
s = 0.15
T = 50
q = 1e4
m1 = T*mu/(T/2)**2
m2 = -mu/(T/2)**2

A = [[1+r, -c_bar, m1, m2],
     [0, 1, 0, 0],
     [0, 1, 1, 0],  # next time step t -> t+1
     [0, 1, 2, 1]]  # next time step t^2 -> t^2 + 2t + 1
B = [[-1],
     [0],
     [0],
     [0]]
C = [[s],
     [0],
     [0],
     [0]]
Q = 1
R = np.zeros((4, 4))
Rf = np.zeros((4, 4))
Rf[0, 0] = q
# == init LQ model == #
lq = LQ(Q, R, A, B, C=C, beta=beta, T=T, Rf=Rf)
x_0 = [0, 1, 0, 0]  # a_0 = 0 and t = 0
x, u, w = lq.compute_sequence(x_0)

# == retrieve results ==#
time = x[2, 1:]
consumption = u[0]+c_bar
income = m1*time+m2*time**2+w[0, 1:]
assets = x[0, :]

# == plotting == #
if PLOT_EXERCISE_1:
    plot_args ={'lw': 2, 'alpha': 0.8}
    bbox = [0., 1.02, 1., .102]
    legend_args = {'bbox_to_anchor': bbox, 'loc': 3, 'mode' : 'expand'}
    fig, axes = plt.subplots(2, 1)
    plt.subplots_adjust(hspace=0.5)

    axes[0].plot(time, consumption, color='blue', label='consumption', **plot_args)
    axes[0].plot(time, income, color='green', label='income', **plot_args)

    axes[1].plot(x[2, :], assets, color='red', label='assets', **plot_args)
    axes[1].axhline(y=0, xmin=0, xmax=T, color='black')

    map(lambda ax: ax.grid(), axes)
    map(lambda ax: ax.set_xlabel('time'), axes)
    map(lambda ax: ax.legend(ncol=2, **legend_args), axes)

    plt.show()
#endregion

#region Exercise 2
print '\nExercise 2 - Polynomial income with retirement:'

# LQ problem
# a_{t+1} = (1+r)*a_t - u_t - c_bar + m1*t + m2*t^2 + sigma*w_{t+1} for t<=K
# a_{t+1} = (1+r)*a_t - u_t - c_bar + s for t>K
# u_t = (c_t-c_bar)
# C = \sum_{t=0}^T beta(c_t-c_bar)^2 + beta^T*q*a_T^2
# where last term of cost function denotes punishment for
# having capital at t=T (iow when dying!)
# the state vector becomes x_t = [a_t, 1, t, t**2]

# == model parameters == #
r = 0.05
beta = 1/(1 + r)
c_bar = 4
mu = 2
sigma = 0.35
K = 40
T = 60
s = 1
q = 1e4
m1 = T*mu/(K/2)**2
m2 = -mu/(K/2)**2

# == setup retirement lq part == #
A = [[1+r, s-c_bar, 0, 0],
     [0, 1, 0, 0],
     [0, 1, 1, 0],  # next time step t -> t+1
     [0, 1, 2, 1]]  # next time step t^2 -> t^2 + 2t + 1
B = [[-1],
     [0],
     [0],
     [0]]
C = [[0],
     [0],
     [0],
     [0]]
Q = 1
R = np.zeros((4, 4))
Rf = np.zeros((4, 4))
Rf[0, 0] = q
# == init LQ model == #
lq_retired = LQ(Q, R, A, B, C=C, beta=beta, T=T-K, Rf=Rf)

for t in range(T-K):
    lq_retired.update_values()  # determine P(t=K) = P_K through back-propagation

# == setup work lq process == #
# cost to go is given by V_K = x'* P_K*x + d_K
# because d_t is a constant it can be discarded
# for the work LQ optimization
# therefore P_K is the Rf for the new optimization
Rf = lq_retired.P
A = [[1+r, -c_bar, m1, m2],
     [0, 1, 0, 0],
     [0, 1, 1, 0],  # next time step t -> t+1
     [0, 1, 2, 1]]  # next time step t^2 -> t^2 + 2t + 1
C = [[sigma],
     [0],
     [0],
     [0]]
lq_work = LQ(Q, R, A, B, C=C, beta=beta, T=K, Rf=Rf)

# == forward simulate process ==#
x_0 = [0, 1, 0, 0]  # a_0 = 0 and t = 0
x_work, u_work, w_work = lq_work.compute_sequence(x_0)

x_retired, u_retired, w_retired = lq_retired.compute_sequence(x_work[:, -1])

time = np.arange(1, K+1)
consumption = np.concatenate((u_work[0]+c_bar, u_retired[0]+c_bar))
income = np.concatenate((w_work[0, 1:K+1]+m1*time+m2*time**2, np.ones(T-K)*s))
assets = np.concatenate((x_work[0, :], x_retired[0, 1:]))

# == plotting == #
if PLOT_EXERCISE_2:
    plot_args ={'lw': 2, 'alpha': 0.8}
    bbox = [0., 1.02, 1., .102]
    legend_args = {'bbox_to_anchor': bbox, 'loc': 3, 'mode' : 'expand'}
    fig, axes = plt.subplots(2, 1)
    plt.subplots_adjust(hspace=0.5)

    axes[0].plot(np.arange(1, T+1), consumption, color='blue', label='consumption', **plot_args)
    axes[0].plot(np.arange(1, T+1), income, color='green', label='income', **plot_args)

    axes[1].plot(np.arange(0, T+1), assets, color='red', label='assets', **plot_args)
    axes[1].axhline(y=0, xmin=0, xmax=T, color='black')

    map(lambda ax: ax.grid(), axes)
    map(lambda ax: ax.set_xlabel('time'), axes)
    map(lambda ax: ax.legend(ncol=2, **legend_args), axes)

    plt.show()
#endregion

#region Exercise 3
print '\nExercise 3 - Monopolist application with adjustment cost:'

# were are solving:
# qbar_{t+1}= rho*qbar_t + (1-rho)*(a0-c)/(2*a1) + sigma/(2*a1)*w_{t+1}
# q_{t+1} = q_t + u_t
# under minimization of cost:
# C = E \sum beta^t*[ a1*(q_t-qbar_t)^2 + gamma*u_t^2]
# the state vector becomes x_t = [qbar_t, q_t, 1]

# == model parameters == #
a0 = 5
a1 = 0.5
sigma = 0.15
gamma = 10
rho = 0.9
beta = 0.95
c = 2

# == usefull constants == #
# == Useful constants == #
m0 = (a0 - c) / (2 * a1)
m1 = 1 / (2 * a1)

# == setup retirement lq part == #
A = [[rho, 0, (1-rho)*m0],
     [0, 1, 0],  # next time step q_t+1 -> q_t + u_t
     [0, 0, 1]]
B = [[0],
     [1],
     [0]]
C = [[sigma*m1],
     [0],
     [0]]
Q = gamma

# xRx = qbar^2+q^2-2q*qbar
R = [[a1, -a1, 0],
     [-a1, a1, 0],
     [0, 0, 0]]

# == init LQ model == #
lq = LQ(Q, R, A, B, C=C, beta=beta)

x0 = (m0, 2, 1)
xp, up, wp = lq.compute_sequence(x0, ts_length=150)

q_bar = xp[0, :]
q = xp[1, :]

# == plotting == #
if PLOT_EXERCISE_3:
    plot_args ={'lw': 2, 'alpha': 0.8}
    bbox = [0., 1.02, 1., .102]
    legend_args = {'bbox_to_anchor': bbox, 'loc': 3, 'mode' : 'expand'}
    fig, ax = plt.subplots()
    plt.subplots_adjust(hspace=0.5)

    time = range(len(q))
    ax.set_xlim(0, max(time))
    ax.plot(time, q_bar, color='black', label=r'$\bar{q}_t$', **plot_args)
    ax.plot(time, q, color='blue', label=r'$q_t$', **plot_args)

    ax.grid()
    ax.set_xlabel('time')
    ax.legend(ncol=2, **legend_args)
    s = r'dynamics with $\gamma = {}$'.format(gamma)
    ax.text(max(time) * 0.6, 1 * q_bar.max(), s, fontsize=14)

    plt.show()
#endregion