import streamlit as st

st.title("SEGITIGA SIKU-SIKU")
st.header("===KELILING===")
a = st.number_input("Masukan Panjang sisi 1")
b = st.number_input("Masukan Panjang sisi 2")
c = st.number_input("Masukan Panjang sisi 3")
k = a + b + c
st.subheader(k)
st.header("LUAS")
alas = st.number_input("Masukan panjang Alas")
tinggi = st.number_input("Masukan Tinggi")
l = alas * tinggi * 1 / 2
st.subheader(l)