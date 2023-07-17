from flask import Flask, request, render_template
import os
import src.functions as functions

app = Flask(__name__)
app.config['DEBUG'] = True

app.template_folder = 'src/static/html/'
app.static_folder = 'src/static'

# Ruta de inicio
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Ruta para recibir y procesar la consulta
@app.route('/response', methods=['GET', 'POST'])
def post_query():
    # Obtener la consulta del parámetro de la URL
    query = request.args.get('query')
    
    # Procesar la consulta utilizando la función query_process
    response = functions.query_process(query)
    
    # Insertar la consulta y respuesta en la base de datos utilizando la función db_insert
    functions.db_insert(query=query, response=response)

    # Renderizar la plantilla de respuesta y pasar la consulta y respuesta como variables
    return render_template('response.html', query=query, response=response)

if __name__ == '__main__':
    # Ejecutar la aplicación Flask
    app.run(debug=True, host='0.0.0.0', port=os.environ.get("PORT", 5000))
