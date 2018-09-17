>>> space_cpu = odl.rn((2, 3, 4))  # NumPy backend
>>> x_cpu = space_cpu.zero()
>>> x_cpu[:, :3, ::2] = -5
>>> x_cpu[0]
rn((3, 4)).element(
    [[-5.,  0., -5.,  0.],
     [-5.,  0., -5.,  0.],
     [-5.,  0., -5.,  0.]]
)

>>> space_gpu = odl.rn((2, 3, 4), impl='cupy')  # cupy backend
>>> x_gpu = space_gpu.zero()
>>> x_gpu[:, :3, ::2] = -5
>>> x_gpu[0]
rn((3, 4), impl='cupy').element(
    [[-5.,  0., -5.,  0.],
     [-5.,  0., -5.,  0.],
     [-5.,  0., -5.,  0.]]
)
