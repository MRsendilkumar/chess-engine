import torch
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm

from model import SimpleModel
from data_loader import get_dataloader
import config

def train():
    # Dummy data for now
    data = torch.randn(1000, 10)

    dataloader = get_dataloader(data, config.BATCH_SIZE)

    model = SimpleModel(input_dim=10, hidden_dim=64, output_dim=1)
    model.to(config.DEVICE)

    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=config.LEARNING_RATE)

    for epoch in range(config.EPOCHS):
        epoch_loss = 0.0
        for x, y in tqdm(dataloader):
            x = x.to(config.DEVICE)
            y = y.float().to(config.DEVICE)

            optimizer.zero_grad()
            preds = model(x).squeeze()
            loss = criterion(preds, y)
            loss.backward()
            optimizer.step()

            epoch_loss += loss.item()

        print(f"Epoch {epoch+1}/{config.EPOCHS} | Loss: {epoch_loss:.4f}")

if __name__ == "__main__":
    train()
