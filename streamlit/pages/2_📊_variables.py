import streamlit as st
import pandas as pd
import missingno as msno
import plotly.express as px
import plotly.graph_objs as go
import snowflake.connector
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="Variables",
    page_icon="📊",
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

@st.experimental_singleton
def init_connection():
    return snowflake.connector.connect(
        user=st.secrets.snowflake.user,
    password=st.secrets.snowflake.password,
    account=st.secrets.snowflake.account,
    warehouse=st.secrets.snowflake.warehouse,
    database=st.secrets.snowflake.database, client_session_keep_alive=True
    )

conn = init_connection()

@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetch_pandas_all()


st.title('Selected Variables')

'''##### We selected 17 indicators that can help explain the relationship of the economy, education and health care with life expectancy at birth.'''
'''##### To make this selection we did our own research based on sources like these:'''

f1,f2=st.columns(2)
with f1:
    url = "https://rstudio-pubs-static.s3.amazonaws.com/180554_a412caa868c24939a873ca679d54bbde.html"
    st.write("Ian Vleeming y Ricardo Valladares paper [link](%s)" % url)

    url = 'https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/undesa_pd_2022_wpp_key-messages.pdf'
    st.write("World Population Prospects 2022 - United Nations [link](%s)" % url)

    url = 'https://www.kaggle.com/search?q=life+expectancy'
    st.write("Kaggle studies reserch [link](%s)" % url)
with f2:
    url = 'https://www.kaggle.com/code/nilaychauhan/etl-pipelines-tutorial-world-bank-datasets'
    st.write("Kaggle ETL process [link](%s)" % url)

    url = 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6650812/'
    st.write("Analysis of Life Expectancy at Birth paper - National Library of Medicine from Spain [link](%s)" % url)

    url = 'https://ruc.udc.es/dspace/bitstream/handle/2183/16409/RodriguezRodriguez_David_TFG_2015.pdf?sequence=2'
    st.write("David Rodríguez Rodríguez paper - Económic Coruña University[link](%s)" % url)




st.write('***')
st.subheader('*Socioeconomic Variables*')

g1,g2=st.columns(2)
with g1:
    '- Trade in services (% of GDP)'
    '- CO2 emissions (kt)'
    '- Population growth (annual %)'
    '- GPD per capita (constant 2015 US$)'
    '- Total unemployment (% total population)'
with g2:
    '- Life expectancy at birth, men (years)'
    '- Life expectancy at birth, women (years)'
    '- Life expectancy at birth, total (years)'
    '- Rural population (% of total population)'
    '- Urban population (% total population)'

st.write('***')
st.subheader('*Health Variables*')

c1,c2=st.columns(2)
with c1:
    '- Hepatitis B (HepB3) inmmunization coverage among 1-year-olds % - ID:7'
    '- Mortality rate, under-5 (per 1000 live births) - ID:11'
    '- Inmmunization, DPT (% of children ages 12-23 months) - ID:8'
with c2:
    '- Inmmunization, measles (% of children ages 12-23 months) -ID:9'
    '- Polio (Pol3) immunization covergae among 1-year-olds (%) - ID:14'
    '- Mortality rate, female adults (per 1000 adults) - ID:20'
    '- Death rate, male adults (per 1000 adults) - ID:19'




columnas = ['Id_Country','Year', 'Id_Indicator', 'Value', 'Continent','Id_Income']
valores1 = [40100,40100,40100,28006,40100,40100]
valores2 = [18278,18278,18278,17664,18278,18278]
valores3 = [18278,18278,18278,18278,18278,18278]
df = pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/Hechos.csv')
df = df.drop('Unnamed: 0', axis = 1)


st.write('***')
'''# Indicators selection process for EDA'''

tab1, tab2, tab3 , tab4= st.tabs(['Crud indicators',"Missing data","Imputer ML algorithm","Compare life expectancy relationship"])
with tab1:
    '''##### We obtained 38 indicators from the World Bank and the World Health Organization.'''
    st.dataframe(df)
    '''##### With all these indicators in our dataset we find a large proportion of missing data in them: 30.16%'''
    trace  = go.Bar(
                    x=columnas,
                    y=valores1,
                    showlegend = False,
                    marker=dict(color = valores1,colorscale='viridis'))

    layout = go.Layout(                                    
                        xaxis_title='Columns',
                        yaxis_title='Number of records')
    data = [trace]
    fig = go.Figure(data=data,layout = layout,)
    st.plotly_chart(fig,use_container_width=True)
