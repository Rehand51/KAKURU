import streamlit as st

st.title("RUMUS TRAPESIUM")
st.header("===LUAS===")
alsa = 6 #st.number_input("Masukan Nilai Alas A")
alsb = 8 #st.number_input("Masukan Nilai Alas B")
t =  3 #st.number_input("Masukan Nilai Tinggi")
l = alsa + alsb * t * 1 / 2 # 25 / 10
st.subheader(l)
