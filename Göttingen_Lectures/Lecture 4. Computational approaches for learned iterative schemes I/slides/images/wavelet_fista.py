# Create space and data
space = odl.uniform_discr([-20, -20], [20, 20], shape=(256, 256))
phantom = odl.phantom.shepp_logan(space, modified=True)
data = phantom + 0.05 * odl.phantom.white_noise(space)

# Set up the wavelet trafo and the functionals
W = odl.trafos.WaveletTransform(space, wavelet='haar', nlevels=5)
l2_norm_sq = odl.solvers.L2NormSquared(space).translated(data)
data_discrepancy = l2_norm_sq * W.inverse
regularizer = 0.005 * odl.solvers.L1Norm(W.range)

# Solve the problem
x = data_discrepancy.domain.zero()  # start value
odl.solvers.accelerated_proximal_gradient(
    x, f=regularizer, g=data_discrepancy, niter=20, gamma=1.5)