with tab2:
    '''##### We decided to eliminate those indicators that had more than 20% of missing data. Taking that percentage to eliminate as few as possible.'''
    '''##### Once that is done we are left with 17 indicators with a percentage of missing data of the 3.36%'''
    trace  = go.Bar(
                    x=columnas,
                    y=valores2,
                    showlegend = False,
                    marker=dict(color = valores2,colorscale='viridis'))

    layout = go.Layout(                                    
                        xaxis_title='Columns',
                        yaxis_title='Number of records')
    data = [trace]
    fig = go.Figure(data=data,layout = layout)
    st.plotly_chart(fig,use_container_width=True)
with tab3:
    '''##### With a reasonable amount of missing data we use the KNNImputer ML algorithm to properly replace the missing data.'''
    trace  = go.Bar(
                    x=columnas,
                    y=valores3,
                    showlegend = False,
                    marker=dict(color = valores3,colorscale='viridis'))

    layout = go.Layout(                                    
                        xaxis_title='Columns',
                        yaxis_title='Number of records')
    data = [trace]
    fig = go.Figure(data=data,layout = layout)
    st.plotly_chart(fig,use_container_width=True)

with tab4:

    sql_ind="SELECT i.ID_INDICADOR , i.CODIGO, i.DESCRIPCION FROM INDICADOR i JOIN (SELECT DISTINCT ID_INDICADOR FROM EV) e ON e.ID_INDICADOR=i.ID_INDICADOR"
    df_ind=run_query(sql_ind) # dataframe indicadores
    sql_pais="SELECT p.ID_PAIS, p.CODIGO_PAIS, p.NOMBRE FROM PAIS p JOIN (SELECT DISTINCT ID_PAIS FROM EV) e ON e.ID_PAIS=p.ID_PAIS"
    df_pais=run_query(sql_pais) # dataframe pais

    col1,col2=st.columns(2)

    'compare life expectancy relationship bettewn diferents factor'
    with col1:
        option_pais = st.selectbox(
            'Choose country from list',
            df_pais.NOMBRE) 

    with col2:
        option_ind = st.selectbox(
                'Choose country from list',
                df_ind.DESCRIPCION) 

    sql_esp =f"""SELECT ANIO, VALOR 
                FROM EV e
                JOIN (SELECT ID_PAIS FROM PAIS WHERE NOMBRE='{option_pais}') p
                ON e.ID_PAIS=p.ID_PAIS
                WHERE ID_INDICADOR=31 AND ANIO<=2020"""
    df_esp=run_query(sql_esp) # dataframe esperanza vida

    sql_ind =f"""SELECT ANIO, VALOR 
                FROM EV e
                JOIN (SELECT ID_INDICADOR FROM INDICADOR WHERE DESCRIPCION='{option_ind}') i
                ON e.ID_INDICADOR=i.ID_INDICADOR
                JOIN (SELECT ID_PAIS FROM PAIS WHERE NOMBRE='{option_pais}') p
                ON e.ID_PAIS=p.ID_PAIS
                WHERE e.ANIO<=2020"""
    df_ind=run_query(sql_ind) # dataframe indicador elejido

    titulo_grafico=f"life expectancy (LE) relationship from {option_pais}  bettewn {option_ind}"
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=df_esp.ANIO, 
                        y=df_esp.VALOR,
                        mode='lines',
                        marker_color='#FF0000',
                        name="LE",
                        line=dict(width=2)),secondary_y=False)

    fig.add_trace(go.Scatter(x=df_ind.ANIO, 
                        y=df_ind.VALOR,#option
                        mode='lines',
                        marker_color='#00FF00',
                        name="Factor",
                        line=dict(width=2)),secondary_y=True)

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, griddash='dot', gridwidth=0.1, gridcolor='White')
    fig.update_yaxes(title_text="years", secondary_y=False)
    fig.update_yaxes(secondary_y=True)
    fig.update_layout(title=titulo_grafico)
    st.plotly_chart(fig,use_container_width=True)
