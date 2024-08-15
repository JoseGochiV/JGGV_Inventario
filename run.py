from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL, MySQLdb


inventario = Flask(__name__)
"""
mysql = MySQL(inventario) #
inventario.secret_key = 'mysecretkey'  # Cambia esto a algo único y secreto
inventario.config['MYSQL_HOST']='127.0.0.1'
inventario.config['MYSQL_USER'] = "JoseG"
inventario.config['MYSQL_PASSWORD'] = "121290"
inventario.config['MYSQL_DB'] = "inventario_v1.0"
inventario.config['MYSQL_CURSORCLASS']= "DictCursor"
"""

@inventario.route('/',methods=["GET", "POST"])
def home():
    titulo="Inventario"
    return render_template("home/home.html",titulo=titulo)
#________________________usuario___________________________________

@inventario.route('/usuarios',methods=["GET", "POST"])
def User():
    """
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
"""
    return render_template("usuarios/usuarios.html")


@inventario.route('/listar',methods=["GET", "POST"])
def listar():
    """

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios")
    usuarios = cur.fetchall()
    cur.close()

    return render_template("usuarios/listar.html", usuarios=usuarios)
    """
    return render_template("usuarios/listar.html")

@inventario.route('/usuariosactualizar/<int:id>', methods=["GET", "POST"])
def usuariosactualizar(id):
    """
    cur = mysql.connection.cursor()
    
    # Obtener el usuario de la base de datos utilizando el ID
    cur.execute("SELECT * FROM usuarios WHERE id = %s", (id,))
    usuario = cur.fetchone()
    cur.close()

    if request.method == "POST":
        # Recoger los datos del formulario
        nombre = request.form['cliente_nombre']
        apellido_paterno = request.form['cliente_apellido_paterno']
        apellido_materno = request.form['cliente_apellido_materno']
        clave_empleado = request.form['clave_empleado']

        # Actualizar el usuario en la base de datos
        cur = mysql.connection.cursor()
        cur.execute("""
    """

            UPDATE usuarios 
            SET nombre = %s, apellido_paterno = %s, apellido_materno = %s, clave_empleado = %s 
            WHERE id = %s
        """
    """
, (nombre, apellido_paterno, apellido_materno, clave_empleado, id))
        mysql.connection.commit()
        cur.close()

        flash('Usuario actualizado correctamente')
        return redirect(url_for('listar'))
    return render_template("usuarios/usuariosactualizar.html", usuario=usuario)
    """

    return render_template("usuarios/usuariosactualizar.html")


#________________________actualizar material____________________________________________________________

@inventario.route('/materiales',methods=["GET", "POST"])
def Materiales():
    """

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

"""

    return render_template("materiales/materiales.html")


@inventario.route('/listamateriales', methods=["GET", "POST"])
def listarMateriales():
    """

    if request.method == "POST":
        # Aquí manejarías la lógica del POST, si fuera necesario
        pass

    # Obtener los materiales siempre para listar
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM materiales")
    materiales = cur.fetchall()
    cur.close()

    return render_template("materiales/listarmaterial.html", materiales=materiales)

    """
    return render_template("materiales/listarmaterial.html")



@inventario.route('/materialactualizar/<int:id>', methods=["GET", "POST"])
def materialactualizar(id):
    """
    
    cur = mysql.connection.cursor()

    # Obtener el material por ID
    cur.execute("SELECT * FROM materiales WHERE id = %s", (id,))
    material = cur.fetchone()
    cur.close()

    if request.method == "POST":
        # Obtener datos del formulario
        codigo = request.form['codigo']
        descripcion = request.form['descripcion']
        fecha_alta = request.form['fecha_alta']
        status = request.form['status']
        responsable = request.form['responsable']
        fecha_baja = request.form['fecha_baja']

        # Actualizar el material
        cur = mysql.connection.cursor()
        cur.execute("""
    """
    
            UPDATE materiales
            SET codigo = %s, descripcion = %s, fecha_alta = %s, status = %s, responsable = %s, fecha_baja = %s
            WHERE id = %s
        """
    """
    , (codigo, descripcion, fecha_alta, status, responsable, fecha_baja, id))
        mysql.connection.commit()
        cur.close()

        flash('Material actualizado correctamente')
        return redirect(url_for('listarMateriales'))

    return render_template("materiales/materialactualizar.html", material=material)
    """
    return render_template("materiales/materialactualizar.html")




#inventario.run(debug=True, port=0.0.0.0) # Docker con puesto 5000
inventario.run(debug=True, port=4500)



