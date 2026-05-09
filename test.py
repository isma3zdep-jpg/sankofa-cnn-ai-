import torch
import torch.nn as nn
import torchvision as tv
import torchvision.transforms as transforms
import matplotlib.pyplot as plt

# parameters
lr = 0.001
epoch = 50
batch_size = 10000
input_calsses = 784
output_calsses = 10

hidden_lyers = 5
hiddeen_layers_n = 500 # neouron number

# the data
train_dataset = tv.datasets.MNIST(root=r'C:\Users\sanko\OneDrive\Desktop\codes\AI', train=True, transform=transforms.ToTensor(), download=True)
test_dataset = tv.datasets.MNIST(root=r'C:\Users\sanko\OneDrive\Desktop\codes\AI', train=False, transform=transforms.ToTensor())

train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=True)

examples = iter(train_loader)


# class
class model(nn.Module):
    def __init__(self, input_size=input_calsses, hidden_size=hiddeen_layers_n, num_classes=output_calsses, num_layers=hidden_lyers):
        super(model, self).__init__()
        self.layers = nn.ModuleList()
        self.layers.append(nn.Linear(input_size, hidden_size))
        for _ in range(num_layers - 1):
            self.layers.append(nn.Linear(hidden_size, hidden_size))
        self.last_layer = nn.Linear(hidden_size, num_classes)
        self.active = nn.Sigmoid()

    def forward(self, x, return_acts=False):
        acts = []
        for layer in self.layers:
            x = self.active(layer(x))
            acts.append(x)

        out = self.last_layer(x)

        if return_acts:
            return out, acts
        return out

ai = model()

# optim and loss
loss = nn.CrossEntropyLoss()
optim = torch.optim.Adam(ai.parameters(), lr=lr)


# loop training

for e in range(epoch + 1):
    for i, (images, labels) in enumerate(train_loader):
        x = images.view(-1, 784)
        y = ai(x)

        l = loss(y, labels)
        l.backward()

        optim.step()
        optim.zero_grad()

        print(f'epoch : {e+1} , batch : {i+1}')



