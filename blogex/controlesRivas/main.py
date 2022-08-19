from flask import Flask, render_template, request, json, redirect,session
from flaskext.mysql import MySQL
#https://www.it-swarm-es.com/es/python/usando-mysql-en-flask/941923326/
# Para ejecutar el servicio debo ejecutar main.py

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
    #session.pop('user', None)
    return render_template('signin.html')



@app.route('/showSignin')
def showSignin():
    if session.get('user'):#Si la sesion del usuario sigue activa ingresamos
        return render_template('usuarioNormal.html')
    else:
        return render_template('signin.html')#Ingresamois con nuestro usuario

@app.route('/usuarioNormal')
def usuarioNormal():
    if session.get('user'):
        return render_template('usuarioNormal.html')
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
    _username = request.form['inputEmail']
    _password = request.form['inputPassword']
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('validarLogin',(_username,))#Llamamos al procedimiento validarLogin de nuestra base de datos
    data = cursor.fetchall()#Obtenemos el resultado  en este caso una tabla
    if len(data)>0:#Si la tabla no esta vacia
        if str(data[0][7]) == _password:
            session['user'] = data[0][0]#asignamos id_usuario
            if data[0][8]:
               return redirect('/usuarioNormal')
            else: 
                return redirect('/usuarioVip')
        else:
            return render_template('error.html', error='Usuario o contraseña es incorrecta')
    else:
        return render_template('error.html', error = 'Usuario no existe')
    cursor.close()
    conn.close()


if __name__ == "__main__":
    app.run()


