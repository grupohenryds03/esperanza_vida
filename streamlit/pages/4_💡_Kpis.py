import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Multipage App",
    page_icon="💡",
)

st.title('Kpis')

lista_Kpi =['Kpi_1','Kpi_2','Kpi_3','Kpi_4']
'''
# PROBANDO SI FUNCIONA 1
'''

'''
## PROBANDO SI FUNCIONA 2
'''

'''
### PROBANDO SI FUNCIONA 3
'''

eleccion = st.selectbox(
    'Seleccionar KPI',
    (lista_Kpi))

if eleccion=='Kpi_1':
    a1,a2=st.columns(2)
    with a1:
        st.subheader("Objetivo")
        '''Objetivo Kpi 1'''
    with a2:
        st.subheader("Hipotesis")
        '''Hipotesis Kpi 1'''
else:
    st.write(eleccion)



st.write('***')


st.write('Se seleccionaron 4 Kpis.')
st.write('Utilizando las siguientes variables:')
st.write(1, '-  var 1')
st.write(2, '-  var 2')
st.write(3, '-  var 3')
st.write(4, '-  var 4')
st.write(5, '-  var 5')
st.write('***')

