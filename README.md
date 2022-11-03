# Latin-Data
## Proyecto Final -Data 03- Soy Henry
### Jhovany Lara, Rodrigo Ruiz, Pablo Poletti , José Toledo

## Tabla de contenidos
1. [Consigna](#Consigna)
2. [Arquitectura](#Arquitectura)
3. [Trabajo_Colaborativo](#Trabajo_Colaborativo)
4. [Paises_elegidos](#Paises_elegidos)
5. [Indicadores_elejidos](#Indicadores_elejidos)
7. [Machine_Learning](#Machine_Learning)
8. [Documentación](#Documentación)

## Consigna
## Desarrollo de un proyecto

Para este proyecto final, se elegio la Esperanza de Vida al Nacer. En el rol de una consultora de datos, nuestro potencial cliente desea conocer los distintos factores que tienen incidencia en el resultado de la Esperanza de vida al nacer y, a su vez, cómo se manifiestan. Para ello se desarrolló un framework para el análisis de la data. 


## Arquitectura

- La arquitectura sigue cinco pasos principales: el primero para analizar las fuentes de datos, el segundo para la Extracción, Trasformación (limpieza) y Carga (Load) llamado por sus siglas ETL. El tercer paso donde se realiza la carga incremental a la base de datos relacional, el cuarto la carga incremental y el último paso donde se realizan las consultas necesarias para ser utilizada en modelos de ML y visualización en dashboard.

1. busqueda de data y análisis para data cruda.
2. Ingesta data cruda, limpieza y carga (ETL). https://etl-latin-data.herokuapp.com/ el repositorio del deploy es: https://github.com/grupohenryds03/airflow-heroku
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
 $ pip install conda #se descarga condas
 $ conda create -n dbconnect python=3.8 #creacion del entorno
 $ conda activate dbconnect #activar el entorno
 $ pip install snowflake-connector-python[pandas] #se instala el conector con snowflake
```

- para realizar la conexión a la base de datos de snowflake, se creo un archivo snow.py con los datos de acceso que se ignora con gitignore para no mostar claves importantes.

```python
import snowflake.connector # se importa conector
from snow import * # se importan claves de acceso
conn = snowflake.connector.connect(
    user=snow_user,
    password=snow_pasoword,
    account=snow_account,
    warehouse=snow_warehouse,
    database=snow_database
    )
```

## Paises_elegidos

- Se selecciono una muestra de países teniendo en cuenta incluir estados de los 5 continentes que sean representativos, tengan buena calidad en la información histórica recolectada por el World Bank para la confección de sus indicadores.
-  Inicialmente se utilizó como filtro para diferenciar la muestra por continentes, el status de países “desarrollados” vs “en desarrollo”, pero tomando en cuenta la clasificación que realiza las naciones unidas se observo que tanto en América Latina, África como en Medio Oriente, se necesitaba incluir otro nivel de clasificación para mejorar la diferenciación; por lo cual se decidió utilizar la clasificación por nivel de ingresos que realiza el World Bank mediante el “GNI (Ingreso Bruto Nacional)  per cápita” y así poder mejorar la diferenciación de los efectos de las diferentes variables sobre la esperanza de vida, según el país o continente en estudio.


## Indicadores_elegidos
- Para la evaluación, se tendrán en cuenta los factores socioeconómicos y de Salud.  
- Para la selección de factores, en una primera instancia, los datos crudos tenían 38 indicadores. Haciendo un análisis exploratorio nos encontramos que el principal problema en nuestros datos eran los valores faltantes, lo que representaba un gran problema para nuestro proyecto. 
- Decidimos eliminar aquellos indicadores que tengan más de un 20% de valores faltantes, con esto nos quedamos con tan solo 17 indicadores con un porcentaje de aproximadamente 3% de datos faltantes. 
- Se imputo el promedio de los vecinos mas cercanos con algoritmo de machine learning.

## Machine_Learning

- Para el análisis estadístico de la expectativa de vida promedio de cada país, lo primero que hicimos fue determinar que los tipos de indicadores con los que íbamos a trabajar eran series de tiempo y luego estudiar qué modelo predictivo era el más conveniente. 
- Considerando las diferentes opciones decidimos que lo mejor era aprovechar al máximo las herramientas que nos brinda la ciencia de datos y buscar automatizar los procesos estadísticos y predictivos.
Para ello recurrimos a la librería Pycaret que nos brindaba la posibilidad de proyectar a 10 años la expectativa de vida usando más de 30 algoritmos, cross validation, métodos de ensamble, optimización de hiperparametros y métodos de mezcla para seleccionar el mejor modelo en cada caso, segun la media absoluta escalada del error.
- Luego se seleccionaron 4 variables relevantes para analizar su efecto real proyectado contra una hipotética mejora del 10% anual por 5 años sobre la esperanza de vida diferenciando entre países desarrollados y en vías de desarrollo. Los supuestos se tomaron para que esta mejora hipotética tenga un efecto positivo mayor sobre la esperanza de vida de los países en vías de desarrollo.

## Documentación

- AIRFLOW: https://airflow.apache.org/docs/
- PANDAS: https://pandas.pydata.org/docs/
- SNOWFLAKE: https://docs.snowflake.com/en/
- STREAMLIT:https://docs.streamlit.io/
- PYCARET: https://pycaret.gitbook.io/docs/
- WBAPI:https://pypi.org/project/wbgapi/
- PLOTLY:https://plotly.com/python/
- SKLEARN: https://scikit-learn.org/stable/user_guide.html
