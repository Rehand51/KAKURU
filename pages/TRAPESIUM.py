import streamlit as st

st.title("RUMUS TRAPESIUM")
st.header("===LUAS===")
alsa = st.number_input("Masukan Nilai Alas A")
alsb = st.number_input("Masukan Nilai Alas B")
t = st.number_input("Masukan Nilai Tinggi")
l = alsa + alsb * t
l1 = l * 1 / 2
st.subheader(l1)
