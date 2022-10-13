# Proyecto Final -Data 03- Soy Henry
## Jhovany Lara, Rodrigo Ruiz, Pablo Poletti ,José María Toledo

### Consigna: Desarrollo de un Proyecto

Para este proyecto final, se elegio la Esperanza de Vida al Nacer.

### Ejecución

Se realizará un data lakehouse con un cluster en Databricks-Apache Spark, con almacenamiento en AWS. 
Para relaizar el trabajo colaborativo , se establece la conexión desde visual studio code local mediante un container en Docker con databrick-conection.

### Descripción de los pasos para el trabajo colaborativo sin container docker:

1. en terminal se crea el entorno de trabajo:
- descargar conda
- creacion del entorno: conda create -n dbconnect python=3.8.12 # pse crea el entorno para realizar la conexión en visual studio code con phyton y el cluster de databricks (dbconnect es el nombre del entorno), no cambiar la versión ya que puede generar problema con el conector de databricks
- activar el entorno: conda activate dbconnect
- se desinstala pyspark: pip uninstall pyspark # se desinstala el modulo de pyspark si es que esta instalado en el nuevo entorno por conflicto con el conector de databricks
- instalar el conector con databricks: pip install -U databricks-connect==9.1.8. # no cambiar la versión ya que puede generar problema con la versión de phyton instalada para el entorno en cuestión
- se realiza la conexión al cluster creado databricks: databricks-connect configure # 
- para realizar la conexión al cluster, igresan lo siguiente:
token: xxxxxxxxxxxx
host: https://dbc-4dcb8a77-7743.cloud.databricks.com/
Org ID: xxxxxxxx
Cluster ID: xxx-xxxxx-udib18tb
- se instala pandas: pip install pandas #instalan pandas en el entorno
para pode utilizar el modulo de pyspark sin conflictos de versiones
correr: databricks-connect get-jar-dir # copiar la ruta que les de
2. en visual studio code:
- seleccionar el entorno dbconnect para correr el código
- ir a Code > Preferences > Settings-> python settings. # es un json que se tiene que modificar
- dentro de json incluir:{“python.venvPath”: “la ruta que copiaron cuando ejecutaron databricks-connect get-jar-dir “,“python.linting.eneble”:false}
3. en un jupiter notebook:
- from pyspark.sql import SparkSession # modulo para crear la sesión que fue conectada con - databricks-connect al cluster
- import pandas as pd # nuestro amigo pandas
- spark = SparkSession.builder.getOrCreate() #conecto
- data = pd.read_csv(“dirección web del csv”) # creo dataframe con amigo pandas
- pysparkDF = spark.createDataFrame(data = data) #creo un dataframe de spark
- pysparkDF.write.saveAsTable(“nombre de tabla”) # ingesto el dataframe de spark a una tabla en databricks. se puede ver en solapa data de la aplicación de databricks la tabla ingestada
- result_pdf = pysparkDF.select("*").toPandas() # para obtener nuevamente un dataframe de pandas
o utilizar:
- pd_df = spark.sql('select * from ‘nombre tabla’).toPandas()



### Descripción de los pasos para el trabajo colaborativo con container docker:

1. conar este repo: git clone https://github.com/grupohenryds03/esperanza_vida

dentro de la carpeta container:

- *.devcontainer*->carpepeta para realizar el container en Visual Studio Code (VSC)

- *Dockerfile*-> archivo docker para la cracion del container

- *.databricks-connect.template* ->archivo con datos en formato .json para la conección con databricks

- *devcontainer.json*->archivo .json con especificaciones del entorno para la conexión 

- para la creacion del container en VSC, se va a From Remote-Containers: Reopen in Container y se eleje la carpeta *.devcontainer*





