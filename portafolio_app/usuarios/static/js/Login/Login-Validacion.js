
//función que valida un formulario INGRESO
$(function(){
    $("#datos").validate({
        rules:{
            correo:{
                required:true,
                email:true
            },
            pass:{
                required:true
            }
        },//rules
        messages:{

            correo:{
                required:'Ingrese correo de usuario',
                email: 'Formato de correo inválido'
            },
            pass:{
                required:'Ingrese contraseña',
                minlength:'Caracteres insuficientes(8)',
                maxlength:'Excedes los (16) caracteres'
            }


        },//messages                
    })
});


//AVISO DE CONFIRMACION AL ENVIAR FORMULARIO CREAR CONTRASEÑA

document.getElementById('datos').addEventListener('#ingresar', function(event) {
    event.preventDefault(); // Evitar el envío de formulario por defecto

    // Realizar la validación del formulario aquí
    var form = document.getElementById('datos');
    if (form.checkValidity()) {
        // Redireccionar a otra página
        window.location.href = 'patitas.html';
    }
});


$(function() {
    $("#recupera").validate({
        rules: {
            correo_recu: {
                required: true,
                email: true
            }
        },
        messages: {
            correo_recu: {
                required: 'Ingrese correo de usuario',
                email: 'Formato de correo inválido'
            }
        }
    });

});

//AVISO DE CONFIRMACION AL ENVIAR FORMULARIO DE CONTACTO
function mostrarToast() {
    var form = document.getElementById('#recupera');
    if (form.checkValidity()) {
        var toast = new bootstrap.Toast(document.getElementById('toastRec'));
        toast.show();
    }
}

var form = document.getElementById('#recupera');
form.addEventListener('#enviaRecu', function (event) {
    event.preventDefault(); // Evitar el envío del formulario
    mostrarToast();
});