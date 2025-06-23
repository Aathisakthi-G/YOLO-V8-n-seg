# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 21:23:57 2025

@author: aathi
"""

import os

# Get the current working directory
current_directory = os.getcwd()

print("Current Working Directory:", current_directory)

# Set a new working directory
new_directory = r"C:\Users\aathi\Downloads\OFF_PROJECT-1\runs_model\runs-20250130T171623Z-001\runs\segment"
os.chdir(new_directory)


import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import tempfile

# Load the YOLOv8 model
model_path = r"C:\Users\aathi\Downloads\OFF_PROJECT-1\runs_model\runs-20250130T171623Z-001\runs\segment\train4\weights\best.pt"  # Update with your actual path
model = YOLO(model_path)

# Streamlit app title
st.title("Highway Inspection and Maintenance Using AI")

# Sidebar for navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose the app mode", ["About", "Run on Image", "Run on Video", "Run on Webcam"])

if app_mode == "About":
    st.markdown("This app uses YOLOv8 for object detection and segmentation. You can upload images or videos to see the model in action.")

elif app_mode == "Run on Image":
    st.header("Upload an Image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_container_width=True)

        # Convert the image to a format suitable for YOLOv8
        image_np = np.array(image)
        results = model(image_np)

        # Draw bounding boxes and segmentation masks on the image
        for result in results:
            annotated_image = result.plot()

        st.image(annotated_image, caption='Processed Image', use_container_width=True)

elif app_mode == "Run on Video":
    st.header("Upload a Video")
    uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "mov", "avi", "mkv"])

    if uploaded_file is not None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())

        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Run YOLOv8 model on the frame
            results = model(frame)

            # Draw bounding boxes and segmentation masks on the frame
            for result in results:
                annotated_frame = result.plot()

            # Display the frame
            stframe.image(annotated_frame, channels="BGR")

        cap.release()

elif app_mode == "Run on Webcam":
    st.header("Live Webcam Feed")
    run_webcam = st.button("Start Webcam")
    stop_webcam = st.button("Stop Webcam")
    
    if run_webcam:
        cap = cv2.VideoCapture(0)
        stframe = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                st.write("Webcam not detected.")
                break

            # Run YOLOv8 model on the frame
            results = model(frame)

            # Draw bounding boxes and segmentation masks on the frame
            for result in results:
                annotated_frame = result.plot()

            # Display the frame
            stframe.image(annotated_frame, channels="BGR")
            
            if stop_webcam:
                break

        cap.release()
        cv2.destroyAllWindows()
