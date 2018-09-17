>>> odl_op = odl.RayTransform(...)
>>> # Make a layer for Tensorflow
>>> tf_layer = odl.contrib.tensorflow.as_tensorflow_layer(odl_op)
>>> # Make a Theano operator
>>> theano_op = odl.contrib.theano.TheanoOperator(odl_op)
>>> # Make Torch autograd Function
>>> torch_op = odl.contrib.pytorch.TorchOperator(odl_op)
