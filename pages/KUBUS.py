import streamlit as st

st.title("KUBUS")
st.header("KELILING")
sisi = st.number_input("Masukan Panjang Sisi:")
k = 12 * sisi
st.subheader(k)
st.header("LUAS")
l = 6 * sisi
st.subheader(l)
st.subheader("VOLUME")
v = sisi * sisi * sisi
st.subheader(v)