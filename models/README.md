# Model Weights

This directory contains the trained model weights for the Speed Breaker Recognition System.

## Available Models

### YOLOv5 Models
- `yolov5_best.pt` - Best performing YOLOv5 model
- `yolov5_last.pt` - Latest checkpoint

### YOLOR Models
- `yolor_best.pt` - Best performing YOLOR model
- `yolor_last.pt` - Latest checkpoint

### VGG16 Models
- `vgg16_model.h5` - Trained VGG16 model
- `vgg16_weights.h5` - Model weights only

## Model Performance

| Model | mAP@0.5 | mAP@0.5:0.95 | Inference Time (ms) | Size (MB) |
|-------|---------|--------------|---------------------|----------|
| YOLOv5 | 0.92 | 0.78 | 15 | 14.1 |
| YOLOR | 0.94 | 0.81 | 22 | 37.2 |
| VGG16 | 0.88 | 0.72 | 45 | 58.9 |

## Download Pre-trained Weights

Due to file size limitations, model weights are hosted externally:

```bash
# Download YOLOv5 weights
wget https://github.com/vimal-crypto/speed-breaker-recognition-system/releases/download/v1.0/yolov5_best.pt -P models/

# Download YOLOR weights
wget https://github.com/vimal-crypto/speed-breaker-recognition-system/releases/download/v1.0/yolor_best.pt -P models/

# Download VGG16 weights
wget https://github.com/vimal-crypto/speed-breaker-recognition-system/releases/download/v1.0/vgg16_model.h5 -P models/
```

## Training Your Own Models

Refer to the main [README](../README.md#training) for training instructions.

## Model Details

### YOLOv5
- **Input Size:** 640x640
- **Classes:** 1 (speed_breaker)
- **Backbone:** CSPDarknet53
- **Training Dataset:** 5000+ annotated images

### YOLOR
- **Input Size:** 640x640
- **Classes:** 1 (speed_breaker)
- **Backbone:** CSPDarknet with implicit knowledge
- **Training Dataset:** 5000+ annotated images

### VGG16
- **Input Size:** 224x224
- **Classes:** Binary classification
- **Architecture:** VGG16 with custom top layers
- **Training Dataset:** 5000+ annotated images

## Usage

```python
from ultralytics import YOLO

# Load model
model = YOLO('models/yolov5_best.pt')

# Run inference
results = model('path/to/image.jpg')
```

## License

Model weights are released under the MIT License.
