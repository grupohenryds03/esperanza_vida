import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Multipage App",
    page_icon="💡",
)

#st.title('Kpis')

lista_Kpi =['Mortalidad Infantil','Inversión Publica en Salud','Mortalidad Materna','Ingresos Per Capita']
'''
# KPIs
'''

st.write('***')
st.write('''Para el diseño de estos KPI, se eligieron 4 variables que segun diferentes estudios realizados tienen influencia
directa sobre la evolucion de la Esperanza de Vida (EV) de la poblacion de un pais.
Ademas, se diferenció segun el nivel de desarrollo de un pais, para observar si esto influye de diferente
forma en los efectos de las variables sobre la EV de cada pais.''')
st.write('***')

eleccion = st.selectbox(
    'Seleccionar KPI',
    (lista_Kpi))

if eleccion=='Mortalidad Infantil':
    a1,a2=st.columns(2)
    with a1:
        st.subheader("Objetivo")
        '''Se espera que la tasa de mortalidad menores de 5 años (por cada 1000 nacidos vivos), 
            disminuya 10% anual en los próximos 5 años para los países de la muestra manteniéndose 
            todo los demás constante.'''
    with a2:
        st.subheader("Hipotesis")
        '''Se presenta como Hipótesis que la Esperanza de Vida al nacer en los países Sub-desarrollados,
             aumentara como mínimo un 1% anual y en el caso de los países Desarrollados no llegara
            a aumentar un 1% anual. Esto por efecto de la mejora en la tasa de mortalidad infantil'''
elif eleccion=='Inversión Publica en Salud':
    a1,a2=st.columns(2)
    with a1:
        st.subheader("Objetivo")
        '''Se espera que los gobiernos de los países de la muestra aumenten el gasto público en Salud 
            un 10% anual de 5 años manteniéndose todo los demás constante.'''
    with a2:
        st.subheader("Hipotesis")
        '''Se presenta como Hipótesis que la variación promedio anual de la Esperanza de Vida al nacer 
            en los países sub-desarrollados de la muestra, aumente como mínimo el doble de la variación 
            promedio anual en los países desarrollados.'''
elif eleccion=='Mortalidad Materna':
    a1,a2=st.columns(2)
    with a1:
        st.subheader("Objetivo")
        ''' Se espera que la tasa de mortalidad materna (por cada 100.000 nacidos vivos), disminuya 10% 
            anual en los próximos 5 años para los países de la muestra manteniéndose todo los demás 
            constante'''
    with a2:
        st.subheader("Hipotesis")
        '''Se presenta como Hipótesis que la variación promedio de la esperanza de vida del total de 
            paises de la muestra aumentara como mínimo un 0.5% anual por los próximos 5 años.'''
elif eleccion=='Ingresos Per Capita':
    a1,a2=st.columns(2)
    with a1:
        st.subheader("Objetivo")
        '''Se espera que los ingresos per cápita (PBI per cápita (constante U$S 2015)), aumente en 
            promedio un 10% anual por los próximos 5 años en los paises de la muestra.'''
    with a2:
        st.subheader("Hipotesis")
        '''Se presenta como Hipótesis que este efecto positivo sobre los ingresos per cápita de la 
            población, generara un efecto positivo en la esperanza de vida, que se presentara como un 
            aumento promedio anual mínimo del 1%.'''



