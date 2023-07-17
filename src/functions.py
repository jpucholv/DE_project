from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from datetime import datetime
from dotenv import load_dotenv
import pymysql
import os

load_dotenv()

# Obtener las variables de entorno
os.environ["OPENAI_API_KEY"] = os.environ.get('OPENAI_API_KEY')
os.environ["SERPAPI_API_KEY"] = os.environ.get('SERPAPI_API_KEY')

username = os.environ.get('USER_DB_AWS')
password = os.environ.get('PASSWORD_DB_AWS')
host =  os.environ.get('HOST_DB_AWS')
port = 3306

def query_process(query):
    # Cargar el modelo y herramientas necesarias
    llm = OpenAI()
    tools = load_tools(["serpapi", "llm-math"], llm=llm)

    # Inicializar el agente
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

    # Ejecutar el agente para procesar la consulta
    return agent.run(query)

def db_insert(query, response):
    # Establecer conexión a la base de datos
    db = pymysql.connect(host=host,
                         user=username,
                         password=password,
                         cursorclass=pymysql.cursors.DictCursor)
    
    cursor = db.cursor()

    # Seleccionar la base de datos
    use_db = ''' USE DE_project_database'''
    cursor.execute(use_db)


    # Obtener la fecha y hora actual
    # current_datetime = datetime.now()
    current_datetime = datetime.now().strftime(r'%Y-%m-%d %H:%M:%S')

    insert_data = '''
    INSERT INTO queries (date, query, response)
    VALUES (%s, %s, %s)
    '''

    # Ejecutar la consulta SQL con los valores de los parámetros
    cursor.execute(insert_data, (current_datetime, query, response))

    # Guardar cambios
    db.commit()

    # Cerrar conexión 
    db.close()