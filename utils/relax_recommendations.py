import streamlit as st
import webbrowser

def show_relaxation():
    st.subheader("🧘 Relaxation Corner")
    st.write("Feeling stressed? Try these:")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌬️ Breathing Exercise"):
            st.image("https://media.tenor.com/DtDdNODfISsAAAAC/breath-in-breath-out.gif")
    with col2:
        if st.button("🎵 Calming Music"):
            webbrowser.open("https://www.youtube.com/watch?v=2OEL4P1Rz04")
