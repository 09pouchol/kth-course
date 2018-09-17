# Read or generate data, Compute the exponent from the data
...

# Setup functionals and operators
data_matching = odl.solvers.L2NormSquared(reco_space).translated(data)
varlp_func = variable_lp.VariableLpModular(gradient.range, exponent)
regularizer = 2e-1 * varlp_func
constraint = odl.solvers.IndicatorBox(reco_space, -5, 5)

lin_ops = [odl.IdentityOperator(reco_space), gradient]

# Start iteration from the noisy data
x = data.copy()

# Choose optimization parameters and go
odl.solvers.douglas_rachford_pd(x, constraint, [data_matching, regularizer],
                                lin_ops, tau=tau, sigma=sigma, lam=lam,
                                niter=100)
