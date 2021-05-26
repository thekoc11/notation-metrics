import math
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np

class RNNModel(nn.Module):
    def __init__(self, rnn_type, ntoken, ninp, nhid, nlayers, dropout=0.5, tie_weights=False):
        super(RNNModel, self).__init__()
        self.ntoken = ntoken
        self.drop = nn.Dropout(dropout)
        self.encoder = nn.Embedding(ntoken, ninp)
        if rnn_type in ['LSTM', 'GRU']:
            self.rnn = getattr(nn, rnn_type)(ninp, nhid, nlayers, dropout=dropout)
        else:
            try:
                nonlinearity = {'RNN_TANH': 'tanh', 'RNN_RELU': 'relu'}[rnn_type]
            except KeyError:
                raise ValueError("""Invalid option for `model`""")

            self.rnn = nn.RNN(ninp, nhid, nlayers, nonlinearity=nonlinearity, dropout=dropout)

        self.decoder = nn.Linear(nhid, ntoken)

        if tie_weights:
            if nhid != ninp:
                raise ValueError('When using tie flag, nhid == emsize')
            self.decoder.weight = self.encoder.weight


        self.rnn_type = rnn_type
        self.nhid = nhid
        self.nLayers = nlayers

        self.init_weights()

    def init_weights(self):
        initrange = 0.1
        nn.init.uniform_(self.encoder.weight, -initrange, initrange)
        nn.init.zeros_(self.decoder.weight)
        nn.init.uniform_(self.decoder.weight, -initrange, initrange)

    def forward(self, input, hidden):
        emb = self.drop(self.encoder(input))
        output, hidden = self.rnn(emb, hidden)
        output = self.drop(output)
        decoded = self.decoder(output)
        decoded = decoded.view(-1, self.ntoken)
        return F.log_softmax(decoded, dim=1), hidden

    def init_hidden(self, bsz):
        weight = next(self.parameters())
        if self.rnn_type == 'LSTM':
            return (weight.new_zeros(self.nLayers, bsz, self.nhid),
                    weight.new_zeros(self.nLayers, bsz, self.nhid))
        else:
            return weight.new_zeros(self.nLayers, bsz, self.nhid)

def get_batch(source, i):
    seq_len = min(25, len(source) -1 - i)
    data = source[i:i+seq_len]
    return data

if __name__ == '__main__':
    x = np.random.random_sample((3, 40, 40, 200))
    x = torch.tensor(x).int()
    x = x.view(3, -1)

    data_x = x[:, 0:25]

    rnn = RNNModel('RNN_TANH', 40, 200, 50, 4)
    hidden = rnn.init_hidden(25)
    rnn_out = rnn(data_x, hidden)
    print(hidden.size(), data_x.size())