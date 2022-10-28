import streamlit as st

st.set_page_config(
    page_title="Contact",
    page_icon="✉",
)

page_style = """
            <style>
            
            [data-testid="stSidebar"]{
            background-image: url("https://github.com/grupohenryds03/esperanza_vida/blob/main/imagenes/WallpaperRocky.jpg?raw=true");
            background-size: cover;
            background-position: right;
            }
            </style>
            """
#background-Color: blue;
            
st.markdown(page_style, unsafe_allow_html=True)

st.title("Contact:")
#José Toledo
a1,a2=st.columns(2)
with a1:
    st.image('https://github.com/grupohenryds03/esperanza_vida/raw/main/imagenes/Jose_photo_v.jpeg', width=100)
with a2:
    st.subheader("José Toledo")
    'toledojm@outlook.com'
    'https://www.linkedin.com/in'

    

#Pablo Poletti
b1,b2=st.columns(2)
with b1:
    st.image('https://github.com/grupohenryds03/esperanza_vida/raw/main/imagenes/Pablo_photo_v.jpeg', width=100)
with b2:
    st.subheader("Pablo Poletti")
    'lic.poletti@gmail.com'
    'https://www.linkedin.com/in'

    


#Jhovany Lara
c1,c2=st.columns(2)
with c1:
    st.image('https://github.com/grupohenryds03/esperanza_vida/raw/main/imagenes/Jhovany_photo_v.jpeg', width=100)
with c2:
    st.subheader('Jhovany Lara')
    'jhovanylara@hotmail.com'
    'https://www.linkedin.com/in/jhovany-lara-ds/'


#Rodrigo Alvarez Ruiz
d1,d2=st.columns(2)
with d1:
    st.image('https://github.com/grupohenryds03/esperanza_vida/raw/main/imagenes/Rodrigo_photo_v.jpeg', width=100)
with d2:
    st.subheader("Rodrigo Álvarez Ruiz")
    'Rodrigorear94@gmail.com'
    'https://www.linkedin.com/in/rodrigo-alvarez-ruiz-0b2410255/'
