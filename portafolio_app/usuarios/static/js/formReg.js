// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()


// Obtener el formulario
var form = document.getElementById('form1');

// Obtener los campos de entrada por sus ids
var nombre = document.getElementById('nombre');
var apellidoPat = document.getElementById('apellidoPat');
var apellidoMat = document.getElementById('apellidoMat');
var rut = document.getElementById('rut');
var correo = document.getElementById('correo');
var telefono = document.getElementById('telefono');
var direccion = document.getElementById('direccion');
var usuario = document.getElementById('usuario');
var pass1 = document.getElementById('pass1');
var pass2 = document.getElementById('pass2');

// Agregar un escuchador de eventos para el evento 'input' en cada campo de entrada
nombre.addEventListener('input', validarCampo);
apellidoPat.addEventListener('input', validarCampo);
apellidoMat.addEventListener('input', validarCampo);
rut.addEventListener('input', validarCampo);
correo.addEventListener('input', validarCampo);
telefono.addEventListener('input', validarCampo);
direccion.addEventListener('input', validarCampo);
usuario.addEventListener('input', validarCampo);
pass1.addEventListener('input', validarCampo);
pass2.addEventListener('input', validarCampo);

// Función para validar un campo de entrada
function validarCampo(event) {
  var input = event.target;

  if (input === pass2) {
    if (pass2.value !== pass1.value) {
      input.classList.remove('is-valid');
      input.classList.add('is-invalid');
      return;
    }
  }

  if (input.checkValidity()) {
    input.classList.remove('is-invalid');
    input.classList.add('is-valid');
  } else {
    input.classList.remove('is-valid');
    input.classList.add('is-invalid');
  }
}

// Agregar un escuchador de eventos para el evento 'submit' en el formulario
form.addEventListener('submit', function(event) {
  // Verificar si el formulario es válido
  if (!form.checkValidity()) {
    event.preventDefault();
    event.stopPropagation();
  } else {
    // Redirigir a la página "patitas.html"
    window.location.href = './patitas.html';
  }

  form.classList.add('was-validated');
});

