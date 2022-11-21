import streamlit as st

st.title("SISTEM PERSAMAAN LINEAR DUA VARIABEL")
st.subheader("Persamaan 1: ax+by=c")
a = st.number_input("Masukan Nilai Variabel a")
b = st.number_input("Masukan Nilai Variabel b")
c = st.number_input("Masukan Nilai Variabel c")
st.subheader("Persamaan 2: px+qy=r")
p = st.number_input("Masukan Nilai Variabel p")
q = st.number_input("Masukan Nilai Variabel q")
r = st.number_input("Masukan Nilai Variabel r")
if a*q-b*p == 0:
    st.write("Belum Di Masukin Nilai")
else:
    x = (c*q-r*b)/(a*q-p*b)
    y = (1/b)*(c-a*x)
    st.write("Solusi sistem persamaan linear dua variabel adalah\nSumbu x : ",x,"\nSumbu y : ",y)
st.caption("Note: AI KAKURU akan mencari variabel x dengan metode eliminasi lalu mencari variabel y dengan metode subtitusi")