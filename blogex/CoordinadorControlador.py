from flask import Flask, render_template, request, json, redirect,session
from flaskext.mysql import MySQL


app = Flask(__name__)
app.debug = True
mysql = MySQL()
app.secret_key = 'secreto'
#MySQL Configuracion
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Asd-1098#'
app.config['MYSQL_DATABASE_DB'] = 'UNSA'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



@app.route("/")
def main():
    return render_template('login.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/get_solicitud')
def get_solicitud():
    if session.get('user'):
        _user = session.get('user')
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT id_solicitud,nombre,apellidoPaterno, apellidoMaterno, correo FROM Solicitudes;')
        data = cursor.fetchall()
        solicitud_list = []
        for solicitud in data:
            solicitud_list = {
                'Id_solicitud': str(solicitud[0]),
                'Nombre': solicitud[1],
                'apellidoPaterno':solicitud[2],
                'apellidoMaterno':solicitud[3],
                'correo':solicitud[4]}
            solicitud_list.append(solicitud_list)
        return json.dumps(solicitud_list)
    else:
        return render_template('error.html', error='Acceso no Autorizado')
#Control de sesion
@app.route('/usuarioNormal')
def usuarioNormal():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('error.html',error = 'Acceso No Autorizado')
    
@app.route('/Coordinador')
def Coordinador():
    if session.get('user'):
        return render_template('Coordinador.html')
    else:
        return render_template('error.html',error = 'Acceso No Autorizado')

@app.route('/usuarioVip')
def usuarioVip():
    if session.get('user'):
        return render_template('usuarioVip.html')
    else:
        return render_template('error.html',error = 'Acceso No Autorizado')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route('/validateLogin', methods = ['POST'])
def validateLogin():
    _username = request.form['username']
    _password = request.form['password']
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('validarLogin',(_username,))#Llamamos al procedimiento validarLogin de nuestra base de datos
    data = cursor.fetchall()#Obtenemos el resultado  en este caso una tabla
    if len(data)>0:#Si la tabla no esta vacia
        if str(data[0][7]) == _password:
            session['user'] = data[0][0]#asignamos id_usuario
            if data[0][8]==1:
               return redirect('/usuarioNormal')
            elif data[0][8]==0: 
                return redirect('/usuarioVip')
            else:
                return redirect('/Coordinador')
        else:
            return render_template('error.html', error='Usuario o contraseña es incorrecta')
    else:
        return render_template('error.html', error = 'Usuario no existe')
    cursor.close()
    conn.close()

@app.route('/signUp', methods = ['POST','GET'])
def signUp():
    _usuario = request.form['usuario']
    _contrasena = request.form['contrasena']
    _nombre = request.form['nombre']
    _apellidoPaterno = request.form['apellidoPaterno']
    _apellidoMaterno = request.form['apellidoMaterno']
    _correo = request.form['correo']
    _telefono = request.form['telefono']
    _estudios = request.form['estudios']
    _descripcion = request.form['descripcion']
    if _usuario and _contrasena and _nombre and _apellidoPaterno and _apellidoMaterno and _correo and _telefono and _estudios and _descripcion:
        conn = mysql.connect()
        if (conn):
            print("Conexion establecida")
        else:
            print("Conexion fallida")
        cursor = conn.cursor()
        cursor.callproc('crearUsuario',(_usuario, _contrasena, _nombre, _apellidoPaterno, _apellidoMaterno, _correo, _telefono, _estudios, _descripcion))
        data = cursor.fetchall()
        if len(data) ==0:
            #conn.commit()
            #print("Usuario fue creado!")
            return render_template('correcto.html', _correcto='Usuario fue creado')
        else:
            return render_template('error.html', error='Usuario ya existe')
    else:
        return render_template('error.html', error='Ningun campo debe estar vacio')
    cursor.close()
    conn.close()
    
@app.route('/getPropuesta')
def getPropuesta():
    if session.get('user'):
        _user = session.get('user')

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('obtenerPropuesta', (_user,))
        data = cursor.fetchall()
        deseos_list = []
        for deseo in data:
            deseo_list = {
                'Id': deseo[0],
                'Titulo': deseo[1],#marca
                'Tema': deseo[2],
                'Descripcion': deseo[3],
                'Tipo':deseo[4]}#precio
            deseos_list.append(deseo_list)
        return json.dumps(deseos_list)
    else:
        return render_template('error.html', error='Acceso no Autorizado')
    cursor.close
    conn.close

@app.route('/addPropuesta', methods=['POST'])
def addPropuesta():
    if session.get('user'):
        _titulo = request.form['titulo']
        _tema = request.form['tema']
        _descripcion = request.form['descripcion']
        _tipo = request.form['tipo']
        _user = session.get('user')
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('agregarPropuesta', (_titulo,_tema,_descripcion,_tipo, _user))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return redirect('usuarioNormal')
        else:
            return render_template('error.html', error='Un error detectado')

    else:
        return render_template('error.html', error='Acceso no Autorizado')
    cursor.close
    conn.close

@app.route('/showaddPropuesta')
def showaddPropuesta():
    return render_template('addPropuesta.html')

@app.route('/getTOTALPropuesta')
def getTOTALPropuesta():
    if session.get('user'):
        _user = session.get('user')

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('SELECT * FROM Propuesta')
        data = cursor.fetchall()
        deseos_list = []
        for deseo in data:
            deseo_list = {
                'Id': deseo[0],
                'Titulo': deseo[1],#marca
                'Tema': deseo[2],
                'Descripcion': deseo[3],
                'Tipo':deseo[4]}#precio
            deseos_list.append(deseo_list)
        return json.dumps(deseos_list)
    else:
        return render_template('error.html', error='Acceso no Autorizado')
    cursor.close
    conn.close


@app.route('/delete/<string:id>', methods = ['POST','GET']) 
def deletePropuesta():
    if session.get('user'):
        _id_propuesta = request.form['id_propuesta']
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Propuesta WHERE id_propuesta={}'.format(_id_propuesta))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return redirect('Coordinador')
        else:
            return render_template('error.html', error='Un error detectado')

    else:
        return render_template('error.html', error='Acceso no Autorizado')
    cursor.close
    conn.close

if __name__ == "__main__":
    app.run()
    
