from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL, MySQLdb


inventario = Flask(__name__)

mysql = MySQL(inventario) #
inventario.secret_key = 'mysecretkey'  # Cambia esto a algo único y secreto
inventario.config['MYSQL_HOST']='127.0.0.1'
inventario.config['MYSQL_USER'] = "JoseG"
inventario.config['MYSQL_PASSWORD'] = "121290"
inventario.config['MYSQL_DB'] = "inventario_v1.0"
inventario.config['MYSQL_CURSORCLASS']= "DictCursor"


@inventario.route('/',methods=["GET", "POST"])
def home():
    titulo="Inventario"
    return render_template("home/home.html",titulo=titulo)
#________________________usuario___________________________________
@inventario.route('/usuarios',methods=["GET", "POST"])
def User():
    if request.method == "POST":
        nombre = request.form['cliente_nombre']
        apellido_paterno = request.form['cliente_apellido_paterno']
        apellido_materno = request.form['cliente_apellido_materno']
        clave_empleado = request.form['clave_empleado']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuarios (clave_empleado, apellido_paterno, apellido_materno, nombre ) VALUES (%s, %s, %s, %s)", (clave_empleado, apellido_paterno, apellido_materno,nombre))
        mysql.connection.commit()
        cur.close()

        flash('Usuario agregado correctamente')
        return redirect(url_for('User'))

    return render_template("usuarios/usuarios.html")


@inventario.route('/listar',methods=["GET", "POST"])
def listar():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios")
    usuarios = cur.fetchall()
    cur.close()
    return render_template("usuarios/listar.html", usuarios=usuarios)



@inventario.route('/usuariosactualizar',methods=["GET", "POST"])
def usuariosactualizar():   

    return render_template("usuarios/usuariosactualizar.html")


#________________________actualizar material____________________________________________________________

@inventario.route('/materiales',methods=["GET", "POST"])
def Materiales():
    if request.method == "POST":
        codigo = request.form['codigo']
        descripcion = request.form['descripcion']
        fecha_alta = request.form['fecha_alta']
        status = request.form['status']
        responsable = request.form['responsable']
        fecha_baja = request.form['fecha_baja']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO materiales (codigo, descripcion, fecha_alta, status, responsable, fecha_baja) VALUES (%s, %s, %s, %s, %s, %s)",
                    (codigo, descripcion, fecha_alta, status, responsable, fecha_baja))
        mysql.connection.commit()
        cur.close()

        flash('Material agregado correctamente')
        return redirect(url_for('Materiales'))


    return render_template("materiales/materiales.html")


@inventario.route('/listamateriales', methods=["GET", "POST"])
def listarMateriales():
    if request.method == "POST":
        # Aquí manejarías la lógica del POST, si fuera necesario
        pass

    # Obtener los materiales siempre para listar
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM materiales")
    materiales = cur.fetchall()
    cur.close()
    
    return render_template("materiales/listarmaterial.html", materiales=materiales)

@inventario.route('/materialactualizar',methods=["GET", "POST"])
def materialactualizar():   

   return render_template("materiales/materialactualizar.html")



#___________________________________actualizar materiales___________________
"""
@inventario.route('/actualizar')
def Actualizar():

    return render_template("actualizar/actualizar.html")

@inventario.route('/listaactualizar')
def ListarActualizar():

    return render_template("actualizar/listaactualizar.html")

"""





"""
@inventario.route('/Borrar')
def Borrar():
    return "Ventana de Borrar ----- Lupillo:2"
"""


#inventario.run(debug=True, port=0.0.0.0) # Docker con puesto 5000
inventario.run(debug=True, port=4500)



