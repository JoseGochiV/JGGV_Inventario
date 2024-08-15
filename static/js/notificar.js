$(document).ready(function() {
    // Manejo de formularios en general
    $("form").on("submit", function(event) {
        event.preventDefault();  // Evita el envío del formulario de forma predeterminada
        
        var form = $(this);  // Captura el contexto del formulario
        var formAction = form.attr("action");

        console.log("Formulario enviado a: " + formAction);  // Verifica la URL

        // Recoge los datos del formulario
        var formData = form.serialize();

        // Enviar los datos a través de AJAX
        $.ajax({
            type: "POST",
            url: formAction,  // URL del formulario
            data: formData,
            success: function(response) {
                // Maneja la respuesta del servidor
                alert("Los datos han sido guardados exitosamente");

                // Redirige basado en la URL del formulario
                if (formAction.includes("/materialactualizar")) {
                    // Si la URL de acción incluye "/materialactualizar", es una actualización de material
                    window.location.href = "/listamateriales";  // Página de lista de materiales después de actualizar

                } else if (formAction === "/usuarios") {
                    // Si la URL de acción es "/usuarios", es una inserción 
                    window.location.href = "/listar";  // Página de listar usuarios

                } else if (formAction === "/materiales") {
                    // Si la URL de acción es "/materiales", es una inserción de material
                    window.location.href = "/listamateriales";  // Página de listar materiales
                    
                } else if (formAction.includes("/usuariosactualizar")) {
                    // Si la URL de acción incluye "/usuariosactualizar", es una actualización de usuario
                    window.location.href = "/listar";  // Página de listar usuarios
                }
            },
            error: function(xhr, status, error) {
                // Maneja los errores
                alert("Hubo un error al guardar los datos: " + error);
            }
        });
    });
});
