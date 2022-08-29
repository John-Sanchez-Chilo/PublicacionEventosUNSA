Sistema de Publicación de Eventos UNSA
=================
Integrantes:  
- John Edson Sanchez Chilo  
- Jheeremy Manuel Alvarez Astete
- Diego Raul Rivas Huanca  

## 1. Proposito  
Con el presente trabajo se busca crear un sistema de de gestión para la publicación de eventos. Como alumnos de Ciencia de la Computación entendemos la necesidad de estar actualizados con nuevas tecnologias, frameworks, lenguajes etc. y una forma profesional de hacerlo es asistiendo a eventos realcionados a nuestros campos de interes en los cuales se realizen conferencias, workshops, simposios, etc. Es así que el presente trabajo cumple la necesidad de gestionar los diferentes tipos de eventos.  
  
## 2. Funcionalidades  
- Se  ha implementado un index del cual los usuarios podran ver las opciones respecto a la página y visualizar eventos
- Se tiene un registro de usuarios nuevos que quieren formar parte
- Se tiene un inicio de sesión para ingresar a las cuenta personales de los usuarios y no redirecciona si somos usuarios normales, vip o coordinador.
- En las cuentas de los usuarios  se presenta la funcionalidad de Realizar Propuesta de Evento, y nos mostrara en tiempo real las propuestas del usuario que realizo o acaba de realizar.
- En la parte de Coordinador se tiene la funcionalidad de Aceptar las Propuestas realizadas por parte de los usuarios y aceptarlas o denegarlas  
  
## 3. Practicas de Codigo Legible Aplicadas  
  
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
conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('SELECT * FROM Propuesta')
```
## 4. Estilos de programación aplicados  
  
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


## 5. Principios SOLID aplicados  
1. Single Responsability Principle(SRP)
```
#bad
class Horario:
    def __init__(self,dia,mes,año, hora, minuto):
#good
class Fecha:
    def __init__(self,dia,mes,año):
        ...
    
    def get_fecha(self):
        ...
class Horario:
    def __init__(self,hora,minuto):
        ...
    
    def get_horario(self):
        ...
```
  
2. Dependency Inversion Principle(DIP)
```
#bad
class Usuario_Normal:
    ...
class Usuario_VIP(Usuario_Normal):
    ...

#good
class Usuario:
    ...
class Usuario_Normal(Usuario):
    ...
class Usuario_VIP(Usuario):
    ...
```

3. Don't repeat yourself(DRY)

```
#bad
class Usuario:
    def __init__(self,id_usuario,nombre,apellido_paterno,apellido_materno,correo,telefono,usuario,contraseña):
        self.id_usuario=id_usuario
        self.nombre_completo=Nombre(nombre,apellido_paterno,apellido_materno)
        self.correo=correo
        self.telefono=telefono
        self.usuario=usuario
        self.contraseña=contraseña
class Usuario_Normal(Usuario):
    def __init__(self,id_usuario,nombre,apellido_paterno,apellido_materno,correo,telefono,centro_estudios,usuario,contraseña):
        self.id_usuario=id_usuario
        self.nombre_completo=Nombre(nombre,apellido_paterno,apellido_materno)
        self.correo=correo
        self.telefono=telefono
        self.centro_estudios=centro_estudios
        self.usuario=usuario
        self.contraseña=contraseña
#good
class Usuario:
    def __init__(self,id_usuario,nombre,apellido_paterno,apellido_materno,correo,telefono,usuario,contraseña):
        self.id_usuario=id_usuario
        self.nombre_completo=Nombre(nombre,apellido_paterno,apellido_materno)
        self.correo=correo
        self.telefono=telefono
        self.usuario=usuario
        self.contraseña=contraseña
        

class Usuario_Normal(Usuario):
    def __init__(self,id_usuario,nombre,apellido_paterno,apellido_materno,correo,telefono,centro_estudios,usuario,contraseña):
        super().__init__(id_usuario,nombre,apellido_paterno,apellido_materno,correo,telefono,usuario,contraseña)
        self.centro_estudios=centro_estudios

```
## 6. Conceptos DDD aplicados  
1. Entidades (Entities)  
```

class Usuario:
    def __init__(self,id_usuario,nombre,apellido_paterno,apellido_materno,correo,telefono,usuario,contraseña):
        ...
  
class Evento():
    def __init__(self,id_evento,titulo,tema,descripcion, id_encargado):
        ...

class Propuesta(object):
    def __init__(self,id_propuesta=None, titulo=None, descripcion=None, tema=None,):
        ...

class Coordinador:
    def __init__(self,id_coordinador,nombre, especialidad):
        ...
        
class Horario:
    def __init__(self,hora,minuto):
        ...
    

```
2. Objetos de valor (Object Values)  
```

class Fecha:
    def __init__(self,dia,mes,año):
        ...

class Horario:
    def __init__(self,hora,minuto):
        ...

class Conferencia(Evento):
    def __init__(self,id_evento,titulo,tema,descripcion, id_encargado,id_evento_conferencia,fecha_inicio, fecha_fin):
        super().__init__(id_evento,titulo,tema,descripcion, id_encargado)
        self.id_evento_conferencia = id_evento_conferencia
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        ...
```
3. Modulos (Modules)  
Se ha realizado las division de modulos por sus dominios relacionados dividiendo en  
- Agentes: Coordinador  
- Evento: Evento, Workshop, Simposio, Conferencia
- Propuesta: Propuesta
- Usuario: USuario, UsuarioNormal, UsuarioVIP
- Utildiad: Fecha, Horario

