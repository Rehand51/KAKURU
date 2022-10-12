import streamlit as st

st.title("PERSEGI")

st.header("===KELILING===")
sisi = st.number_input("Masukan Panjang Sisi:")
keliling = sisi * sisi
st.subheader(keliling)

st.header("===LUAS===")
luas = 4 * sisi
st.subheader(luas)