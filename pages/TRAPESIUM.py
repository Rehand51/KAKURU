import streamlit as st

st.title("RUMUS TRAPESIUM")
st.header("===LUAS===")
alsa = st.number_input("Masukan Nilai Alas A")
alsb = st.number_input("Masukan Nilai Alas B")
t = st.number_input("Masukan Nilai Tinggi")
l = 2 / alsa + alsb * t
st.subheader(l)
