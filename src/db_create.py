from dotenv import load_dotenv
from os import environ
import pymysql

load_dotenv()

# Obtener las variables de entorno
username = environ.get('USER_DB_AWS')
password = environ.get('PASSWORD_DB_AWS')
host =  environ.get('HOST_DB_AWS')
port = 3306

# Establecer la conexión a la base de datos
db = pymysql.connect(host=host,
                     user=username,
                     password=password,
                     cursorclass=pymysql.cursors.DictCursor)

cursor = db.cursor()

# Crear la base de datos
create_db = '''CREATE DATABASE DE_project_database'''
cursor.execute(create_db)

cursor.connection.commit()

# Usar la base de datos creada
use_db = ''' USE DE_project_database'''
cursor.execute(use_db)

# Crear la tabla 'queries'
create_table = '''
CREATE TABLE queries (
    id INT NOT NULL auto_increment,
    date TEXT,
    query TEXT,
    response TEXT,
    primary key (id)
)
'''
cursor.execute(create_table)

# Guardar cambios y cerrar la conexión
db.commit()
db.close()