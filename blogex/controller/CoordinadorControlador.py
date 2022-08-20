from flask import Flask, render_template, request, json, redirect,session
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()
app.secret_key = 'secreto'
#MySQL Configuracion
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin_1572003_jesc'
app.config['MYSQL_DATABASE_DB'] = 'tienda_lentes'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



@app.route("/")
def main():
    return render_template('indexCoord.html')

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
