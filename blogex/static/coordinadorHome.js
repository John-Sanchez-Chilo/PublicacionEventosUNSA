$(function(){
    $.ajax({
        url : '/getPropuesta',
        type: 'GET',
        success: function(res){
            var div = $('<tr>')
                .append($('<th>').attr('scope', 'row')
                .append($('<td>').attr('class',"nombre"),
                    $('<td>').attr('class',"correo"),
                    $('<td>').attr('class',"aceptar")
                ));
            var solicitudObj=JSON.parse(res);
            var solicitud = '';
            $.each(solicitudObj,function(index,value){
                solicitud=$(div).clone();
                $(solicitud).find('th').text(value.Id);
                $(solicitud).find('td').text(value.Nombre);
                $(solicitud).find('td').text(value.Correo);
                $('.table_rows').append(solicitud);
            });
        },
        error: function(error){
            console.log(error);
        }
    })
})