import torch
from torch import nn, optim
from torch.nn import functional as F


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class VAE(nn.Module):
    def __init__(self, len_comp):
        super(VAE, self).__init__()

        self.fc1 = nn.Linear(len_comp, 400)
        self.fc21 = nn.Linear(400, 20)
        self.fc22 = nn.Linear(400, 20)
        self.fc3 = nn.Linear(20, 400)
        self.fc4 = nn.Linear(400, len_comp)

        self.size = len_comp

    def encode(self, x):
        assert len(x) == self.size
        h1 = F.relu(self.fc1(x))
        return self.fc21(h1), self.fc22(h1)

    def reparametrize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps*std

    def decode(self, z):
        h3 = F.relu(self.fc3(z))
        return torch.sigmoid(self.fc4(h3))

    def forward(self, x):
        print(x.size(), self.size)
        assert len(x) == self.size
        mu, logvar = self.encode(x)
        z = self.reparametrize(mu, logvar)
        return self.decode(z), mu, logvar

model = VAE(1500).to(device)
optimizer = optim.Adam(model.parameters(), lr=1e-5)

def define_model(len_comp):
    model = VAE(len_comp).to(device)
    optimizer = optim.Adam(model.parameters(), lr=1e-5)
    return model, optimizer

def loss_function(recon_x, x, len_comp, mu, logvar):
    BCE = F.binary_cross_entropy(recon_x, x, reduction='sum')

    KLD = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())

    return BCE + KLD

def train(model, optimizer, songs, len_com):
    model.train()
    train_loss = 0
    iter = 0
    for s in songs:
        iter += 1
        s = torch.Tensor(s).to(device)
        optimizer.zero_grad()
        recon_batch, mu, logvar = model(s)
        loss = loss_function(recon_batch, s, len_com, mu, logvar)
        loss.backward()
        train_loss += loss.item()
        optimizer.step()
        print('Song # {}: [({:.0f}%)]\tLoss: {:.6f}, train loss: {}'.format(iter, 100. * (iter / len(songs)), loss.item() / len(s), train_loss))

    print('=====> Songs used: {}, Average Loss: {:.4f}'.format(len(songs), train_loss / len(songs)))

def test(model, songs, len_com):
    model.eval()
    test_loss = 0
    with torch.no_grad():
        for i, s in enumerate(songs):
            s = torch.Tensor(s).to(device)
            recon_batch, mu, logvar = model(s)
            test_loss += loss_function(recon_batch, s, len_com, mu, logvar)
    test_loss /= len(songs)
    print('=========> Test set loss: {:.4f}'.format(test_loss))


def UseVAE(songs, len_com):
    train_songs = songs[0:len(songs)-2]
    test_songs = songs[-2:]
    model, optimizer = define_model(len_com)

    train(model, optimizer, train_songs, len_com)
    test(model, test_songs, len_com)
    with torch.no_grad():
        sample = torch.randn(1, 20).to(device)
        sample = model.decode(sample).cpu()
        return list(sample.view(len_com, -1))
