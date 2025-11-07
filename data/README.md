# Dataset Directory

This directory contains the speed breaker dataset for training and testing.

## Dataset Structure

```
data/
├── train/
│   ├── images/
│   └── labels/
├── val/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/
```

## Dataset Statistics

- **Total Images:** 5000+
- **Training Set:** 3500 images (70%)
- **Validation Set:** 1000 images (20%)
- **Test Set:** 500 images (10%)
- **Image Resolution:** Variable (640x640 recommended)
- **Annotation Format:** YOLO format (.txt files)

## Classes

| Class ID | Class Name | Description |
|----------|------------|-------------|
| 0 | speed_breaker | Road speed breaker/bump |

## Data Collection

Images were collected from:
- Real-world road camera footage
- Dashcam recordings
- Public datasets
- Manually captured images

## Annotation Format

YOLO format annotations (one .txt file per image):

```
<class_id> <x_center> <y_center> <width> <height>
```

All values are normalized (0-1 range).

**Example:**
```
0 0.512 0.384 0.165 0.092
```

## Download Dataset

Due to size limitations, the dataset is hosted externally:

```bash
# Download complete dataset
wget https://github.com/vimal-crypto/speed-breaker-recognition-system/releases/download/v1.0/dataset.zip

# Extract
unzip dataset.zip -d data/
```

## Data Augmentation

Applied during training:
- Horizontal flip (50% probability)
- HSV augmentation
- Random scaling (±50%)
- Random translation (±10%)
- Mosaic augmentation

## Dataset Preparation

To prepare your own dataset:

1. **Organize images:**
   ```bash
   data/train/images/*.jpg
   data/val/images/*.jpg
   data/test/images/*.jpg
   ```

2. **Create annotations:**
   - Use tools like [LabelImg](https://github.com/tzutalin/labelImg)
   - Export in YOLO format
   - Save to corresponding labels/ directories

3. **Create data.yaml:**
   ```yaml
   train: data/train/images
   val: data/val/images
   test: data/test/images
   nc: 1
   names: ['speed_breaker']
   ```

## Dataset Quality

- All images manually reviewed
- Annotations verified for accuracy
- Diverse lighting conditions included
- Multiple angles and perspectives
- Various speed breaker types

## License

Dataset is provided under MIT License for research and educational purposes.
