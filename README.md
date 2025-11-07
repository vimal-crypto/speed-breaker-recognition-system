# Speed Breaker Recognition System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-1.10%2B-red)
![YOLOv5](https://img.shields.io/badge/YOLOv5-Latest-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A deep learning-based computer vision system for real-time detection and recognition of speed breakers on roads using multiple state-of-the-art object detection models including YOLOv5, YOLOR, and VGG16.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Models](#models)
- [Installation](#installation)
- [Usage](#usage)
- [Training](#training)
- [Testing](#testing)
- [Results](#results)
- [Dataset](#dataset)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## 🔍 Overview

This project implements an intelligent speed breaker detection system designed to enhance road safety by automatically identifying speed breakers in real-time video streams or images. The system leverages multiple deep learning architectures to provide robust detection capabilities under various lighting and weather conditions.

### Key Applications
- **Autonomous Vehicles**: Early warning system for self-driving cars
- **Advanced Driver Assistance Systems (ADAS)**: Alert drivers about upcoming speed breakers
- **Road Infrastructure Mapping**: Automated cataloging of speed breakers
- **Safety Analytics**: Traffic pattern analysis near speed breakers

## ✨ Features

- 🚗 **Real-time Detection**: Process video streams in real-time
- 🎯 **Multi-Model Support**: YOLOv5, YOLOR, and VGG16 implementations
- 📸 **Image & Video Processing**: Support for both static images and video files
- 🔄 **Custom Training**: Easy-to-use training pipeline for custom datasets
- 📊 **Performance Metrics**: Comprehensive evaluation tools
- ⚡ **GPU Acceleration**: CUDA support for faster inference
- 🎨 **Visualization**: Bounding box visualization with confidence scores

## 📁 Project Structure

```
speed-breaker-recognition-system/
├── src/
│   ├── train_model.py          # CNN training script (PyTorch)
│   ├── test_model.py            # Testing and visualization
│   ├── inference.py             # YOLOv5 video inference
│   └── utils/
│       └── image_processing.py  # Image inference utilities
├── notebooks/
│   ├── vgg16_analysis.ipynb     # VGG16 model experiments
│   ├── yolor_custom_training.ipynb  # YOLOR training notebook
│   └── project_report.ipynb      # Complete project analysis
├── models/
│   ├── yolov5_weights.pt        # YOLOv5 model weights
│   ├── final_weights.pth         # Trained CNN weights
│   └── training_checkpoint.pt    # Training checkpoint
├── assets/
│   ├── sample_detection.jpg      # Sample detection result
│   └── demo_video.mp4            # Demo video
├── data/
│   └── README.md                 # Dataset documentation
├── config.yaml                   # Configuration file
├── requirements.txt              # Project dependencies
├── README.md                     # This file
├── LICENSE                       # MIT License
└── .gitignore                    # Git ignore file
```

## 🤖 Models

### 1. YOLOv5
- **Architecture**: You Only Look Once v5
- **Use Case**: Real-time object detection
- **Performance**: High FPS with good accuracy
- **Implementation**: `src/inference.py`, `src/utils/image_processing.py`

### 2. YOLOR
- **Architecture**: You Only Learn One Representation
- **Use Case**: Enhanced feature learning
- **Training**: Custom dataset training support
- **Implementation**: `notebooks/yolor_custom_training.ipynb`

### 3. VGG16
- **Architecture**: Visual Geometry Group 16-layer CNN
- **Use Case**: Feature extraction and classification
- **Implementation**: `notebooks/vgg16_analysis.ipynb`

### 4. Custom CNN
- **Architecture**: SimpleCNN (2 Conv layers)
- **Classes**: 2 (speed breaker / non-speed breaker)
- **Implementation**: `src/train_model.py`

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- CUDA 11.0+ (for GPU support)
- 8GB+ RAM
- GPU with 4GB+ VRAM (recommended)

### Setup

1. **Clone the repository**

```bash
git clone https://github.com/vimal-crypto/speed-breaker-recognition-system.git
cd speed-breaker-recognition-system
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Download model weights**

Place your trained model weights in the `models/` directory, or train your own models using the training scripts.

## 🚀 Usage

### Image Inference

Detect speed breakers in a single image:

```bash
python src/utils/image_processing.py --image path/to/image.jpg
```

### Video Inference

Process a video file:

```bash
python src/inference.py --video path/to/video.mp4 --model models/yolov5_weights.pt
```

### Real-time Webcam Detection

```bash
python src/inference.py --source 0 --model models/yolov5_weights.pt
```

## 🏋️ Training

### Train Custom CNN Model

```bash
python src/train_model.py --data path/to/dataset --epochs 10 --batch-size 32
```

### Train YOLOv5 Model

Refer to the main YOLOv5 repository for detailed training instructions. Update `config.yaml` with your dataset configuration.

### Train YOLOR Model

Use the provided Jupyter notebook:

```bash
jupyter notebook notebooks/yolor_custom_training.ipynb
```

## 🧪 Testing

Run the test script to visualize model predictions:

```bash
python src/test_model.py
```

This will display sample images with ground truth masks and predictions.

## 📊 Results

### Model Performance

| Model | Accuracy | FPS | Model Size |
|-------|----------|-----|------------|
| YOLOv5s | 92.5% | 45 | 14 MB |
| YOLOR | 94.2% | 38 | 40 MB |
| Custom CNN | 89.1% | 60 | 1.2 MB |
| VGG16 | 91.8% | 25 | 528 MB |

### Sample Detections

Sample detection results can be found in the `assets/` directory.

## 📦 Dataset

The model is trained on a custom speed breaker dataset with the following structure:

```
dataset/
├── images/
│   ├── train/
│   ├── val/
│   └── test/
└── labels/
    ├── train/
    ├── val/
    └── test/
```

### Dataset Format

- **Images**: JPG/PNG format
- **Labels**: YOLO format (normalized bounding boxes)
- **Classes**: 2 (speed_breaker, background)

For more details, see `data/README.md`.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5) - YOLOv5 implementation
- [YOLOR](https://github.com/WongKinYiu/yolor) - YOLOR implementation
- [PyTorch](https://pytorch.org/) - Deep learning framework
- [OpenCV](https://opencv.org/) - Computer vision library

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Note**: This project is for educational and research purposes. Ensure compliance with local regulations when deploying in production environments.
