Sistema de Publicación de Eventos UNSA
=================

Alumno: John Edson Sanchez Chilo  
**Estilos de Programacion aplicados**  
  
Estilo #1:  Code-golf  

```
@app.route("/")  
def main():  
    return render_template('indexCoord.html') 
```

Estilo #2:  CookBook

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


```
def getSolicitud():
    if session.get('user'):
        _user = session.get('user')
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT id_solicitud,nombre,apellidoPaterno, apellidoMaterno, correo FROM Solicitudes;')
        data = cursor.fetchall()
```
