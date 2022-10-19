import streamlit as st

st.title("RUMUS TRAPESIUM")

st.header("===KELILING===")
a = st.number_input("Masukan Nilai Alas A")
b = st.number_input("Masukan Nilai Alas B") 
c = st.number_input("Masukan Nilai Alas C")
d = st.number_input("Masukan Nilai Alas D")
k = a + b + c + d
st.subheader(k)
#alsa = st.number_input("Masukan Nilai Alas A")
#alsb = st.number_input("Masukan Nilai Alas B")
#t = st.number_input("Masukan Nilai Tinggi")
#l = alsa + alsb * t
#l1 = l * 1 / 2 #14^2
#st.subheader(l1)
