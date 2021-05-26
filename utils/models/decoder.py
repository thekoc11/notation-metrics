import torch
import torch.nn as nn
import numpy as np
from residual import ResidualStack

class Decoder(nn.Module):
    def __init__(self, in_dim, h_dim, n_re_layers, residual=False, res_h_dim=None):
        super(Decoder, self).__init__()
        if residual is False:
            self.inverse_conv_stack = nn.Sequential(
                nn.ConvTranspose1d(
                    in_dim, h_dim, kernel_size=3, stride=1, padding=1),
                nn.ConvTranspose1d(h_dim, h_dim // 2, kernel_size=4, stride=2, padding=1),
                nn.ReLU(),
                nn.ConvTranspose1d(h_dim//2, 3, kernel_size=4, stride=2, padding=1)
            )
        else:
            self.inverse_conv_stack = nn.Sequential(
                nn.ConvTranspose1d(
                    in_dim, h_dim, kernel_size=3, stride=1, padding=1),
                ResidualStack(h_dim, h_dim, res_h_dim, n_re_layers),
                nn.ConvTranspose1d(h_dim, h_dim // 2, kernel_size=4, stride=2, padding=1),
                nn.ReLU(),
                nn.ConvTranspose1d(h_dim // 2, 3, kernel_size=4, stride=2, padding=1)
            )

    def forward(self, x):
        return self.inverse_conv_stack(x)


if __name__ == '__main__':
    x = torch.randn(3, 40, 200).float()

    decoder = Decoder(40, 128, 3, True, 64)
    decoder_out = decoder(x)
    print('decoder out shape (with residual): ', decoder_out.size())

    decoder1 = Decoder(40, 128, 3)
    decoder_out = decoder1(x)
    print('decoder out shape (without residual): ', decoder_out.size())
