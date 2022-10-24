import streamlit as st

st.set_page_config(
    page_title="Multipage App",
    page_icon="✉",
)

st.title("Contact:")

a1,a2=st.columns(2)
with a1:
    st.subheader("José Toledo")
with a2:
    'toledojm@outlook.com'
b1,b2=st.columns(2)
with b1:
    st.subheader("Pablo Poletti")
with b2:
    'lic.poletti@gmail.com'
c1,c2=st.columns(2)
with c1:
    st.subheader("Rodrigo Álvarez Ruiz")
with c2:
    'Rodrigorear94@gmail.com'
d1,d2=st.columns(2)
with d1:
    st.subheader("Jhovany Lara")
with d2:
    'jhovanylara@hotmail.com'