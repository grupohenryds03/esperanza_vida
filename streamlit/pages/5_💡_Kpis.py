import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Kpis",
    page_icon="💡",
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


lista_Kpi =['Infant Mortality','CO2 Emission','Rural Population (%)','GDP Per Capita','Conclusions']
'''
# Analysis and Assumptions
'''

st.write('***')
st.write('''
<<<<<<< HEAD
_To carry out this study, 4 variables were selected that, according to different studies, affect the evolution of the Life Expectancy (LE) 
of the population of a country.
The objective of this analysis is to identify if an improvement of 10% per year during the next 5 years in the 4 selected variables, 
will have a greater benefit in LE in developing countries, since we assume that they have greater room for improvement in these 4 variables 
compared to developed countries._''')

=======
_To carry out this study, 4 variables were selected, according to different studies that argue they may affect the Life Expectancy (LE) evolution of a country's population.
The objective of this analysis is to identify if a 10% per year improvement in the next 5 years will have a greater benefit on LE in developing countries, 
since we assume that they have greater margin to improve in these 4 variables compared to the developed countries._''')
>>>>>>> df9615f09166b2861930d6ccd7f0c6e4c58f09e1

st.write('''
_To separate between developed and undeveloped countries, the World Bank Income Index was used. Developed countries were considered those with a high income index
and the rest as undeveloped countries._''')
st.write('***')

st.write('''
_In order to carry out this analysis we are going to project the LE until 2025 in 2 ways, the first will consist of making 
the prediction using the 4 variables selected as exogenous variables (VE) and their respective "natural" predictions until 2025 
and then the LE will be projected using the EVs, but with their “Hypothetical” predictions.
Finally, both results will be compared to obtain conclusions._''')
st.write('***')

eleccion = st.selectbox(
    'Select:',
    (lista_Kpi))

if eleccion=='Infant Mortality':
    
    st.subheader("Results")
    st.write('***')
    st.write('''
     _In the case of the exogenous variable (VE) Infant Mortality, the results of the "Hypothetical" vs. "Natural" projections 
     show that developing countries would obtain a slight improvement in LE compared to developed countries._''')
    st.write('***')


    df = pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/KPI_Mort-Inf.csv')
    
    pais_desarrollo=[]
    ev_2020_average=[]
    ev_2025_average=[]
    ev_2025_hypo_average=[]

    pais_desarrollo.append('Developed Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] ==0)].mean()),4))

    pais_desarrollo.append('Developing  Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] !=0)].mean()),4))
    resultados = pd.DataFrame(pais_desarrollo, columns=['Developed Level'])
    resultados1 = pd.DataFrame(ev_2020_average, columns=['LE 2020 Average'])
    resultados2 = pd.DataFrame(ev_2025_average, columns=['LE Forecast 2025 Average'])
    resultados3 = pd.DataFrame(ev_2025_hypo_average, columns=['LE Forecast Hypot. 2025 Average'])
    #resultados4 = pd.DataFrame(modelo_mejora, columns=['Modelo_Predictivo'])
    resultadoa = pd.concat([resultados,resultados1,resultados2,resultados3],axis=1)#,resultados4
    resultadoa['Difference (%)']=(resultadoa['LE Forecast Hypot. 2025 Average']/resultadoa['LE Forecast 2025 Average'])-1

    resultado1=resultadoa['Difference (%)']
    resultado1=pd.DataFrame(resultado1)
    resultado1=resultado1.rename(columns={'Difference (%)':'Infant Mortality'})
    resultado1=pd.concat([resultados,resultado1],axis=1)

 
    st.table(resultadoa)



    df.drop('Unnamed: 0',inplace=True, axis=1)
    df=df.rename(columns={'Pais':'Country','EV_2020':'LE 2020','EV_2025':'LE 2025','EV_2025_Mejora':'LE 2025 Hypotetical'})
    
    agree = st.checkbox('Show Forecast Table')

    if agree:

        st.table(df)


elif eleccion=='CO2 Emission':

    st.subheader("Results")
    st.write('***')
    st.write('''
     _In the case of the exogenous variable (VE) CO2 Emission, the results of the "Hypothetical" vs. "Natural" projections 
     show that developed countries would obtain a slight improvement in LE compared to developeding countries._''')
    st.write('***')

    df = pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/KPI_CO2.csv')
    
    pais_desarrollo=[]
    ev_2020_average=[]
    ev_2025_average=[]
    ev_2025_hypo_average=[]

    pais_desarrollo.append('Developed Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] ==0)].mean()),4))

    pais_desarrollo.append('Developingd Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] !=0)].mean()),4))
    resultados = pd.DataFrame(pais_desarrollo, columns=['Developed Level'])
    resultados1 = pd.DataFrame(ev_2020_average, columns=['LE 2020 Average'])
    resultados2 = pd.DataFrame(ev_2025_average, columns=['LE Forecast 2025 Average'])
    resultados3 = pd.DataFrame(ev_2025_hypo_average, columns=['LE Forecast Hypot. 2025 Average'])
    #resultados4 = pd.DataFrame(modelo_mejora, columns=['Modelo_Predictivo'])
    resultadob = pd.concat([resultados,resultados1,resultados2,resultados3],axis=1)#,resultados4
    resultadob['Difference (%)']=(resultadob['LE Forecast Hypot. 2025 Average']/resultadob['LE Forecast 2025 Average'])-1

    resultado2=resultadob['Difference (%)']
    resultado2=pd.DataFrame(resultado2)
    resultado2=resultado2.rename(columns={'Difference (%)':'CO2 Emission'})
    

    st.table(resultadob)


    
    df.drop('Unnamed: 0',inplace=True, axis=1)
    df=df.rename(columns={'Pais':'Country','EV_2020':'LE 2020','EV_2025':'LE 2025','EV_2025_Mejora':'LE 2025 Hypotetical'})

    agree = st.checkbox('Show Forecast Table')

    if agree:

        st.table(df)



elif eleccion=='Rural Population (%)':

    st.subheader("Results")
    st.write('***')
    st.write('''
     _In the case of the exogenous variable (VE) Rural Population (%), the results of the "Hypothetical" vs. "Natural" projections 
     show that developing countries would obtain an improvement in LE compared to developed countries._''')
    st.write('***')

    df = pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/KPI_RURAL.csv')
    
    pais_desarrollo=[]
    ev_2020_average=[]
    ev_2025_average=[]
    ev_2025_hypo_average=[]

    pais_desarrollo.append('Developed Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] ==0)].mean()),4))

    pais_desarrollo.append('Developing Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] !=0)].mean()),4))
    resultados = pd.DataFrame(pais_desarrollo, columns=['Developed Level'])
    resultados1 = pd.DataFrame(ev_2020_average, columns=['LE 2020 Average'])
    resultados2 = pd.DataFrame(ev_2025_average, columns=['LE Forecast 2025 Average'])
    resultados3 = pd.DataFrame(ev_2025_hypo_average, columns=['LE Forecast Hypot. 2025 Average'])
    #resultados4 = pd.DataFrame(modelo_mejora, columns=['Modelo_Predictivo'])
    resultadoc = pd.concat([resultados,resultados1,resultados2,resultados3],axis=1)#,resultados4
    resultadoc['Difference (%)']=(resultadoc['LE Forecast Hypot. 2025 Average']/resultadoc['LE Forecast 2025 Average'])-1

    resultado3=resultadoc['Difference (%)']
    resultado3=pd.DataFrame(resultado3)
    resultado3=resultado3.rename(columns={'Difference (%)':'Rural Population (%)'})


    st.table(resultadoc)


    
    df.drop('Unnamed: 0',inplace=True, axis=1)
    df=df.rename(columns={'Pais':'Country','EV_2020':'LE 2020','EV_2025':'LE 2025','EV_2025_Mejora':'LE 2025 Hypotetical'})

    agree = st.checkbox('Show Forecast Table')

    if agree:
        st.table(df)


elif eleccion=='GDP Per Capita':

    st.subheader("Results")
    st.write('***')
    st.write('''
     _In the case of the exogenous variable (VE) GDP Per Capita, the results of the "Hypothetical" vs. "Natural" projections 
     show that developing countries would obtain an improvement in LE compared to developed countries._''')
    st.write('***')

    df = pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/KPI_GDP.csv')
    
    pais_desarrollo=[]
    ev_2020_average=[]
    ev_2025_average=[]
    ev_2025_hypo_average=[]

    pais_desarrollo.append('Developed Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] ==0)].mean()),4))

    pais_desarrollo.append('Developing Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] !=0)].mean()),4))
    resultados = pd.DataFrame(pais_desarrollo, columns=['Developed Level'])
    resultados1 = pd.DataFrame(ev_2020_average, columns=['LE 2020 Average'])
    resultados2 = pd.DataFrame(ev_2025_average, columns=['LE Forecast 2025 Average'])
    resultados3 = pd.DataFrame(ev_2025_hypo_average, columns=['LE Forecast Hypot. 2025 Average'])
    #resultados4 = pd.DataFrame(modelo_mejora, columns=['Modelo_Predictivo'])
    resultadod = pd.concat([resultados,resultados1,resultados2,resultados3],axis=1)#,resultados4
    resultadod['Difference (%)']=(resultadod['LE Forecast Hypot. 2025 Average']/resultadod['LE Forecast 2025 Average'])-1

    resultado4=resultadod['Difference (%)']
    resultado4=pd.DataFrame(resultado4)
    resultado4=resultado4.rename(columns={'Difference (%)':'GDP Per Capita'})


    st.table(resultadod)

    
    
    df.drop('Unnamed: 0',inplace=True, axis=1)
    df=df.rename(columns={'Pais':'Country','EV_2020':'LE 2020','EV_2025':'LE 2025','EV_2025_Mejora':'LE 2025 Hypotetical'})

    agree = st.checkbox('Show Forecast Table')

    if agree:
        st.table(df)


if eleccion=='Conclusions':

    st.subheader("Final Conclusions")
    st.write('***')
    st.write('''
     _From the studies and analyzes carried out, it can be concluded that 3 of the 4 selected variables would have a greater positive 
    influence on the LE of the population of underdeveloped countries, but 2 of them showed better results 
    ('GDP Per Capita' and 'Rural Population (%)')._''')
    st.write('***')

    df = pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/KPI_Mort-Inf.csv')
        
    pais_desarrollo=[]
    ev_2020_average=[]
    ev_2025_average=[]
    ev_2025_hypo_average=[]

    pais_desarrollo.append('Developed Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] ==0)].mean()),4))

    pais_desarrollo.append('Developing Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] !=0)].mean()),4))
    resultados = pd.DataFrame(pais_desarrollo, columns=['Developed Level'])
    resultados1 = pd.DataFrame(ev_2020_average, columns=['LE 2020 Average'])
    resultados2 = pd.DataFrame(ev_2025_average, columns=['LE Forecast 2025 Average'])
    resultados3 = pd.DataFrame(ev_2025_hypo_average, columns=['LE Forecast Hypot. 2025 Average'])
    
    resultadoa = pd.concat([resultados,resultados1,resultados2,resultados3],axis=1)#,resultados4
    resultadoa['Difference (%)']=(resultadoa['LE Forecast Hypot. 2025 Average']/resultadoa['LE Forecast 2025 Average'])-1

    resultado1=resultadoa['Difference (%)']
    resultado1=pd.DataFrame(resultado1)
    resultado1=resultado1.rename(columns={'Difference (%)':'Infant Mortality'})
    resultado1=pd.concat([resultados,resultado1],axis=1)

    df = pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/KPI_CO2.csv')
        
    pais_desarrollo=[]
    ev_2020_average=[]
    ev_2025_average=[]
    ev_2025_hypo_average=[]

    pais_desarrollo.append('Developed Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] ==0)].mean()),4))

    pais_desarrollo.append('Developing Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] !=0)].mean()),4))
    resultados = pd.DataFrame(pais_desarrollo, columns=['Developed Level'])
    resultados1 = pd.DataFrame(ev_2020_average, columns=['LE 2020 Average'])
    resultados2 = pd.DataFrame(ev_2025_average, columns=['LE Forecast 2025 Average'])
    resultados3 = pd.DataFrame(ev_2025_hypo_average, columns=['LE Forecast Hypot. 2025 Average'])
        
    resultadob = pd.concat([resultados,resultados1,resultados2,resultados3],axis=1)#,resultados4
    resultadob['Difference (%)']=(resultadob['LE Forecast Hypot. 2025 Average']/resultadob['LE Forecast 2025 Average'])-1

    resultado2=resultadob['Difference (%)']
    resultado2=pd.DataFrame(resultado2)
    resultado2=resultado2.rename(columns={'Difference (%)':'CO2 Emission'})

    df = pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/KPI_RURAL.csv')
        
    pais_desarrollo=[]
    ev_2020_average=[]
    ev_2025_average=[]
    ev_2025_hypo_average=[]

    pais_desarrollo.append('Developed Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] ==0)].mean()),4))

    pais_desarrollo.append('Developing Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] !=0)].mean()),4))
    resultados = pd.DataFrame(pais_desarrollo, columns=['Developed Level'])
    resultados1 = pd.DataFrame(ev_2020_average, columns=['LE 2020 Average'])
    resultados2 = pd.DataFrame(ev_2025_average, columns=['LE Forecast 2025 Average'])
    resultados3 = pd.DataFrame(ev_2025_hypo_average, columns=['LE Forecast Hypot. 2025 Average'])
        
    resultadoc = pd.concat([resultados,resultados1,resultados2,resultados3],axis=1)#,resultados4
    resultadoc['Difference (%)']=(resultadoc['LE Forecast Hypot. 2025 Average']/resultadoc['LE Forecast 2025 Average'])-1

    resultado3=resultadoc['Difference (%)']
    resultado3=pd.DataFrame(resultado3)
    resultado3=resultado3.rename(columns={'Difference (%)':'Rural Population (%)'})

    df = pd.read_csv('https://raw.githubusercontent.com/grupohenryds03/esperanza_vida/main/datasets/KPI_GDP.csv')
        
    pais_desarrollo=[]
    ev_2020_average=[]
    ev_2025_average=[]
    ev_2025_hypo_average=[]

    pais_desarrollo.append('Developed Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] ==0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] ==0)].mean()),4))

    pais_desarrollo.append('Developing Countrys')

    ev_2020_average.append(round((df['EV_2020'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_average.append(round((df['EV_2025'][(df['ID_INCOME'] !=0)].mean()),4))
    ev_2025_hypo_average.append(round((df['EV_2025_Mejora'][(df['ID_INCOME'] !=0)].mean()),4))
    resultados = pd.DataFrame(pais_desarrollo, columns=['Developed Level'])
    resultados1 = pd.DataFrame(ev_2020_average, columns=['LE 2020 Average'])
    resultados2 = pd.DataFrame(ev_2025_average, columns=['LE Forecast 2025 Average'])
    resultados3 = pd.DataFrame(ev_2025_hypo_average, columns=['LE Forecast Hypot. 2025 Average'])
        
    resultadod = pd.concat([resultados,resultados1,resultados2,resultados3],axis=1)#,resultados4
    resultadod['Difference (%)']=(resultadod['LE Forecast Hypot. 2025 Average']/resultadod['LE Forecast 2025 Average'])-1

    resultado4=resultadod['Difference (%)']
    resultado4=pd.DataFrame(resultado4)
    resultado4=resultado4.rename(columns={'Difference (%)':'GDP Per Capita'})


    conclu=pd.concat([resultado1,resultado2,resultado3,resultado4],axis=1)
    
    st.dataframe(conclu.style.highlight_max(axis=0))