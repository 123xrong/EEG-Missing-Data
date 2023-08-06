from cvxpy import *

def nuclear_norm_solve(A, mask, mu=1.0):
    X = Variable(shape=A.shape)
    objective = Minimize((mu * norm(X, "nuc")) + sum_squares(multiply(mask, X-A)))
    problem = Problem(objective, [])
    problem.solve(solver=SCS, eps=1e-8)
    return X.value