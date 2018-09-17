scales = W.scales()
pre_factor = np.power(1.7, -scales)
Winv = W.inverse * pre_factor
