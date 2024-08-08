$(document).ready(function() {
    // Manejo de formularios en general
    $("form").on("submit", function(event) {
        event.preventDefault();  // Evita el envío del formulario de forma predeterminada
        
        var form = $(this);  // Captura el contexto del formulario

        // Recoge los datos del formulario
        var formData = form.serialize();

        // Enviar los datos a través de AJAX
        $.ajax({
            type: "POST",
            url: form.attr("action"),  // URL del formulario
            data: formData,
            success: function(response) {
                // Maneja la respuesta del servidor
                alert("Los datos han sido guardados exitosamente");

                // Redirige a la página de listar usuarios o materiales
                if (form.attr("action") === "/usuarios") {
                    window.location.href = "/listar";  // Página de listar usuarios
                } else if (form.attr("action") === "/materiales") {
                    window.location.href = "/listamateriales";  // Página de listar materiales
                }
            },
            error: function(xhr, status, error) {
                // Maneja los errores
                alert("Hubo un error al guardar los datos: " + error);
            }
        });
    });
});
