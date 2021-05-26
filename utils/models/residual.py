import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class ResidualLayer(nn.Module):
    def __init__(self, in_dim, h_dim, res_h_dim):
        super(ResidualLayer, self).__init__()
        self.res_block = nn.Sequential(
            nn.ReLU(True),
            nn.Conv1d(in_dim, res_h_dim, kernel_size=3,
                      stride=1, padding=1, bias=False),
            nn.ReLU(True),
            nn.Conv1d(res_h_dim, h_dim, kernel_size=1,
                      stride=1, bias=False)
        )

    def forward(self, x):
        x = x + self.res_block(x)
        return x


class ResidualStack(nn.Module):
    def __init__(self, in_dim, h_dim, res_h_dim, n_res_layers):
        super(ResidualStack, self).__init__()
        self.n_res_layers = n_res_layers
        self.stack = nn.ModuleList([ResidualLayer(in_dim, h_dim, res_h_dim)]*n_res_layers)

    def forward(self, x):
        for l in self.stack:
            x = l(x)
        x = F.relu(x)

        return x


if __name__ == '__main__':
    x = torch.randn(3, 15, 20).float()
    # print(x)

    res = ResidualLayer(15, 15, 7)
    res_out = res(x)
    print('Res x out shape: ', res_out.size())
    res_stack = ResidualStack(15, 15, 7, 3)
    res_stack_out = res_stack(x)
    print('Res stack x out shape', res_stack_out.size())
