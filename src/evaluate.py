# évaluation
from torch.utils.data import DataLoader
from dataset import OpenDataset

test_dataset = OpenDataset()

test_loader = DataLoader(
    test_dataset,
    batch_size=16,
    shuffle=False
)
def evaluate(model, dataloader, loss_fn):
    pass
