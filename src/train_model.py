"""Training script for Speed Breaker Detection using Custom CNN.

This script trains a simple CNN model for binary classification:
- Class 0: No speed breaker
- Class 1: Speed breaker present
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from PIL import Image
import os

# Define your CNN model
class SimpleCNN(nn.Module):
    def __init__(self, num_classes):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(32 * 32 * 32, num_classes)  # Adjust the input size based on the output from conv layers

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        
        # Adjust the view operation based on the actual size of the tensor
        x = x.view(-1, 32 * 32 * 32)
        x = self.fc1(x)
        return x

# Define hyperparameters
batch_size = 32
learning_rate = 0.001
epochs = 10
num_classes = 2  # Assuming you have 2 classes: speed breaker and non-speed breaker

# Define data transformations
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
])

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define your custom dataset class
class CustomDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.images = [f for f in os.listdir(root_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, self.images[idx])
        image = Image.open(img_name).convert('RGB')

        if self.transform:
            image = self.transform(image)

        label_filename = f"labels/{os.path.splitext(self.images[idx])[0]}.txt"
        label_path = os.path.join(self.root_dir, label_filename)

        # Default to label 0 if file not found
        label = self.load_label(label_path) if os.path.exists(label_path) else 0

        return image, label

    def load_label(self, label_path):
        # Implement a function to load labels from the file
        # Replace this with your actual logic
        # Example: Read label from a text file
        with open(label_path, 'r') as file:
            label = int(file.read().strip())
        return label

# Create dataset and dataloaders
train_dataset = CustomDataset("archive/dataspeed/data/train/images", transform=transform)
val_dataset = CustomDataset("archive/dataspeed/data/val/images", transform=transform)

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, pin_memory=True, num_workers=4)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, pin_memory=True, num_workers=4)

# Initialize the model, loss function, and optimizer
model = SimpleCNN(num_classes=num_classes).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Training loop
if __name__ == '__main__':
    for epoch in range(epochs):
        model.train()
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)

            # Manually handle batch size mismatch
            batch_size = min(outputs.size(0), labels.size(0))
            loss = F.cross_entropy(outputs[:batch_size], labels[:batch_size])

            loss.backward()
            optimizer.step()

        # Validation loop
        model.eval()
        val_loss = 0.0
        correct = 0
        total = 0
        with torch.no_grad():
            for val_images, val_labels in val_loader:
                val_images, val_labels = val_images.to(device), val_labels.to(device)

                val_outputs = model(val_images)

                # Manually handle batch size mismatch
                val_batch_size = min(val_outputs.size(0), val_labels.size(0))
                val_loss = F.cross_entropy(val_outputs[:val_batch_size], val_labels[:val_batch_size])

                _, predicted = val_outputs.max(1)
                total += val_batch_size
                correct += predicted.eq(val_labels[:val_batch_size]).sum().item()

        accuracy = correct / total
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item()}, Val Loss: {val_loss/len(val_loader)}, Accuracy: {accuracy}")

    # Save the trained model
    torch.save(model.state_dict(), "model.pth")
    print("Model saved successfully!")
