import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class Encoder(nn.Module):
    def __init__(self, in_dim, h_dim, residual=False):
        super(Encoder, self).__init__()
        kernel = 4
        stride = 2
        self.conv_stact = nn.Sequential(
            nn.Conv1d(in_dim, h_dim // 2, kernel_size=kernel,
                      stride=stride, padding=1),
            nn.ReLU(),
            nn.Conv1d(h_dim // 2, h_dim, kernel_size=kernel,
                      stride=stride, padding=1),
            nn.ReLU(),
            nn.Conv1d(h_dim, h_dim, kernel_size=kernel-1,
                      stride=stride-1, padding=1),
            nn.ReLU()
        )

    def forward(self, x):
        return self.conv_stact(x)

if __name__ == '__main__':
    x = np.random.random_sample((25, 3, 15))
    x = torch.tensor(x).float()

    encoder = Encoder(3, 7)
    encoder_out = encoder(x)
    print(encoder_out.shape)