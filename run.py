from flask import Flask,render_template,request
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

@inventario.route('/usuarios',)
def User():
    return render_template("usuarios/usuarios.html")

@inventario.route('/actualizar')
def Actualizar():
    return render_template("actualizar/actualizar.html")

@inventario.route('/materiales')
def Materiales():
   return render_template("materiales/materiales.html")




"""
@inventario.route('/Borrar')
def Borrar():
    return "Ventana de Borrar ----- Lupillo:2"
"""


inventario.run(debug=True, port=4500)



