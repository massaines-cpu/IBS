# dataset pytorch

from torch.utils.data import Dataset
from preprocessing import load_eeg, create_epochs, normalize

class OpenDataset(Dataset):

    def __init__(self, data, transform=None):
        self.data = data
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        # recup les chemins des 2 eeg
        # eeg_A_path =
        # eeg_B_path =

        # charger les eeg
        # eeg_A = load_eeg(eeg_A_path)
        # eeg_B = load_eeg(eeg_B_path)

        # appliquer prétraitements

        # recup label
        # label =

        # return données
        # return eeg_A, eeg_B, label
        pass