from flask import Flask

inventario = Flask(__name__)


@inventario.route('/')
def home():
    return "Primer Inventario , Hola:Compadre"

@inventario.route('/usuarios')
def User():
    return "Ventana de Usuarios ----  RO"

@inventario.route('/actualiza')
def Actualiza():
    return "Ventana de Actualizar ----- RO"

@inventario.route('/Borrar')
def Borrar():
    return "Ventana de Borrar ----- Lupillo"

inventario.run(debug=True, port=4500)



