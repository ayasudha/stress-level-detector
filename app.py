import streamlit as st
from webcam_emotion_detector import start_detection
from stress_tracker import plot_stress_graph
from utils.relax_recommendations import show_relaxation

st.set_page_config(page_title="Stress Level Detector", layout="centered")

st.title("🧠 Stress Level Detector Using Webcam")
st.markdown("Detect stress, fatigue, or anxiety using your facial expressions in real-time.")

if st.button("▶ Start Stress Detection"):
    start_detection()

st.markdown("---")
st.subheader("📊 Stress Trend")
plot_stress_graph()

st.markdown("---")
show_relaxation()
