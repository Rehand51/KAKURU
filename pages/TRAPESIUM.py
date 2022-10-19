import streamlit as st

st.title("RUMUS TRAPESIUM")
st.header("===LUAS===")
alsa = st.number_input("Masukan Nilai Alas A")
alsb = st.number_input("Masukan Nilai Alas B")
t = st.number_input("Masukan Nilai Tinggi")
l = alsa + alsb / 2 * t
st.subheader(l)
