# coding=utf-8
from __future__ import division
import numpy as np
import matplotlib.pylab as plt
from scipy.stats import norm, uniform, chi2
from scipy.linalg import sqrtm, inv


__author__ = 'stijn'

#region Exercise 1
print '\nExercise 1 - Central Limit Theorem; asymptotic distribution estimator:'

# == Set parameters == #
n = 250     # Choice of n
replications = 100000  # Number of draws of Y_n
distribution = uniform(loc=0, scale=0.5*np.pi)  # Uniform distribution [0,1/2*pi]
mu, s = distribution.mean(), distribution.std()
g = np.sin  # Function g
g_d = np.cos  # Derivative of function g

# == Draw underlying RVs. Each row contains a draw of X_1,..,X_n == #
data = distribution.rvs((replications, n))
# == Compute mean of each row, producing k draws of \bar X_n == #
sample_means = data.mean(axis=1)
# == Generate observations of Y_n == #
Y = np.sqrt(n) * (g(sample_means) - g(mu))

# == Plotting approximation and N(0,g'(mu)^2*sigma^2) == #
fig, ax = plt.subplots()
x_min, x_max = -3 * s, 3 * s
ax.set_xlim(x_min, x_max)
ax.hist(Y, bins=60, alpha=0.5, normed=True)
x_grid = np.linspace(x_min, x_max, 200)
ax.plot(x_grid, norm.pdf(x_grid, scale=g_d(mu)*s), 'k-', lw=2, label=r'$N(0, g\'(\mu)^2\sigma^2)$')
ax.legend()
fig.suptitle(r'$\sqrt{n}(g(\bar{X}_n)-g(\mu))\sim N(0, g\'(\mu)^2\sigma^2)$ for n = '+str(n), fontsize=16)

plt.show()
#endregion

#region Exercise 2
print '\nExercise 2 - Central Limit Theorem; approximate chi squared distribution:'

# == Set parameters == #
n = 250
replications = 100000

dist_w = uniform(loc=-1, scale=2)  # Uniform distribution [-1,1]
mu_w, s_w = dist_w.mean(), dist_w.std()

dist_u = uniform(loc=-2, scale=4)  # Uniform distribution [-2,2]
mu_u, s_u = dist_u.mean(), dist_u.std()

# == Compute variance matrix == #
S = np.array([[s_w**2, s_w**2], [s_w**2, s_u**2+s_w**2]])  # based on X_i = (w_i, w_i + u_i)
mu = np.array([mu_w, mu_u+mu_w])
Q = inv(sqrtm(S))

# == Draw underlying RVs == #
data = dist_w.rvs((2, replications, n))
data[1, :, :] = dist_u.rvs((1, replications, n))
# == Compute mean of each row, producing k draws of \bar X_n == #
sample_means = data.mean(axis=2)

Y = n*np.sum((np.dot(Q, sample_means - mu[:, np.newaxis]))**2, axis=0)

# == Plotting approximation and chi^2(2) distribution == #
fig, ax = plt.subplots()
x_min, x_max = 0, 8
ax.set_xlim(x_min, x_max)
ax.hist(Y, bins=60, alpha=0.5, normed=True)
x_grid = np.linspace(x_min, x_max, 200)
ax.plot(x_grid, chi2.pdf(x_grid, 2), 'k-', lw=2, label=r'$\chi^2(k=2)$')
ax.legend()
fig.suptitle(r'$n ||Q(\bar{X}_n-\mu)||^2\sim \chi^2(k)$ for n = '+str(n), fontsize=16)

plt.show()
#endregion
