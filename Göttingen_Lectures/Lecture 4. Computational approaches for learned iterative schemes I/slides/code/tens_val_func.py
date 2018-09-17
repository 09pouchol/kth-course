>>> # Vector-valued functions, 2 components
>>> space = odl.uniform_discr(0, 1, 5, dtype=(float, (2,)))
>>> def f(x):
...     return (x + 1, x ** 2 - 1)
>>> f_elem = space.element(f)
>>> f_elem  # Discretized using vectorized evaluation
uniform_discr(0.0, 1.0, 5, dtype=('float64', (2,))).element(
    [[ 1.1   1.3   1.5   1.7   1.9 ]
     [-0.99 -0.91 -0.75 -0.51 -0.19]]
)
