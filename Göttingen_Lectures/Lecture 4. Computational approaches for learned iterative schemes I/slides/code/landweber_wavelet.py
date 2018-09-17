W = odl.trafos.WaveletTransform(T.range)
S = W * T # Composition

landweber(S, f, g, niter, omega)
