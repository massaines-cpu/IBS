# modèle

import torch.nn as nn

class Brain_Model(nn.Module):
    def __init__(self):
        super().__init__()

        self.net = nn.Sequential(
            nn.Conv1d(in_channels=nb_channel, #X.shape[1]
                      out_channels=32, kernel_size=7),
            nn.ReLU(),
            nn.MaxPool1d(2),

            nn.Conv1d(32, 64, kernel_size=5),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(1),

            nn.Flatten(),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        return self.net(x).squeeze(1)

