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
with a2:
    st.subheader("José Toledo")
    'toledojm@outlook.com'
with a3:
    '''### Linkedin'''
    'https://www.linkedin.com/in

#Pablo Poletti
b1,b2,b3=st.columns(3)
with b1:
    st.image('https://github.com/grupohenryds03/esperanza_vida/raw/main/imagenes/Pablo_photo_v.jpeg', width=100)
with b2:
    st.subheader("Pablo Poletti")
    'lic.poletti@gmail.com'
with b3:
    '''### Linkedin'''
    'https://www.linkedin.com/in'

#Rodrigo Alvarez Ruiz
c1,c2,c3=st.columns(3)
with c1:
    st.image('https://github.com/grupohenryds03/esperanza_vida/raw/main/imagenes/Rodrigo_photo_v.jpeg', width=100)
with c2:
    st.subheader("Rodrigo Álvarez Ruiz")
    'Rodrigorear94@gmail.com'
with c3:
    '''### Linkedin'''
    'https://www.linkedin.com/in'

#Jhovany Lara
d1,d2,d3=st.columns(3)
with d1:
    st.image('https://github.com/grupohenryds03/esperanza_vida/raw/main/imagenes/Jhovany_photo_v.jpeg', width=100)
with d2:
    st.subheader('Jhovany Lara')
    'jhovanylara@hotmail.com'
with d3:
    '''### Linkedin'''
    'https://www.linkedin.com/in/jhovany-lara-ds/'