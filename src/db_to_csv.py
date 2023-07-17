from dotenv import load_dotenv
from os import environ
import pymysql
import csv

load_dotenv()

username = environ.get('USER_DB_AWS')
password = environ.get('PASSWORD_DB_AWS')
host =  environ.get('HOST_DB_AWS')
port = 3306

db = pymysql.connect(host=host, user=username, password=password, database='DE_project_database')

cursor = db.cursor()

# Ejecutar consulta para obtener los datos
select_query = 'SELECT * FROM queries'
cursor.execute(select_query)
data = cursor.fetchall()

# Obtener las columnas del resultado
columns = [column[0] for column in cursor.description]

# Ruta del archivo CSV
csv_path = '/data/queries.csv'

# Guardar los datos en el archivo CSV
with open(csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(columns)  # Escribir las columnas en la primera fila
    writer.writerows(data)  # Escribir los datos en las filas siguientes

db.close()
