1. The forward model is of the form  with the attenuation coefficient mu chosen to be 0.2. On MNIST (picture size 28^2), I currently use 5 directions for the rays, each of which has a resolution of 25 pixels. I apply Poisson noise to this at a level corresponding to a 60 photons measurement, meaning the simulated measurement distribution is given by Poisson(true_meas * 60)/60. I might reduce the amount of noise slightly the next days (number of photons around 100) to get better picture quality.

2. Learned reconstruction is learned gradient descent scheme. I use a slightly reduced model in comparison to the one presented in the paper in order to reduce training time. The network I have been using has 3 hidden layers and takes as input the current reconstruction image, the data gradient and the regulariser gradient only, but does not use any data of the algorithms history as proposed in your paper. These are details that are very easy to change though, so let me know if you want me to stick to the paper architecture and then I can run everything in that setting.
- Pretrained the network using L2 loss
- I pretrained for about 500 steps with a batch size of 64, so the amount of data points used is 64*500.

3. I used a standard CNN classifier with 3 convolutional layers, each followed by 2x2 max pooling. The activation functions used were Relus. The layers had 32,64 and 128 channels respectively. I ended with one dense layer that transformed the output of the last convolutional layer to a logit layer of size 10, with the last activation function being a softmax.
- Throughout the whole training I always used Cross-Entropy as loss function for the classifier
- Yes, I also pretrained the classifier until it had reached around 97.5\% accuracy on the normal MNIST data. The amount of training steps used for that was around 1000 (again each training step on a batch of size 64)

4. For joint reconstruction/ classification I simply took the output of the reconstruction algorithm as the input of the classifier and trained the combined network using only Cross-Entropy loss on the classifier output. 

5. Results
Each of the files represent reconstructions along with outcome of classification. Naming scheme of files is as follows with <nn>=0,...,4

L2LossClassificationComparison_Reconstruction_<nn>
Sequential pipeline: Reconstruction operator pre-trained with L^2-loss, classifier pre-trained with cross-entropy loss.

TrainClassifierOnly_Reconstruction_<nn>
Joint pipeline (partial joint training): Reconstruction operator pre-trained with $L^2$-loss, classifier trained with cross-entropy loss.

ClassificationLoss_Reconstruction_<nn>
Joint pipeline (partial joint training): Reconstruction operator trained with cross-entropy loss, classifier pre-trained with cross-entropy loss

JointlyTrained_Reconstruction_<nn>
Joint pipeline: Both Reconstruction operator and classifier trained with cross-entropy loss.

Corresponding files with 'FBP' in their names is sequential pipeline where reconstruction is by FBP followed by classifier pre-trained with cross-entropy loss.

Corresponding files with 'True' in their names is corresponding ground truth.