# Create reconstruction space and ray transform
space = odl.uniform_discr([-20, -20], [20, 20], shape=(256, 256))
geometry = odl.tomo.parallel_beam_geometry(space, num_angles=1000)
ray_transform = odl.tomo.RayTransform(space, geometry)

# Create artificial data with around 5 % noise (data max = 10)
phantom = odl.phantom.shepp_logan(space, modified=True)
g = ray_transform(phantom)
g_noisy = g + 0.5 * odl.phantom.white_noise(ray_transform.range)

# Solve inverse problem
x = space.zero()
odl.solvers.conjugate_gradient_normal(ray_transform, x, g_noisy, niter=20)

# Display results
phantom.show('Phantom')
g_noisy.show('Noisy data')
x.show('CGLS after 20 iterations')
