# Create space and noisy data
space = odl.uniform_discr([-20, -20], [20, 20], shape=(256, 256))
phantom = odl.phantom.shepp_logan(space, modified=True)
data = phantom + odl.phantom.white_noise(space) * 0.05

# Set up the wavelet trafo and the functionals
W = odl.trafos.WaveletTransform(space, wavelet='haar', nlevels=5)
Winv = W.inverse
l2_norm_sq = odl.solvers.L2NormSquared(space).translated(data)
data_discrepancy = l2_norm_sq * Winv
regularizer = 0.005 * odl.solvers.L1Norm(W.range)

# Solve the problem
gamma = 1.5  # parameter for the FISTA method
x = data_discrepancy.domain.zero()  # start value
odl.solvers.accelerated_proximal_gradient(
    x, f=regularizer, g=data_discrepancy, niter=20, gamma=gamma)
