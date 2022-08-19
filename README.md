Sistema de Publicación de Eventos UNSA
=================

Alumno: John Edson Sanchez Chilo  
**Estilos de Programacion aplicados**  
  
Estilo #1:  Code-golf  
Direccion: Blogex/Controller/CoordinadorControlador.py 
```
@app.route("/")  
def main():  
    return render_template('indexCoord.html') 
```

Estilo #2:  CookBook
Direccion: blogex/static/coordinadorHome.js
```
$.each(solicitudObj,function(index,value){
    solicitud=$(div).clone();
    $(solicitud).find('th').text(value.Id);
    $(solicitud).find('td').text(value.Nombre);
    $(solicitud).find('td').text(value.Correo);
    $('.table_rows').append(solicitud);
 });
```

Estilo #3: Persistent Tables  
Direccion: Blogex/Controller/CoordinadorControlador.py

```
def getSolicitud():
    if session.get('user'):
        _user = session.get('user')
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT id_solicitud,nombre,apellidoPaterno, apellidoMaterno, correo FROM Solicitudes;')
        data = cursor.fetchall()
```
