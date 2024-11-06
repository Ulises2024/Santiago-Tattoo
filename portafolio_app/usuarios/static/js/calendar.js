// Function to format date to MM/DD/YYYY
function formatDate(dateStr) {
    const date = new Date(dateStr);
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    const year = date.getFullYear();
    return `${month}/${day}/${year}`;
}

// Function to format time to HH:MM AM/PM
function formatTime(timeStr) {
    const [hour, minute, second] = timeStr.split(':');
    let hours = parseInt(hour);
    const suffix = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12 || 12;
    return `${hours}:${minute} ${suffix}`;
}

document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the JSON data from the script tag
    const citaJsonData = document.getElementById('cita-json-data').textContent;

    // Parse the JSON data
    const citas = JSON.parse(citaJsonData);

    // Convert to the desired format
    const events = citas.map(cita => ({
        id: cita.pk,
        title: cita.fields.eventTitle,
        start: `${cita.fields.eventStartDate}T${cita.fields.eventStartTime}`,
        end: `${cita.fields.eventEndDate}T${cita.fields.eventEndTime}`,
        url: "#", // Placeholder, adjust if you have this info
        extendedProps: {
            location: "INK MASTERY STUDIO", // Placeholder, adjust if you have this info
            tatuador: cita.tatuador,
            timeStart: formatTime(cita.fields.eventStartTime),
            timeEnd: formatTime(cita.fields.eventEndTime),
            description: cita.fields.descripcion
        }
    }));

    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: events, // Directly pass the events array
        eventClick: function(info) {
            showDeleteModal(info.event.id, info.el);
        },
        
        eventContent: function(info) {
            return {
                html: `
                <div style="overflow: hidden; font-size: 12px; position: relative; cursor: pointer; font-family: 'Inter', sans-serif;">
                    <div><strong>${info.event.title}</strong></div>
                    <div>Location: ${info.event.extendedProps.location}</div>
                    <div>Id: ${info.event.id}</div>
                    <div>Date: ${info.event.start.toLocaleDateString("es-US", {month: "long", day: "numeric", year: "numeric"})}</div>
                    <div>Time: ${info.event.extendedProps.timeStart} - ${info.event.extendedProps.timeEnd}</div>
                    <button type="button" class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" data-id="${info.event.id}" onclick="showDeleteModal(event, this)"><i class="bi bi-trash"></i>Eliminar</button>
                    <button type="button" class="btn btn-warning btn-sm" data-bs-toggle="modal" data-bs-target="#editModal" data-id="${info.event.id}" onclick="showEditModal(event, this)"><i class="bi bi-pencil"></i>Editar</button>
                </div>
                `
            };
        }
    });
    calendar.render();
});

function addEvent() {
    const form = document.getElementById('createCitaForm');
    const formData = new FormData(form);

    fetch('/create_cita/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': formData.get('csrfmiddlewaretoken')
        }
    }).then(response => {
        if (response.ok) {
            response.json().then(data => {
                // Optionally reload or update the calendar
                location.reload();
            });
        } else {
            console.error('Failed to create event.');
        }
    }).catch(error => {
        console.error('Error:', error);
    });
}

function showDeleteModal(event, button) {
    // Obtener el ID del evento desde el atributo data-id
    const eventId = button.getAttribute('data-id');
    
    // Loguear el ID del evento
    console.log("ID del evento:", eventId);
    
    // Verificar si eventId es null o undefined
    if (!eventId) {
        console.error("No se pudo obtener el ID del evento.");
        return;
    }
    
    // Actualizar el contenido del modal con el ID del evento
    const modalBody = document.querySelector('#deleteModal .modal-body');
    modalBody.textContent = `¿Estás seguro de que deseas eliminar el evento con ID ${eventId}?`;
    
    // Establecer el ID del evento en el botón de confirmación de eliminación
    const confirmButton = document.querySelector('#confirmDeleteButton');
    confirmButton.setAttribute('data-id', eventId);
}

function deleteEvent(button) {
    // Obtener el ID del evento desde el atributo data-id
    const eventId = button.getAttribute('data-id');
    
    // Verificar si eventId es null o undefined
    if (!eventId) {
        console.error("No se pudo obtener el ID del evento para eliminar.");
        return;
    }
    
    // Loguear el ID del evento para verificación
    console.log("ID del evento para eliminar:", eventId);
    
    // Redirigir a la ruta de eliminación con el ID del evento
    const url = `http://localhost:8000/calendar/eliminar_cita/${eventId}/`;
    window.location.href = url;
}


function showEditModal(event, button) {
    // Obtener el ID del evento desde el atributo data-id
    const eventId = button.getAttribute('data-id');
    
    // Loguear el ID del evento
    console.log("ID del evento:", eventId);
    
    // Verificar si eventId es null o undefined
    if (!eventId) {
        console.error("No se pudo obtener el ID del evento.");
        return;
    }
    
    // Actualizar el contenido del modal con el ID del evento
    const modalBody = document.querySelector('#editModal .modal-body');
    modalBody.textContent = `¿Estás seguro de que deseas editar el evento con ID ${eventId}?`;
    
    // Establecer el ID del evento en el botón de confirmación de edición
    const confirmButton = document.querySelector('#confirmEditButton');
    confirmButton.setAttribute('data-id', eventId);
}

function editEvent(button) {
    // Obtener el ID del evento desde el atributo data-id
    const eventId = button.getAttribute('data-id');
    
    // Verificar si eventId es null o undefined
    if (!eventId) {
        console.error("No se pudo obtener el ID del evento para editar.");
        return;
    }
    
    // Loguear el ID del evento para verificación
    console.log("ID del evento para editar:", eventId);
    
    // Redirigir a la ruta de edición con el ID del evento
    const url = `http://localhost:8000/calendar/editar_cita/${eventId}/`;
    window.location.href = url;
}





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







// function confirmDeleteEvent() {
//     var eventId = window.currentEventIdToDelete;
//     deleteEvent(eventId);
//     var modal = bootstrap.Modal.getInstance(document.getElementById('deleteModal'));
//     modal.hide();
// }

