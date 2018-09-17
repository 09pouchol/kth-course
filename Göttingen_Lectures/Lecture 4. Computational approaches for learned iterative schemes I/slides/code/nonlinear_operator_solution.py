# Create ray transform
space = odl.uniform_discr([-20, -20], [20, 20], shape=(256, 256))
geometry = odl.tomo.parallel_beam_geometry(space, angles=1000)
ray_transform = odl.tomo.RayTransform(space, geometry)

# Create forward operator
forward_op = SpectralProjector(ray_transform, sigma=[0.5, 0.5], mu=[0.05, 0.1])

# Create artificial data
phantom = odl.phantom.shepp_logan(space)
g = forward_op(phantom)
g_noisy = odl.phantom.poisson_noise(g * 100000) / 100000

# Monochromatic (linear) approximation by FBP 
fbp_op = odl.tomo.fbp_op(ray_transform, filter_type='Hann')
fbp_result = fbp_op(-np.log(g_noisy) * 14)

# Solve (nonlinear) inverse problem by Landweber
x = fbp_result.copy()
odl.solvers.landweber(spectral_projector, x, g_noisy, niter=100, omega=10.0)