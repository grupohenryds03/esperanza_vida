import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="KPIs",
    page_icon="💡",
)

#st.title('Kpis')

lista_Kpi =['Mortalidad Infantil','CO2 EMISSION','RURAL POPULATION (%)','GDP PER CAPITA']
'''
# Key Performance Indicators (KPIs)
'''

st.write('***')
st.write('''
For the design of these KPIs, 4 variables were selected that, according to different studies, affect
on the evolution of Life Expectancy (LE) of the population of a country.
In addition, it was differentiated according to the level of development of a country, to see if this influences the effects of the variables on the LE of each country.''')
st.write('***')

eleccion = st.selectbox(
    'Select KPI',
    (lista_Kpi))

if eleccion=='Mortalidad Infantil':
    a1,a2=st.columns(2)
    with a1:
        st.subheader("Objetivo")
        '''Se espera que la tasa de mortalidad menores de 5 años (por cada 1000 nacidos vivos), 
            disminuya 10% anual en los próximos 5 años para los países de la muestra manteniéndose 
            todo los demás constante.'''
    with a2:
        st.subheader("Hipótesis")
        '''Se presenta como Hipótesis que la Esperanza de Vida al nacer en los países Sub-desarrollados,
             aumentara como mínimo un 1% anual y en el caso de los países Desarrollados no llegara
            a aumentar un 1% anual. Esto por efecto de la mejora en la tasa de mortalidad infantil'''

    df = pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/KPI_Mort-Inf.csv')
    
    pais_desarrollo=[]
    ev_2020_average=[]
    ev_2025_average=[]
    ev_2025_hypo_average=[]

    pais_desarrollo.append('Developed Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] ==0)].mean()),4))

    pais_desarrollo.append('NOT Developed Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] !=0)].mean()),4))
    resultados = pd.DataFrame(pais_desarrollo, columns=['DEVELOPED LEVEL'])
    resultados1 = pd.DataFrame(ev_2020_average, columns=['LE 2020 AVERAGE'])
    resultados2 = pd.DataFrame(ev_2025_average, columns=['LE FORECAST 2025 AVERAGE'])
    resultados3 = pd.DataFrame(ev_2025_hypo_average, columns=['LE HYPOTETICAL 2025 AVERAGE'])
    #resultados4 = pd.DataFrame(modelo_mejora, columns=['Modelo_Predictivo'])
    resultado = pd.concat([resultados,resultados1,resultados2,resultados3],axis=1)#,resultados4
    resultado['DIFFERENCE (%)']=(resultado['LE HYPOTETICAL 2025 AVERAGE']/resultado['LE FORECAST 2025 AVERAGE'])-1

    st.table(resultado)


    
    df.drop('Unnamed: 0',inplace=True, axis=1)
    
    st.table(df)


elif eleccion=='CO2 EMISSION':
    a1,a2=st.columns(2)
    with a1:
        st.subheader("Objetivo")
        '''Se espera que los gobiernos de los países de la muestra aumenten el gasto público en Salud 
            un 10% anual de 5 años manteniéndose todo los demás constante.'''
    with a2:
        st.subheader("Hipótesis")
        '''Se presenta como Hipótesis que la variación promedio anual de la Esperanza de Vida al nacer 
            en los países sub-desarrollados de la muestra, aumente como mínimo el doble de la variación 
            promedio anual en los países desarrollados.'''

    df = pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/KPI_CO2.csv')
    
    pais_desarrollo=[]
    ev_2020_average=[]
    ev_2025_average=[]
    ev_2025_hypo_average=[]

    pais_desarrollo.append('Developed Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] ==0)].mean()),4))

    pais_desarrollo.append('NOT Developed Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] !=0)].mean()),4))
    resultados = pd.DataFrame(pais_desarrollo, columns=['DEVELOPED LEVEL'])
    resultados1 = pd.DataFrame(ev_2020_average, columns=['LE 2020 AVERAGE'])
    resultados2 = pd.DataFrame(ev_2025_average, columns=['LE FORECAST 2025 AVERAGE'])
    resultados3 = pd.DataFrame(ev_2025_hypo_average, columns=['LE HYPOTETICAL 2025 AVERAGE'])
    #resultados4 = pd.DataFrame(modelo_mejora, columns=['Modelo_Predictivo'])
    resultado = pd.concat([resultados,resultados1,resultados2,resultados3],axis=1)#,resultados4
    resultado['DIFFERENCE (%)']=(resultado['LE HYPOTETICAL 2025 AVERAGE']/resultado['LE FORECAST 2025 AVERAGE'])-1

    st.table(resultado)


    
    df.drop('Unnamed: 0',inplace=True, axis=1)
    
    st.table(df)



elif eleccion=='RURAL POPULATION (%)':
    a1,a2=st.columns(2)
    with a1:
        st.subheader("Objetivo")
        ''' Se espera que la tasa de mortalidad materna (por cada 100.000 nacidos vivos), disminuya 10% 
            anual en los próximos 5 años para los países de la muestra manteniéndose todo los demás 
            constante'''
    with a2:
        st.subheader("Hipótesis")
        '''Se presenta como Hipótesis que la variación promedio de la esperanza de vida del total de 
            paises de la muestra aumentara como mínimo un 0.5% anual por los próximos 5 años.'''

    df = pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/KPI_RURAL.csv')
    
    pais_desarrollo=[]
    ev_2020_average=[]
    ev_2025_average=[]
    ev_2025_hypo_average=[]

    pais_desarrollo.append('Developed Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] ==0)].mean()),4))

    pais_desarrollo.append('NOT Developed Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] !=0)].mean()),4))
    resultados = pd.DataFrame(pais_desarrollo, columns=['DEVELOPED LEVEL'])
    resultados1 = pd.DataFrame(ev_2020_average, columns=['LE 2020 AVERAGE'])
    resultados2 = pd.DataFrame(ev_2025_average, columns=['LE FORECAST 2025 AVERAGE'])
    resultados3 = pd.DataFrame(ev_2025_hypo_average, columns=['LE HYPOTETICAL 2025 AVERAGE'])
    #resultados4 = pd.DataFrame(modelo_mejora, columns=['Modelo_Predictivo'])
    resultado = pd.concat([resultados,resultados1,resultados2,resultados3],axis=1)#,resultados4
    resultado['DIFFERENCE (%)']=(resultado['LE HYPOTETICAL 2025 AVERAGE']/resultado['LE FORECAST 2025 AVERAGE'])-1

    st.table(resultado)


    
    df.drop('Unnamed: 0',inplace=True, axis=1)
    
    st.table(df)


elif eleccion=='GDP PER CAPITA':
    a1,a2=st.columns(2)
    with a1:
        st.subheader("Objetivo")
        '''Se espera que los ingresos per cápita (PBI per cápita (constante U$S 2015)), aumente en 
            promedio un 10% anual por los próximos 5 años en los paises de la muestra.'''
    with a2:
        st.subheader("Hipótesis")
        '''Se presenta como Hipótesis que este efecto positivo sobre los ingresos per cápita de la 
            población, generara un efecto positivo en la esperanza de vida, que se presentara como un 
            aumento promedio anual mínimo del 1%.'''

    df = pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/KPI_GDP.csv')
    
    pais_desarrollo=[]
    ev_2020_average=[]
    ev_2025_average=[]
    ev_2025_hypo_average=[]

    pais_desarrollo.append('Developed Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] ==0)].mean()),4))

    pais_desarrollo.append('NOT Developed Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] !=0)].mean()),4))
    resultados = pd.DataFrame(pais_desarrollo, columns=['DEVELOPED LEVEL'])
    resultados1 = pd.DataFrame(ev_2020_average, columns=['LE 2020 AVERAGE'])
    resultados2 = pd.DataFrame(ev_2025_average, columns=['LE FORECAST 2025 AVERAGE'])
    resultados3 = pd.DataFrame(ev_2025_hypo_average, columns=['LE HYPOTETICAL 2025 AVERAGE'])
    #resultados4 = pd.DataFrame(modelo_mejora, columns=['Modelo_Predictivo'])
    resultado = pd.concat([resultados,resultados1,resultados2,resultados3],axis=1)#,resultados4
    resultado['DIFFERENCE (%)']=(resultado['LE HYPOTETICAL 2025 AVERAGE']/resultado['LE FORECAST 2025 AVERAGE'])-1

    st.table(resultado)


    
    df.drop('Unnamed: 0',inplace=True, axis=1)
    
    st.table(df)