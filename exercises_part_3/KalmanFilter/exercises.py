# coding=utf-8
from __future__ import division
import numpy as np
import matplotlib.pylab as plt
from scipy.stats import norm
from numpy.random import multivariate_normal
from programs.kalman import Kalman


__author__ = 'stijn'

#region Exercise 1
print '\nExercise 1 - Constant parameter estimation:'
# == Set parameters == #

# for the Kalman filter
A, G, Q, R = 1, 1, 0, 1
x_hat_0, Sigma_0 = 8, 1

# for the observed process y_t = theta + v_t
theta = 10
T = 5

# == Init Kalman filter == #
kf = Kalman(A, G, Q, R)

# == Run process and filter == #
kf.set_state(x_hat_0, Sigma_0)

fig, ax = plt.subplots()
xgrid = np.linspace(theta - 5, theta + 2, 200)
for t in range(T):
    m, v = map(float, (kf.current_x_hat, kf.current_Sigma))
    ax.plot(xgrid, norm.pdf(xgrid, loc=m, scale=np.sqrt(v)), label=r'$t=%d$' % t)
    y = theta + norm.rvs(scale=R)
    kf.update(y)

ax.set_title(r'First %d densities when $\theta = %.1f$' % (T, theta))
ax.legend(loc='upper left')
plt.show()
#endregion

#region Exercise 2
print '\nExercise 2 - Probability :'

# for the observed process y_t = theta + v_t
T = 600
epsilon = 0.1

# == Init Kalman filter == #
kf = Kalman(A, G, Q, R)

# == Run process and filter == #
kf.set_state(x_hat_0, Sigma_0)

fig, ax = plt.subplots()
z = np.zeros(T)
for t in range(T):
    m, v = map(float, (kf.current_x_hat, kf.current_Sigma))
    lower, upper = norm.cdf((theta-epsilon, theta+epsilon), loc=m, scale=np.sqrt(v))
    z[t] = 1-(upper-lower)
    y = theta + norm.rvs(scale=R)
    kf.update(y)


ax.plot(range(T), z)
ax.fill_between(range(T),np.zeros(T), z, color='blue', alpha=0.2)
ax.set_title(r'$z_t=1-p_t(x=%.1f)\Delta{x}$ for $t=0...%d$' % (theta, T))
plt.show()

#endregion

#region Exercise 3
print '\nExercise 3 - Optimal state prediction versus filtering:'
# == Set parameters == #

# for the Kalman filter
A = np.array([[0.5, 0.4], [0.6, 0.3]])
G = np.eye(2)
Q = 0.3*np.eye(2)
R = 0.5*np.eye(2)
x_hat_0 = np.array([8, 8])
Sigma_0 = np.array([[0.9, 0.3], [0.3, 0.9]])

# for the observed process y_t = theta + v_t
T = 50

# == Init Kalman filter == #
kf = Kalman(A, G, Q, R)

# == Run process and filter == #
kf.set_state(x_hat_0, Sigma_0)

x = np.zeros(2)
cond_error = np.zeros(T)
filt_error = np.zeros(T)

for t in range(T):
    y = G.dot(x) + multivariate_normal(mean=[0, 0], cov=R)
    kf.update(y)
    x_hat = kf.current_x_hat
    x_cond = A.dot(x)

    x = x_cond + multivariate_normal(mean=[0, 0], cov=Q)

    filt_error[t] = np.sqrt(np.sum((x_hat-x)**2))
    cond_error[t] = np.sqrt(np.sum((x_cond-x)**2))

fig, ax = plt.subplots()
ax.plot(range(T), filt_error, 'k', lw=2, alpha=0.6, label='kalman filter error')
ax.plot(range(T), cond_error, 'g', lw=2, alpha=0.6, label='conditional expectation error')

ax.legend(loc='upper right')
plt.show()
#endregion