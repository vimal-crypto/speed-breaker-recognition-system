"""Image Inference Utilities for Speed Breaker Detection.

This module provides utilities for processing single images.
"""

import torch
import cv2

# Load your own pre-trained model
model = torch.load('epoch.pt')
model.eval()  # Set the model to evaluation mode

# Open the image
img = cv2.imread('image.jpg')

# Run your model on the image
with torch.no_grad():
    outputs = model(img)

# Process the outputs
for output in outputs:
    x1, y1, x2, y2, confidence, class_name = output
    if class_name == 'speed_breaker_alert':
        # Draw a bounding box around the detected speedbreaker
        img = cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

# Display the processed image
cv2.imshow('Speedbreaker Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
