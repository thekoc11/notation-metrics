import torch
import torch.nn as nn
import numpy as np
from encoder import Encoder
from quantizer import VectorQuantizer
from decoder import Decoder

class VQVAE(nn.Module):
    def __init__(self, h_dim, n_embeddings, embedding_dim, beta, residual = False, res_h_dim=None, n_res_layers=0):
        super(VQVAE, self).__init__()
        #encoder image into continupus latent space