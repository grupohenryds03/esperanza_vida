# streamlit_app.py

import streamlit as st
import snowflake.connector
import pandas as pd
from PIL import Image
import plotly.express as px
import plotly.graph_objs as go


st.set_page_config(
    page_title="Homepage", layout="wide",
    page_icon="👋",
)


page_style = """
            <style>
            [data-testid="stSidebar"]{
            background-image: url("https://github.com/grupohenryds03/esperanza_vida/blob/main/imagenes/life6.jpg?raw=true");
            background-size: cover;
            background-position: right;
            }
            </style>
            """
st.markdown(page_style, unsafe_allow_html=True)

col1,col2,col3=st.columns(3)
with col2:
    st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/LDlogo.png', width=200)


st.title("LIFE EXPECTANCY ANALYSIS")

st.header("Life expectancy differs depending on the birth place ")
'''
According to data from the World Health Organization (WHO), on a global scale, the life expectancy of children
born in 2015 was 71.4 years (73.8 years for girls and 69.1 for boys), but the expectations for
each child in particular depend on the place of birth.

Notes that *newborns* in high-income countries have an average life expectancy equal to or greater than 80 years,
while *newborns* in countries in sub-Saharan Africa have a life expectancy of less than 60 years.

Japanese women, whose average lifespan is 86.8 years, are the longest. In the case of men,
it is in Switzerland where they live the longest, with an average of 81.3 years. The population of Sierra Leone has the lowest life expectancy
worldwide for both sexes: 50.8 years for women and 49.3 years for men.
'''
st.subheader("Which factors influence Life Expectancy (LE)?")

'''
The largest increase in LE was recorded in the African Region, where the
life expectancy increased by 9.4 years, until it reached 60 years, due to improvements in
child survival, progress in combating malaria and expanding access to
antiretrovirals for the treatment of AIDS.

Although in the most developed countries it has been seen that LE depends on other factors, such as tobacco consumption,
overweight in children under 5 years, air pollution. So it is a multifactorial issue that depends on the economy of each country.

Studies by different entities show that life expectancy at birth comes in
increase year after year. Different factors are key to deciphering the reason for the
increased life expectancy at birth.
From the industrial revolution onwards it was shown that not only biological factors affect the EV, 
but also socioeconomic factors are studied in relevance for the construction of this index.
'''

st.write('***')

a1,a2,a3=st.columns(3)
with a1:
    a1.metric('', '1.1 billion','people smoke tobacco')
with a2:
    a2.metric('','156 million','children -5 age are stunted')
with a3:
    a3.metric('','42 million','children -5 age are overweight')
st.write('***')
b1,b2,b3=st.columns(3)
with b1:
    b1.metric('','1.8 billion','people drink contaminated water')
with b2:
    b2.metric('','946 million','people defecate in open air')
with b3:
    b3.metric('','3.1 billion','cooking with polluting fuels')
   

st.write('***')
st.image('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/imagenes/paso_vida.jpeg')
c1,c2,c3=st.columns(3)
with c2:
    st.header("Goals")

'''
- Provide advice to public and private entities about the most relevant possible socioeconomic and health factors in the incidence of life expectancy at birth.

- Help the different regions or countries to implement state policies, providing them with the possible causes that are affecting life expectancy at birth.

- Contribute to achieve a better quality of life based on a change in the indicators by region.
'''

d1,d2=st.columns(2)
with d1:
    st.subheader("In scope")
    '''Loadings of different datasets with records from the year 1960 in order to transform this data into valuable information that allows queries on life expectancy at birth in a specific period of time or make predictions through machine learning algorithms.'''
with d2:
    st.subheader("Out of scope")
    '''The analysis and predictions provided will not be prior to the year 1960.
    The consultations will not include biological factors.
    The data load will be in batches in different formats.'''

st.write('***')

h1,h2,h3=st.columns(3)
with h2:
    st.header("Metodology")
'''
The work is based on a quantitative approach which will help to establish relations between quantitative variables from socioeconomic and health indicators, such as GDP per capita,
public spending on education, under-5 mortality rate, % of rural population, % of poverty, % of total
health spending etc. which can help to generate a context of the possible influence of each variable in
life expectancy at birth.

We have worked on the development of a ML algorithm that allows us to generate future predictions using
expectations of these indicators.'''

