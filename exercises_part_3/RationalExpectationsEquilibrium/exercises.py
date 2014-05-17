from programs.lqcontrol import LQ
#region Exercise 1
print '\nExercise 1 - Firm\'s problem'

# price demand curve p_t = a_0 - a_1 * Y_t
# where p_t is price and Y_t market wide output with Y_t = n*y_t
#
# the firm needs to minimize production cost sum_0^\infty beta^t * r_t
# where r_t = - p_t*y_t + gamma(y_{t+1}-y_t)^2/2
#           = - a_0*y_t + a_1*Y_t*y_t + gamma(u_t)^2/2
# with u_t = y_{t+t}-y_t
# iow. maximize income versus minimize adjustment costs
#
# firm's believe is H(Y_t) is Y_{t+1} = k_0 + k_1 * Y_t
#
# to write it in the form of LQ problem
# x_{t+1} = A*x_t + B*u_t
# r_t = x_t*R*x_t + u_t*Q*U_t (see above for definition of cost function for firm)
#
# if we set x_t = [y_t Y_t 1] the we need to capture
# transition due to control y_{t+1} = y_t + u_t (= y_t + y_{t+1} - y_t)
# and the firms believe Y_{t+1} = k_0 + k_1 * Y_t

# == paramters == #
a_0 = 100
a_1 = 0.05

beta = 0.95
gamma = 10

k_0 = 95.5
k_1 = 0.95

# == LQ parameters == #
A = [[1, 0, 0],
     [0, k_1, k_0],
     [0, 0, 1]]
B = [[1],
     [0],
     [0]]
R = [[0, 0.5*a_1, -0.5*a_0],  #needs to be a symmetric matrix!
     [0.5*a_1, 0, 0],
     [-0.5*a_0, 0, 0]]
Q = 0.5*gamma

lq = LQ(Q, R, A, B, beta=beta)
P, F, d = lq.stationary_values()
# F is optimal policy
# u_t = -F_t*x_t
# y_{t+1}-y_t = -f_0*y_t - f_1*Y_t - f_2
# however we are looking for the format:
# y_{t+1} = h_0 + h_1*y_t + h_2*Y_t
# therefore:
# h_0 = -f_2
# h_1 = 1-f_0
# h_2 = -f_1

F = F.flatten()
out1 = "F = [{0:.3f}, {1:.3f}, {2:.3f}]".format(F[0], F[1], F[2])
h0, h1, h2 = -F[2], 1 - F[0], -F[1]
out2 = "(h0, h1, h2) = ({0:.3f}, {1:.3f}, {2:.3f})".format(h0, h1, h2)

print(out1)
print(out2)

# y_{t+1} = 96.949 + y_t - 0.046*Y_t
# If there were n identical competitive firms all behaving according to
# the above equation the actual law of motion for market supply becomes:
# Y_{t+1} = n(96.949 + y_t - 0.046*Y_t)
#         = n*96.949 + (1-n*0.046)*Y_t
# which use Y_t = n*y_t (=> all firms behave according to y_t)

#endregion

#region Exercise 3
print '\nExercise 3 - Planner\'s problem'

# maximize area under demand curve versus minimizing changing output cost
# therefore the firm needs to minimize production cost sum_0^\infty beta^t * r_t
# where r_t = - int_0^Y_t (a_0 - a_1*x) dx + gamma(Y_{t+1}-Y_t)^2/2
#           = - a_0*Y_t + a_1/2*Y_t^2 + gamma(u_t)^2/2
# with u_t = Y_{t+t}-Y_t
#
# to write it in the form of LQ problem
# x_{t+1} = A*x_t + B*u_t
# r_t = x_t*R*x_t + u_t*Q*U_t (see above for definition of cost function for firm)
#
# if we set x_t = [Y_t 1] the we need to capture
# transition due to control Y_{t+1} = Y_t + u_t (= Y_t + Y_{t+1} - Y_t)

a0 = 100
a1 = 0.05
beta = 0.95
gamma = 10

# == LQ matrices == #

A = [[1, 0],
     [0, 1]]

B = [[1],
     [0]]

R = [[0.5*a_1, -0.5*a_0],
     [-0.5*a_0, 0]]

Q = gamma/2

# == run LQ to find stationary distributions/policy == #
lq = LQ(Q, R, A, B, beta=beta)
P, F, d = lq.stationary_values()
# F is optimal policy
# u_t = -F_t*x_t
# Y_{t+1}-Y_t = -f_0*Y_t - f_1
# Y_{t+1} = (1-f_0)*Y-t - f_1
# however we are looking for the format:
# Y_{t+1} = k_0 + k1*Y_t
# therefore:
F = F.flatten()
out1 = "F = [{0:.3f}, {1:.3f}]".format(F[0], F[1])
k0, k1 = -F[1], 1-F[0]
out2 = "(k0, k1) = ({0:.3f}, {1:.3f})".format(k0, k1)

print(out1)
print(out2)
#endregion

#region Exercise 4
print '\nExercise 4 - Monopolist\'s problem'

# monopolist is faced with industry demand curve:
# p_t = a_0 - a_1*Y_t
# and choose {Y_t} such thtat it minimizes a cost:
# C = sum_{t=0}^/infty /beta^2*r_t
# where r_t = -p_t*Y_t + gamma*(Y_{t+1}-Y_t)^2/2
#           = -a_0*Y_t + a_1*Y_t^2 + gamma*(Y_{t+1}-Y_t)^2/2
#
# to write it the problem in the form of LQ problem
# x_{t+1} = A*x_t + B*u_t
# r_t = x_t*R*x_t + u_t*Q*U_t (see above for definition of cost function for firm)
# we set x_t = [Y_t 1] because we need to capture
# transition due to control Y_{t+1} = Y_t + u_t (= Y_t + Y_{t+1} - Y_t)

a0 = 100
a1 = 0.05
beta = 0.95
gamma = 10

# == LQ matrices == #

A = [[1, 0],
     [0, 1]]

B = [[1],
     [0]]

R = [[a_1, -0.5*a_0],
     [-0.5*a_0, 0]]

Q = gamma/2

# == run LQ to find stationary distributions/policy == #
lq = LQ(Q, R, A, B, beta=beta)
P, F, d = lq.stationary_values()
# the optimal control policy is
# u_t = -F*x_t
# Y_{t+1} - Y_t = -f_0*Y_t -f_1
# thus Y_{t+t} = (1-f_0)*Y_t - f_1
# however we are looking for the format:
# Y_{t+1} = m_0 + m_1*Y_t
# therefore:
F = F.flatten()
out1 = "F = [{0:.3f}, {1:.3f}]".format(F[0], F[1])
m0, m1 = -F[1], 1-F[0]
out2 = "(m0, m1) = ({0:.3f}, {1:.3f})".format(m0, m1)

print out1
print out2
#endregion

