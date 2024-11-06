$(document).ready(function() {
    $('.card').click(function() {
      // Recupera la información de la tarjeta seleccionada
      var infoType = $(this).data('info');
      $('#infoModalLabel').text(infoType);  // Establece el título del modal de información
  
      // Aquí se decide qué texto mostrar basado en la tarjeta seleccionada
      var content = "";
      switch (infoType) {
        case 'Horario de atención':
          content = "Nuestro horario de atención es de lunes a viernes de 9:00 a 18:00.";
          break;
        case 'Precios':
          content = "Nuestros precios varían según el diseño y tamaño del tatuaje.";
          break;
        case 'Cuidados del tatuaje':
          content = "Es importante cuidar tu tatuaje, manteniéndolo limpio y hidratado.";
          break;
        case 'Certificados de higiene':
          content = "Contamos con todos los certificados de higiene y salud requeridos.";
          break;
        default:
          content = "Información no disponible.";
      }
  
      // Establece el texto del modal de información
      $('#infoText').text(content);
    });
  });
  