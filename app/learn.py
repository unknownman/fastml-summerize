from typing import List

import torch
import torch.nn as nn
import torch.optim as optim

from app.dataset import PersianDataset
from app.summarizer import Summarizer


def train_model(dataset: PersianDataset, model: Summarizer, epochs: int, batch_size: int, learning_rate: float):
    # Define loss function and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # Set the model to training mode
    model.train()

    # Train the model for the specified number of epochs
    for epoch in range(epochs):
        running_loss = 0.0
        for i in range(0, len(dataset), batch_size):
            # Get a batch of data and labels
            inputs, labels = dataset.get_batch(i, i + batch_size)

            # Zero the parameter gradients
            optimizer.zero_grad()

            # Forward pass, backward pass, and optimization
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # Print statistics
            running_loss += loss.item()
            if i % 1000 == 999:
                print(
                    f"[Epoch {epoch + 1}, Batch {i + 1}] loss: {running_loss / 1000:.3f}")
                running_loss = 0.0

    print("Finished training")
