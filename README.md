Sistema de Publicación de Eventos UNSA
=================

Alumno: John Edson Sanchez Chilo  
**Estilos de Programacion aplicados**  
  
Estilo #1:  Code-golf  
Direccion: blogex/Controller/CoordinadorControlador.py 
```
@app.route("/")  
def main():  
    return render_template('coordinadorHome.html') 
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
Direccion: blogex/Controller/CoordinadorControlador.py

```
def get_solicitud():
    if session.get('user'):
        _user = session.get('user')
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT id_solicitud,nombre,apellidoPaterno, apellidoMaterno, correo FROM Solicitudes;')
        data = cursor.fetchall()
```

**Practicas de Clean Code Aplicadas**  
Practica #1: Comentar y documentar

```
    #funcion para pasar una propuesta aceptada a un evento ascociando al encargado
    def convertir_a_evento(self,encargado):
        evento=Evento(self.id_propuesta,self.titulo,self.descripcion,encargado,self.tema)
        return evento
```
Practica #2: Identación Consistente

```
class Propuesta(object):
    def __init__(self,id_propuesta=None, titulo=None, descripcion=None, tema=None,):
        self.id_propuesta = id_propuesta
        self.titulo = titulo
        self.descripcion = descripcion
        self.tema = tema
```
Practica #3: Esquema de Nomeclatura Coherente

```
@app.route('/get_solicitud')
def get_solicitud():
```
  
```
def convertir_a_evento(self,encargado):
  ...
```
Practica #4: Longitud de Linea Límite  

```
//bad
function(res){
var div = $('<tr>').append($('<th>').attr('scope', 'row').append($('<td>').attr('class',"nombre"),$('<td>').attr('class',"correo"),$('<td>').attr('class',"aceptar")));
var solicitudObj=JSON.parse(res);
var solicitud = '';
...
});

//good
function(res){
var div = $('<tr>')
    .append($('<th>').attr('scope', 'row')
    .append($('<td>').attr('class',"nombre"),
        $('<td>').attr('class',"correo"),
        $('<td>').attr('class',"aceptar")
    ));
var solicitudObj=JSON.parse(res);
var solicitud = '';
...
});
```

Practica #5: Poner MAYUSCULAS las palabras reservadas de SQL  

```
def get_solicitud():
    if session.get('user'):
        _user = session.get('user')
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT id_solicitud,nombre,apellidoPaterno, apellidoMaterno, correo FROM Solicitudes;')
```
