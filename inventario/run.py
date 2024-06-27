from flask import Flask

inventario = Flask(__name__)


@inventario.route('/')
def home():
    return "Primer Inventario , Hola"

@inventario.route('/usuarios')
def home():
    return "Ventana de Usuarios ----  RO"

@inventario.route('/actualiza')
def home():
    return "Ventana de Actualizar ----- RO"

inventario.run(debug=True, port=4500)



