def landweber(T, f, g, omega, K):
    for i in range(K):
        f += omega * T.derivative(f).adjoint(g - T(f))
