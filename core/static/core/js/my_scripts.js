$(document).ready(function() {
    $('#id_idAlimento').attr('readonly','readonly');
    $('#id_idAccesorio').attr('readonly','readonly');   
    $('#id_idProducto_limpieza').attr('readonly','readonly');   
    $('#id_idProducto_peluqueria').attr('readonly','readonly');      
    
    $('#texto_buscado').on('keyup', function() {
        var texto = $(this).val().toLowerCase();
        $('#tabla_productos tr').filter (function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(texto) > -1)
        });
    });
});