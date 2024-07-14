from flask import Flask
from flask_mysqldb import MySQL, MySQLdb

inventario = Flask(__name__)

mysql = MySQL(inventario)

inventario.config['MYSQL_HOST']='127.0.0.1'
inventario.config['MYSQL_USER'] = "JoseG"
inventario.config['MYSQL_PASSWORD'] = "121290"
inventario.config['MYSQL_DB'] = "inventario_v1.0"


@inventario.route('/')
def home():
    
    return "Primer Inventario , Hola:Compadre"

@inventario.route('/usuarios')
def User():
    return "Ventana de Usuarios ----  RO:2"

@inventario.route('/actualiza')
def Actualiza():
    return "Ventana de Actualizar ----- RO:2"

@inventario.route('/Borrar')
def Borrar():
    return "Ventana de Borrar ----- Lupillo:2"



inventario.run(debug=True, port=4500)



