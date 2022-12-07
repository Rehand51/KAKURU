import streamlit as st

st.title("ROTASI")
x = st.number_input("Masukan Nilai x")
y = st.number_input("Masukan Nilai y")
rotasi = st.selectbox(
    'Masukan jenis Rotasi',
    ('(+90/-270)', '(-90/+270)', '(180)'
    ))
if (+90/-270):
    x1 = (-y)
    y1 = (x)
    st.write('sumbu x:',x1,'\n sumbu y:', y1)
else:
    x2 = (y)
    y2 = (-x)
    st.write('sumbu x:',x2,'sumbu y:', y2)
    x3 = (-x)
    y3 = (-y)
    st.write('sumbu x:',x3,'sumbu y:', y3)