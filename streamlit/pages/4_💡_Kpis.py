import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Multipage App",
    page_icon="💡",
)

st.title('Kpis')

lista_Kpi =['Mortalidad Infantil','Inversión Publica en Salud','Mortalidad Materna','Ingresos Per Capita']
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

if eleccion=='Mortalidad Infantil':
    a1,a2=st.columns(2)
    with a1:
        st.subheader("Objetivo")
        '''Se espera que los gobiernos de los países de la muestra aumenten el gasto público 
            en Salud un 10% anual de 5 años manteniéndose todo los demás constante.'''
    with a2:
        st.subheader("Hipotesis")
        '''Se presenta como Hipótesis que la Esperanza de Vida al nacer en los países Sub-desarrollados,
             aumentara como mínimo un 1% anual y en el caso de los países Desarrollados no llegara
            a aumentar un 1% anual. Esto por efecto de la mejora en la tasa de mortalidad infantil'''
elif eleccion=='Inversión Publica en Salud':
    a1,a2=st.columns(2)
    with a1:
        st.subheader("Objetivo")
        '''Objetivo Kpi 2'''
    with a2:
        st.subheader("Hipotesis")
        '''Hipotesis Kpi 2'''
elif eleccion=='Mortalidad Materna':
    a1,a2=st.columns(2)
    with a1:
        st.subheader("Objetivo")
        '''Objetivo Kpi 3'''
    with a2:
        st.subheader("Hipotesis")
        '''Hipotesis Kpi 3'''
elif eleccion=='Ingresos Per Capita':
    a1,a2=st.columns(2)
    with a1:
        st.subheader("Objetivo")
        '''Objetivo Kpi 4'''
    with a2:
        st.subheader("Hipotesis")
        '''Hipotesis Kpi 4'''


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

