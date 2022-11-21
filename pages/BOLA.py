import streamlit as st

st.header("KELILING BOLA")
r = st.number_input("Masukan Panjang Jari - jari")
k = 2 * 22/7 * r
kk = 2 * 3.14 * r
st.write(k, " & ", kk)

st.header("LUAS BOLA")
l = 4 * 22/7 * r**2
ll = 4 * 3.14 * r**2
st.write(l, " & ", ll)

st.caption("Kiri menggunakan 22/7, kanan menggunakan 3.14")