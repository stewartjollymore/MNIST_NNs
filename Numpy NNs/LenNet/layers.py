## This file will create the layers needed for creating LenNet 5

class Convole:
  def __init__(self, number_filter, filter_size, channels, padding, lr, layer_name):
    self.F = number_filter
    self.Fs = filter_size
    self.C = channels
    self.p = padding
    self.lr = lr
    self.name = layer_name
