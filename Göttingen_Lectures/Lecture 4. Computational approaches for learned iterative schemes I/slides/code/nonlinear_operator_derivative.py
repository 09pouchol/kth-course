def derivative(self, rho):
    """Find derivative in point rho."""
    result = self.range.zero()
    for s, m in zip(self.sigma, self.mu):
        result -= (m * s) * np.exp(-m * self.ray_transform(rho))

    # Multiply vector with operator
    return result * self.ray_transform