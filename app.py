import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO

# Load YOLO model
model = YOLO("models/yolov8_weights.pt")

# Set page config
st.set_page_config(page_title="EcoVision", layout="wide")

# Main Title
st.title("♻️ EcoVision: AI-Powered  Waste Detection in Oceans 🌊")

# Sidebar UI
st.sidebar.title("🌊 Ocean Cleanup AI")
st.sidebar.markdown("**Detect waste in marine images using advanced AI.**")
confidence = st.sidebar.slider("🎯 Confidence Threshold", 0.1, 1.0, 0.5, 0.05)

# Upload image
uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Convert to OpenCV format
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Create two columns
    col1, col2 = st.columns(2)

    with col1:
        st.image(image, channels="BGR", caption="🖼 Original Image")

    # Detect button with spinner
    if st.button("🔍 Detect Plastic Waste"):
        with st.spinner("🚀 Processing... Please wait!"):
            results = model(image, conf=confidence)

            # Process results
            for result in results:
                labeled_image = result.plot()

        with col2:
            st.image(labeled_image, channels="BGR", caption="✅ Detection Result")

# Custom CSS for styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #007BFF;
        color: white;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    </style>
""", unsafe_allow_html=True)
