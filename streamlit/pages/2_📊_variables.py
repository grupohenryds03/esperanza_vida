import streamlit as st
import pandas as pd
import missingno as msno
import plotly.express as px
import plotly.graph_objs as go

st.set_page_config(
    page_title="Multipage App",
    page_icon="📊",
)

st.title('Selected Variables')
st.write('***')

'''##### We select 17 indicators that can help explain the relationship of the economy, education and health with life expectancy at birth.'''
'''##### To make this selection we did our own research based on sources like these:'''

st.write(1, '-  https://rstudio-pubs-static.s3.amazonaws.com/180554_a412caa868c24939a873ca679d54bbde.html')
st.write(2, '-  https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/undesa_pd_2022_wpp_key-messages.pdf')
st.write(3, '-  https://www.kaggle.com/search?q=life+expectancy')
st.write(4, '-  https://www.kaggle.com/code/nilaychauhan/etl-pipelines-tutorial-world-bank-datasets')
st.write(5, '-  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6650812/')
st.write('***')

st.subheader('*Socioeconomic Variables*')
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
columnas = ['Id_Country','Year', 'Id_Indicator', 'Value', 'Continent','Id_Income']
valores1 = [40100,40100,40100,28006,40100,40100]
valores2 = [18278,18278,18278,17664,18278,18278]
valores3 = [18278,18278,18278,18278,18278,18278]
df = pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/Hechos.csv')

st.write('***')
'''# Variable selection process'''
'''##### We obtained 38 indicators from the World Bank and the World Health Organization.'''
st.write(df.head())
'''##### With all these indicators in our dataset we find a large proportion of missing data in them: 30.16%'''
trace  = go.Bar(
                x=columnas,
                y=valores1,
                showlegend = False
                                    )

layout = go.Layout(                                    
                    xaxis_title='Columns',
                    yaxis_title='Number of records'
                                                            )
data = [trace]
fig = go.Figure(data=data,layout = layout)
st.plotly_chart(fig)
'''##### We decided to eliminate those indicators that had more than 20% of missing data. Taking that percentage to eliminate as few as possible.'''
'''##### Once that is done we are left with 17 indicators with a percentage of missing data from the 3.36%'''
trace  = go.Bar(
                x=columnas,
                y=valores2,
                showlegend = False
                                    )

layout = go.Layout(                                    
                    xaxis_title='Columns',
                    yaxis_title='Number of records'
                                                            )
data = [trace]
fig = go.Figure(data=data,layout = layout)
st.plotly_chart(fig)
'''##### With a reasonable amount of missing data we use the KNNImputer ML algorithm to properly replace the missing data.'''
trace  = go.Bar(
                x=columnas,
                y=valores3,
                showlegend = False
                                    )

layout = go.Layout(                                    
                    xaxis_title='Columns',
                    yaxis_title='Number of records'
                                                            )
data = [trace]
fig = go.Figure(data=data,layout = layout)
st.plotly_chart(fig)