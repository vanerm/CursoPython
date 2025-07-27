# AppCoder - Proyecto Django

## Descripción

AppCoder es una aplicación web basada en Django para la gestión de cursos, alumnos y profesores.  
Fue desarrollada como parte de la materia de Python de la Diplomatura de Data Science en [Coder House](https://www.coderhouse.com/).

## Funcionalidades

- **Pagina de Inicio**
  - Información general sobre la aplicación
  - Formulario de suscripcion de [Start Bootstrap](https://startbootstrap.com)
  - Si el usuario no está autenticado, se muestra la página de inicio general
  - Si el usuario está autenticado, se muestra la página de inicio personalizada con su nombre y avatar con las iniciales del mismo y acceso al resto de la aplicación (cursos,profesores y alumnos)

  - **Perfil de Usuario**
  - Si el usuario está autenticado, puede editar su email y cerrar sesión desde su perfil personalizado.
  - Avatar con las iniciales de su nombre generado con la API de [UI Avatars](https://ui-avatars.com/)
  - Permisos de administración para listar, buscar, editar y eliminar cursos, alumnos y profesores. 

- **Login, Logout & Registro de Usuarios**
  - Iniciar sesión
  - Cerrar sesión
  - Registro de usuarios
  - Editar perfil de usuarios

- **Gestión de Cursos**
  - Listar todos los cursos
  - Agregar nuevos cursos
  - Buscar cursos por nombre
  - Editar cursos existentes
  - Eliminar cursos existentes

- **Gestión de Alumnos**
  - Listar todos los alumnos
  - Agregar nuevos alumnos
  - Buscar alumnos por nombre
  - Editar alumnos existentes
  - Eliminar alumnos existentes

- **Gestión de Profesores**
  - Listar todos los profesores
  - Agregar nuevos profesores
  - Buscar profesores por nombre
  - Editar profesores existentes
  - Eliminar profesores existentes

- **Formulario de Contacto**
  - Los usuarios pueden enviar consultas a través de un formulario

- **Navigation Bar**
  - Barra de navegación con enlaces a la home, secciones principales y perfil de usuario dependiendo si el usuario está autenticado o no

- **Footer**
  - Información de contacto y redes sociales

- **Diseño Responsivo**
  - Interfaz moderna y adaptable usando Bootstrap
  - Tema oscuro con contraste accesible

- **Botón flotante de WhatsApp**
  - Acceso rápido a WhatsApp para consultas

- **Mensajes de éxito**
  - SnackBar de mensajes de éxito al finalizar operaciones exitosas

- **Página 404 Not Found**  
  - Página 404 not found para manejar errores de ruta no encontrada 
  - Animación de [Lottie](https://app.lottiefiles.com/)
  - Botones para regresar al inicio o contactar al administrador a través del formulario de contacto

## Créditos

Este proyecto fue desarrollado como parte de la materia de Python de la Diplomatura de Data Science en [Coder House](https://www.coderhouse.com/)