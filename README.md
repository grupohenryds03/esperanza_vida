# Latin-Data
## Proyecto Final -Data 03- Soy Henry
### Jhovany Lara, Rodrigo Ruiz, Pablo Poletti , José Toledo

## Tabla de contenidos
1. [Consigna](#Consigna)
2. [Arquitectura](#Arquitectura)
3. [Trabajo_Colaborativo](#Trabajo_Colaborativo)
4. [Documentación](#Documentación)

## Consigna
## Desarrollo de un proyecto

Para este proyecto final, se elegio la Esperanza de Vida al Nacer. En el rol de una consultora de datos, nuestro potencial cliente desea conocer los distintos factores que tienen incidencia en el resultado de la Esperanza de vida al nacer y, a su vez, cómo se manifiestan. Para ello se desarrolló un framework para el análisis de la data. 


## Arquitectura

- La arquitectura sigue cinco pasos principales: el primero para analizar las fuentes de datos, el segundo para la Extracción, Trasformación (limpieza) y Carga (Load) llamado por sus siglas ETL. El tercer paso donde se realiza la carga incremental a la base de datos relacional, el cuarto la carga incremental y el último paso donde se realizan las consultas necesarias para ser utilizada en modelos de ML y visualización en dashboard.

1. busqueda de data y análisis para data cruda.
2. Ingesta data cruda, limpieza y carga (ETL).
3. Tareas para la carga incremental.
4.  Ingesta de data a base de datos relacional.
5. Acceso a base de datos para modelar progresiones en machine lerning y visualización en dasboard.

<img src="/imagenes/arquitetura_bueno.jpg"/>


- Para la creación del dashboard se utiliza STREAMLIT: https://latin-data.streamlitapp.com/

- Para el deploy del dashboard se utiliza la herramienta propia STREAMLIT.

## Trabajo_colaborativo

- Para poder realizar el trabajo colaborativo ,se establece la conexión desde visual studio code local da cada integrante al repositorio compartido de GITHUB.

- en terminal se crea el entorno de trabajo para realizar con la conexión con snowflake en visual studio code en maquina local con lenguaje phyton:

```bash
 pip install conda #se descarga condas
 conda create -n dbconnect python=3.8 #creacion del entorno
 conda activate dbconnect #activar el entorno
 pip install snowflake-connector-python[pandas] #se instala el conector con snowflake
```

- para realizar la conexión a la base de datos de snowflake, se creo un archivo snow.py con los datos de acceso que se ignora con gitignore para no mostar claves importantes.

```python
import snowflake.connector # se importa conector
from snow import * # se importan claves de acceso
conn = snowflake.connector.connect(
    user='snow_user',
    password='snow_pasoword',
    account='snow_account',
    warehouse='snow_warehouse',
    database='snow_database'
    )
```

## Paises elegidos

- Se selecciono una muestra de países teniendo en cuenta incluir estados de los 5 continentes que sean representativos, tengan buena calidad en la información histórica recolectada por el World Bank para la confección de sus indicadores.
-  Inicialmente se utilizó como filtro para diferenciar la muestra por continentes, el status de países “desarrollados” vs “en desarrollo”, pero tomando en cuenta la clasificación que realiza las naciones unidas se observo que tanto en América Latina, África como en Medio Oriente, se necesitaba incluir otro nivel de clasificación para mejorar la diferenciación; por lo cual se decidió utilizar la clasificación por nivel de ingresos que realiza el World Bank mediante el “GNI (Ingreso Bruto Nacional)  per cápita” y así poder mejorar la diferenciación de los efectos de las diferentes variables sobre la esperanza de vida, según el país o continente en estudio.


## Variables elejidas

- de acuerdo a diferentes papers la seleccion de variables se separaron en salud y socio-económicas:
- papers realacionados

|                                                 Papers life expectancy                                                |                                   descripción                                   |
|:---------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| http://www.scielo.org.pe/scielo.php?script=sci_arttext&pid=S1025-55832011000400006                                    |                                                                                 |
| https://ruc.udc.es/dspace/bitstream/handle/2183/16409/RodriguezRodriguez_David_TFG_2015.pdf?sequence=2                |                                                                                 |
| https://population.un.org/wpp/Publications/Files/WPP2022_Methodology.pdf                                              |                         Metodologia UN para proyecciones                        |
| https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/undesa_pd_2022_wpp_key-messages.pdf |                   Informe UN "World Population Prospects 2022"                  |
| https://www.kaggle.com/search?q=life+expectancy                                                                       |                                      KAGGLE                                     |
| https://www.kaggle.com/code/nilaychauhan/etl-pipelines-tutorial-world-bank-datasets                                   |                                                                                 |
| https://www.ucm.es/data/cont/docs/518-2016-09-15-Tema2_regresi%C3%B3n%20con%20series%20temporales.pdf                 |                  Analizar Correlacion Espuria (como filtrarla)                  |
| https://core.ac.uk/download/pdf/6264941.pdf                                                                           |              Correlacion Espuria (como filtrarla) Con cointegracion             |
| https://www.linkedin.com/pulse/la-correlaci%C3%B3n-de-todos-los-males-valent%C3%ADn-chab/?originalSubdomain=es        |                               Correlacion Espuria                               |
| https://statisticsbyjim.com/basics/spurious-correlation/                                                              |                                                                                 |
| https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6650812/                                                                 |                  A Causal Analysis of Life Expectancy at Birth.                 |
| https://hrcak.srce.hr/file/178666                                                                                     | Determinant Factors of Life Expectancy at Birth in the European Union Countries |
| https://rstudio-pubs-static.s3.amazonaws.com/180554_a412caa868c24939a873ca679d54bbde.html                             |                          8 variables a tener en cuenta                          |
| https://www.analyticslane.com/2019/11/18/test-de-causalidad-de-wiener-granger/                                        | granger causality test ejemplo en Python                                        |

## Documentación

- AIRFLOW: https://airflow.apache.org/docs/
- PANDAS: https://pandas.pydata.org/docs/
- SNOWFLAKE: https://docs.snowflake.com/en/
- STREAMLIT:https://docs.streamlit.io/
- PYCARET: https://pycaret.gitbook.io/docs/
- WBAPI:https://pypi.org/project/wbgapi/
- PLOTLY:https://plotly.com/python/
- SKLEARN: https://scikit-learn.org/stable/user_guide.html