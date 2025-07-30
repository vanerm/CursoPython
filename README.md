# AppCoder - Proyecto Django

## Descripción

AppCoder es una aplicación web basada en Django para la gestión de cursos, alumnos y profesores.  
Fue desarrollada como parte de la materia de Python de la Diplomatura de Data Science en [Coder House](https://www.coderhouse.com/).

## Evidencia
[App Coder](https://drive.google.com/file/d/17nL4Xflm00BKB2R6sz0Z98-7sjbjc0lT/view?usp=sharing)

## Funcionalidades

- **Pagina de Inicio**
  - Formulario de suscripción de [Start Bootstrap](https://startbootstrap.com)
  - Si el usuario no está autenticado, se muestra la página de inicio general
  - Si el usuario está autenticado, se muestra la página de inicio personalizada con su nombre y avatar con las iniciales del mismo y acceso al resto de la aplicación (cursos,profesores y alumnos)
  - Carrousel de cursos
  - Sección de Información General sobre la aplicación
  - Sección de Testimonios
  - Sección de Partners

- **Navigation Bar**
  - Barra de navegación con enlaces a la home, secciones principales y perfil de usuario dependiendo si el usuario está autenticado o no  

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

- **Footer**
  - Información de contacto y redes sociales

- **Formulario de Contacto**
  - Los usuarios pueden enviar consultas a través de un formulario

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

## 🛠️ Archivos estáticos y modo producción

Este proyecto usa archivos estáticos (CSS, JS, imágenes) ubicados en `AppCoder/static/AppCoder/`.

Para servir estos archivos correctamente cuando `DEBUG = False` (modo producción), primero ejecutar el siguiente comando:

```bash
python manage.py collectstatic
```

Esto recopilará todos los archivos estáticos en la carpeta `staticfiles/`, desde donde deben ser servidos en producción.

**IMPORTANTE:**  
El servidor de desarrollo de Django (`python manage.py runserver`) **no está pensado para servir archivos estáticos con `DEBUG = False`**. Aunque existe una configuración temporal en `urls.py` para pruebas locales, puede fallar al recargar la página (por ejemplo, usando Ctrl+Shift+R o Cmd+Shift+R) y no es confiable para producción real.

- Durante el desarrollo, mantener `DEBUG = True` para evitar problemas con los archivos estáticos.
- Usar `DEBUG = False` solo para probar páginas de error personalizadas (como la 404).
- En un entorno de producción real, los archivos estáticos deben ser servidos por un servidor web como Nginx o Apache, no por Django.

**Resumen:**  
- Si el CSS o los archivos estáticos no se cargan correctamente con `DEBUG = False` usando el servidor de desarrollo, es un comportamiento esperado y no un error del código.

## Créditos

Este proyecto fue desarrollado como parte de la materia de Python de la Diplomatura de Data Science en [Coder House](https://www.coderhouse.com/)