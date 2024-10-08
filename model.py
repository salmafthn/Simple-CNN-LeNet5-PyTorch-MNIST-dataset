from torch.nn import Module
from torch import nn

class Model(Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)  
        self.tanh1 = nn.Tanh()
        self.pool1 = nn.MaxPool2d(2, 2) 
        self.conv2 = nn.Conv2d(6, 16, 5)  
        self.tanh2 = nn.Tanh()
        self.pool2 = nn.MaxPool2d(2, 2)  
        self.conv3 = nn.Conv2d(16, 120, 4)  
        self.tanh3 = nn.Tanh()
        self.fc1 = nn.Linear(120, 84)  
        self.tanh4 = nn.Tanh()
        self.fc2 = nn.Linear(84, 10) 
        self.softmax = nn.Softmax(dim=1)  
      
    def forward(self, x):
        y = self.conv1(x)
        y = self.tanh1(y)
        y = self.pool1(y)
        y = self.conv2(y)
        y = self.tanh2(y)
        y = self.pool2(y)
        y = self.conv3(y)  
        y = self.tanh3(y)
        y = y.view(y.shape[0], -1)  
        y = self.fc1(y)
        y = self.tanh4(y)
        y = self.fc2(y)
        y = self.softmax(y)
        return y
