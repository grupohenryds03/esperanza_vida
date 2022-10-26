import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="✉",
)

st.title("Contact:")
#José Toledo
a1,a2,a3=st.columns(3)
with a1:
    st.image('https://github.com/grupohenryds03/esperanza_vida/raw/main/imagenes/Jose_photo_v.jpeg', width=100)
with a1:
    '''##### José Toledo'''
with a2:
    'toledojm@outlook.com'

#Pablo Poletti
b1,b2,b3=st.columns(3)
with b1:
    st.image('https://github.com/grupohenryds03/esperanza_vida/raw/main/imagenes/Pablo_photo_v.jpeg', width=100)
with b2:
    st.subheader("Pablo Poletti")
with b3:
    'lic.poletti@gmail.com'

#Rodrigo Alvarez Ruiz
c1,c2,c3=st.columns(3)
with c1:
    st.image('https://github.com/grupohenryds03/esperanza_vida/raw/main/imagenes/Rodrigo_photo_v.jpeg', width=100)
with c2:
    st.subheader("Rodrigo Álvarez Ruiz")
with c3:
    'Rodrigorear94@gmail.com'

#Jhovany Lara
d1,d2,d3=st.columns(3)
with d1:
    st.image('https://github.com/grupohenryds03/esperanza_vida/raw/main/imagenes/Jhovany_photo_v.jpeg', width=100)
with d2:
    '''### Jhovany Lara'''
    'jhovanylara@hotmail.com'
with d3:
    'jhovanylara@hotmail.com'