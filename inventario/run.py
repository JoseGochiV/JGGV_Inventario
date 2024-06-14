from flask import Flask

inventario = Flask(__name__)


@inventario.route('/')
def home():
    return "Primer Inventario , Hola"

inventario.run()

