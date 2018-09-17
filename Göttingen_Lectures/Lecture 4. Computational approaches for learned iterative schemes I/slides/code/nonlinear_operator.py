class SpectralProjector(odl.Operator):
    def __init__(self, ray_transform, sigma, mu):
        """Initialize the operator."""
        self.ray_transform = ray_transform
        self.sigma = sigma
        self.mu = mu
        super().__init__(domain=ray_transform.domain,
                         range=ray_transform.range,
                         linear=False)

    def _call(self, rho):
        """Evaluate forward operator in point rho."""
        pass

    def derivative(self, rho):
        """Find derivative in point rho."""
        pass