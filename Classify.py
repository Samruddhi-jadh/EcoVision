import torch
import argparse
from ultralytics import YOLO

# Load trained waste classifier
parser = argparse.ArgumentParser(description="Waste Classification")
parser.add_argument("--source", type=str, required=True, help="Path to image")
parser.add_argument("--model", type=str, default="models/classifier_weights.pt", help="Path to classifier model")
args = parser.parse_args()

model = YOLO(args.model)

# Run classification
results = model(args.source)
for r in results:
    print(f"Detected: {r.names[r.probs.top1]} with confidence {r.probs.top1conf:.2f}")
