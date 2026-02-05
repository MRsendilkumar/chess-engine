import torch
from torch.utils.data import Dataset, DataLoader

class CustomDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        x = self.data[idx]
        y = 0  # placeholder label
        return x, y

def get_dataloader(data, batch_size):
    dataset = CustomDataset(data)
    return DataLoader(dataset, batch_size=batch_size, shuffle=True)
