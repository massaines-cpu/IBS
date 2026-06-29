# entrainement
from dataset import OpenDataset
from torch.utils.data import DataLoader

def train(model, dataloader, optimizer, loss_fn):
    pass

train_dataset = OpenDataset()

train_loader = DataLoader(
    train_dataset,
    batch_size=16,
    shuffle=True
)