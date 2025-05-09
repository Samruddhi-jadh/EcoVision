import cv2
import torch
import argparse
import os
from ultralytics import YOLO

# Argument parser for command-line inputs
parser = argparse.ArgumentParser(description="Plastic Waste Detection using YOLOv8")
parser.add_argument("--source", type=str, required=True, help="Path to image, video file, or folder")
parser.add_argument("--model", type=str, default="models/yolov8_weights.pt", help="Path to trained YOLO model")
parser.add_argument("--conf", type=float, default=0.5, help="Confidence threshold")
parser.add_argument("--output", type=str, default="results/", help="Directory to save results")

args = parser.parse_args()

# Load the trained YOLOv8 model
model = YOLO(args.model)

# Ensure the output directory exists
os.makedirs(args.output, exist_ok=True)

# Check if input is a folder (batch processing)
if os.path.isdir(args.source):
    print(f"📂 Processing images in folder: {args.source} ...")
    results = model.predict(source=args.source, conf=args.conf, save=True, project=args.output, name="detections")
    print(f"✅ All images processed. Results saved in: {args.output}/detections")

# Check if input is a single image
elif os.path.isfile(args.source):
    print(f"🖼️ Processing image: {args.source} ...")
    results = model.predict(source=args.source, conf=args.conf)
    
    for result in results:
        img = result.plot()  # Draw bounding boxes
        output_path = os.path.join(args.output, os.path.basename(args.source))
        cv2.imwrite(output_path, img)  # Save processed image
        print(f"✅ Processed: {args.source} -> Saved: {output_path}")

# Error handling if the source is invalid
else:
    print("❌ Error: Source file or folder does not exist! Please check the path.")
