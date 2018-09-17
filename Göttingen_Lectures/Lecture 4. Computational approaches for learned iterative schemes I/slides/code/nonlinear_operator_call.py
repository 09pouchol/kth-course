def _call(self, rho):
    """Evaluate forward operator in point rho."""
    result = self.range.zero()
    for s, m in zip(self.sigma, self.mu):
        result += s * np.exp(- m * self.ray_transform(rho))

    return result