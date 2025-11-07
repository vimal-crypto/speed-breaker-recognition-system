"""Main training script for YOLOv3 model on speed breaker dataset."""

import yaml
from ultralytics import YOLO
import torch

def train_yolov3():
    """Train YOLOv3 model for speed breaker detection."""
    # Load configuration
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    # Initialize model
    model = YOLO('yolov3.yaml')
    
    # Check device
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Training on device: {device}")
    
    # Training parameters
    results = model.train(
        data='data.yaml',
        epochs=config.get('epochs', 100),
        imgsz=config.get('img_size', 640),
        batch=config.get('batch_size', 16),
        device=device,
        workers=config.get('workers', 8),
        project='runs/train',
        name='speed_breaker_yolov3',
        exist_ok=True
    )
    
    # Save final model
    model.export(format='onnx')
    print("Training completed. Model exported to ONNX format.")

if __name__ == '__main__':
    train_yolov3()
