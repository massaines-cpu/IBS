from dataset import OpenDataset
from model import Brain_Model
from train import train
from evaluate import evaluate

import torch
import torch.nn as nn
from torch.utils.data import DataLoader


def main():

    train_dataset = OpenDataset()
    test_dataset = OpenDataset()

    train_loader = DataLoader(
        train_dataset,
        batch_size=16,
        shuffle=True
    )
    # X, y = next(iter(train_loader))
    #
    # print(X.shape)
    # print(y.shape)
    # print(X.dtype)

    test_loader = DataLoader(
        test_dataset,
        batch_size=16,
        shuffle=False
    )

    model = Brain_Model()

    loss_fn = nn.BCEWithLogitsLoss()

    optimizer = torch.optim.Adam(
        model.parameters(),
        lr=1e-3
    )

    train(model, train_loader, optimizer, loss_fn)

    evaluate(model, test_loader, loss_fn)


if __name__ == "__main__":
    main()