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
    for c in range(n_C): # For each channel.
      for h in range(n_H): # Slide the filter vertically.
        h_start = h * self.s
        h_end = h_start + self.f
        
        for w in range(n_W): # Slide the filter horizontally.                
          w_start = w * self.s
          w_end = w_start + self.f

                    # Element wise multiplication + sum.
                    out[i, c, h, w] = np.sum(X[i, :, h_start:h_end, w_start:w_end] 
                                    * self.W['val'][c, ...]) + self.b['val'][c]
    return out 
