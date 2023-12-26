## This file will create the layers needed for creating LenNet 5

class Convole():

	"""

 This model is coded to be run for a basic LenNet.  My choice to hard code some things was to ensure 
 that I could focus on the architecture of the CNN rather than generalizable. 

 Things that are hard coded is padding, which is set to zero, and stride, which is set to 1.

 	"""
  def __init__(self, number_filter, filter_size, channels, lr, layer_name):
    self.Filter = number_filter
    self.Ker = filter_size
    self.Chan = channels
    self.lr = lr
    self.name = layer_name
    self.weights = np.zeros((self.Filter, self.Chan, self.Ker, self.Ker))
    self.bias = np.zeros((self.Filter, 1))


  def forward_conv(self, input):
    """
     
    """
    

    # Define output size.
    C = input.shape[0]
    H = int((input.shape[1] - self.Ker)) + 1
    W = int((input.shape[2] - self.Ker)) + 1

    self.inputs = np.zeros((C, W, H))
    
    out = np.zeros((C, H, W))

    # 
    for k in range(self.Ker): 

      #Setting the limits for each horizontal pass of the kernal
      for h in range(H): 
        h_start = h
        h_end = h_start + self.Ker
        
        for w in range(W):                 
          w_start = w 
          w_end = w_start + self.Ker

          #
          out[k, h, w] = np.sum(self.inputs[:, h_start:h_end, w_start:w_end] * self.weights[k,:,:,:]) + self.bias[k]
          
    return out 

  def backward(self, grad_output):
    
    C, W, H = self.inputs.shape
    
    grad_input = np.zeros(self.inputs.shape)
    wgrad = np.zeros(self.weights.shape)
    bgrad = np.zeros(self.bias.shape)

    F, W, H = grad_output.shape
    for f in range(F):
      for h in range(0, H, 1):
				
				h_start = h
      	h_end = h_start + self.Ker
			
        for w in range(0, W, 1):
					
					 w_start = w 
         	 w_end = w_start + self.K
			
         	 wgrad[f,:,:,:] += grad_output[f,w,h]*self.inputs[:, w_start:w_end, h_start:h_end]
			
         	 grad_input[:, w_start:w_end, h_start:h_end] += grad_output[f,w,h]*self.weights[f,:,:,:]

    for f in range(F):
       bgrad[f] = np.sum(dy[f, :, :])

    self.weights -= self.lr * wgrad
    self.bias -= self.lr * bgrad
    
    return grad_input

def return_params(self):
	return {self.name+'.weights':self.weights, self.name+'.bias':self.bias}

