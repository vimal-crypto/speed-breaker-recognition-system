"""YOLOv5 Video Inference Script for Speed Breaker Detection.

This script processes video files and performs real-time detection.
"""

import torch
import cv2

# Load the YOLOv5 model from a local file
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5s.pt')

# Open the video capture
cap = cv2.VideoCapture('video.mp4')
if not cap.isOpened():
    print("Error opening video file")
    exit()

# Create a window to display the frames
cv2.namedWindow('Speedbreaker Detection', cv2.WINDOW_NORMAL)

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        print("Error reading frame from video")
        break

    # Convert the frame to the correct format (BGR to RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Run the YOLOv5 model on the frame
    results = model(frame_rgb)

    # Process the results
    speedbreaker_detected = False
    for result in results.xyxy[0]:
        x1, y1, x2, y2, confidence, class_idx = result
        class_name = model.names[int(class_idx)]
        if class_name == 'speed_breaker_alert':
            # Draw a bounding box around the detected speedbreaker
            frame = cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            speedbreaker_detected = True

    # Display the processed frame
    cv2.imshow('Speedbreaker Detection', frame)

    # Notify if a speedbreaker is detected
    if speedbreaker_detected:
        print("Speedbreaker detected!")

    # Wait for user input to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
