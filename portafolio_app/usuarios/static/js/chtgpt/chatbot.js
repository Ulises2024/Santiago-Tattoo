function sendMessage() {
    var message = document.getElementById('userInput').value;
    document.getElementById('userInput').value = ''; // Limpiar el campo de entrada
  
    // Añadir el mensaje del usuario al chat
    var chatList = document.getElementById('chatList');
    var userMessageElement = document.createElement('li');
    userMessageElement.classList.add('list-group-item', 'text-end');
    userMessageElement.textContent = message;
    chatList.appendChild(userMessageElement);
  
    // Enviar mensaje al servidor
    fetch('/usuarios/chatbot/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')  // Asegúrate de manejar CSRF si es necesario
      },
      body: JSON.stringify({ message: message })
    }).then(response => response.json())
      .then(data => {
        var botMessageElement = document.createElement('li');
        botMessageElement.classList.add('list-group-item');
        botMessageElement.textContent = data.response;
        chatList.appendChild(botMessageElement);
      });
  }
  
  // Función para obtener el cookie CSRF de Django
  function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }
  