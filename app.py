import cv2
import streamlit as st
from PIL import Image
import numpy as np
import time

st.title("📸 Real-time Webcam Stream")

# Start webcam
cap = cv2.VideoCapture(0)

# Placeholder for the stream
frame_placeholder = st.empty()

# Run until user stops
run = st.checkbox('Start Webcam')

if run:
    st.write("Press 'Stop Webcam' checkbox to stop.")
    while run:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to grab frame from webcam.")
            break

        # Convert BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Show frame
        frame_placeholder.image(frame, channels="RGB")

        # Check again for checkbox value
        run = st.session_state.get('Start Webcam', True)

    cap.release()
    st.write("Webcam stopped.")
else:
    st.write("Check the box to start the webcam.")
