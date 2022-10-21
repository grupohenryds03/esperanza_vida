import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Multipage App",
    page_icon="📊",
)

st.title('Variables Seleccionadas')
st.write('***')


st.write('Se seleccionaron 17 indicadores que pueden ayudar a explicar la relación de la economía, la educación y la salud con la esperanza de vida al nacer.')
st.write('Para hacer esta selección hicimos investigaciones propias basandonos en fuentes como estas:')
st.write(1, '-  https://rstudio-pubs-static.s3.amazonaws.com/180554_a412caa868c24939a873ca679d54bbde.html')
st.write(2, '-  https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/undesa_pd_2022_wpp_key-messages.pdf')
st.write(3, '-  https://www.kaggle.com/search?q=life+expectancy')
st.write(4, '-  https://www.kaggle.com/code/nilaychauhan/etl-pipelines-tutorial-world-bank-datasets')
st.write(5, '-  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6650812/')
st.write('***')

st.subheader('*Variables Socioeconómicas*')
'- Trade in services (% of GDP) - ID:38'
'- CO2 emissions (kt) - ID:2'
'- Population growth (annual %) - ID:3'
'- GPD per capita (constant 2015 US$) - ID:31'
'- Total unemployment (% total population) - ID:25'
'- Life expectancy at birth, men (years) - ID:26'
'- Life expectancy at birth, women (years) - ID:27'
'- Life expectancy at birth, total (years) - ID:28'
'- Rural population (% of total population) - ID:33'
'- Urban population (% total population) - ID:34'

st.subheader('*Variables de Salud*')
'- Hepatitis B (HepB3) inmmunization coverage among 1-year-olds % - ID:7'
'- Mortality rate, under-5 (per 1000 live births) - ID:11'
'- Inmmunization, DPT (% of children ages 12-23 months) - ID:8'
'- Inmmunization, measles (% of children ages 12-23 months) -ID:9'
'- Polio (Pol3) immunization covergae among 1-year-olds (%) - ID:14'
'- Mortality rate, female adults (per 1000 adults) - ID:20'
'- Death rate, male adults (per 1000 adults) - ID:19'

st.write('***')
'''# Proceso de selección de variables'''
'''##Obtuvimos 38 indicadores del Banco Mundial y de la Organización Mundial de la Salud.'''
'''##Con todos estos indicadores en nuestro dataset nos encontramos con una gran proporción de datos faltantes en ellos: 30.16%'''
'''##Decidimos eliminar aquellos indicadores que contaban con mas del 20% de datos faltantes. Tomando ese porcentaje para eliminar los menos posibles.'''
'''##Una vez hecho eso nos quedamos con 17 indicadores con un porcentaje de datos faltantes del 3.36%'''
'''##Con una cantidad razonable de datos faltantes utilizamos el algoritmo de ML KNNImputer para reemplar adecuadamente los datos faltantes.'''