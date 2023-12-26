## This file will create the layers needed for creating LenNet 5

class Convole:
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
    out = np.zeros((C, H, W))

    # 
    for c in range(C): 

      #Setting the limits for each horizontal pass of the kernal
      for h in range(H): 
        h_start = h
        h_end = h_start + self.Ker
        
        for w in range(W):                 
          w_start = w 
          w_end = w_start + self.Ker

          #
          out[c, h, w] = np.sum(input[:, h_start:h_end, w_start:w_end] * self.weights[c,:,:,:]) + self.bias[c]
          
    return out 
