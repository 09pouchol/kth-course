# Code from above ...

# Isotropic TV-regularizer
gradient = odl.Gradient(space)
regularizer = 0.01 * odl.solvers.L1Norm(gradient.range)

# Enforce 0 < f < 1
f = odl.solvers.IndicatorBox(space, 0, 1)

# Data discrepancy || . - g||_2^2
data_discr = odl.solvers.L2NormSquared(ray_transform.range).translated(g_noisy)

# Solve using Douglas Rachford Primal-Dual
x = space.zero()
odl.solvers.douglas_rachford_pd(x,
                                f, g=[data_discr, regularizer],
                                L=[ray_transform, gradient],
                                tau=1.0, sigma=[0.01, 0.01], niter=100)