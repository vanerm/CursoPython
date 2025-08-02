# AppCoder - Proyecto Django

## 📋 Descripción

AppCoder es una aplicación web basada en Django para la gestión de cursos, alumnos y profesores.  
Fue desarrollada como parte de la materia de Python de la Diplomatura de Data Science en [Coder House](https://www.coderhouse.com/).

## 🎥 Evidencia
[App Coder](https://drive.google.com/file/d/17egvA7ELSF8jHT6y4vwKYcs4KMTPVdMV/view?usp=sharing)

## 🚀 Instalación y Configuración

### Requisitos previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/vanerm/CursoPython.git
   cd CursoPython/Clase18
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar migraciones:**
   ```bash
   python manage.py migrate
   ```

4. **Crear superusuario (opcional):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Ejecutar el servidor:**
   ```bash
   python manage.py runserver
   ```

6. **Acceder a la aplicación:**
   - Abrir http://127.0.0.1:8000 en el navegador

## ✨ Funcionalidades

### **🏠 Página de Inicio**
- Formulario de suscripción de [Start Bootstrap](https://startbootstrap.com)
- Contenido dinámico según el estado de autenticación del usuario
- Carrousel de cursos
- Sección de Información General sobre la aplicación
- Sección de Testimonios
- Sección de Partners

### **🧭 Navigation Bar**
- Barra de navegación adaptativa según el estado de autenticación
- Enlaces a las secciones principales
- Acceso rápido al perfil de usuario
- Avatar personalizado si existe
- Iniciales como fallback si no hay avatar

### **👤 Perfil de Usuario**
- Edición de email y contraseña
- Avatar personalizado con iniciales generado por [UI Avatars](https://ui-avatars.com/)
- Campo de subida de archivos para avatares
- Validación de imágenes (solo acepta archivos de imagen)
- Permisos de administración para gestionar cursos, alumnos y profesores

### **🔐 Autenticación de Usuarios**
- Sistema de login/logout
- Registro de nuevos usuarios
- Edición de perfiles de usuarios
- Mensajes de feedback para todas las operaciones

### **📚 Gestión de Cursos**
- Listado completo de cursos
- Agregar nuevos cursos
- Búsqueda por nombre
- Edición de cursos existentes
- Eliminación de cursos

### **👨‍🎓 Gestión de Alumnos**
- Listado completo de alumnos
- Agregar nuevos alumnos
- Búsqueda por nombre
- Edición de alumnos existentes
- Eliminación de alumnos

### **👨‍🏫 Gestión de Profesores**
- Listado completo de profesores
- Agregar nuevos profesores
- Búsqueda por nombre
- Edición de profesores existentes
- Eliminación de profesores

### **📞 Formulario de Contacto**
- Envío de consultas a través de formulario web
- **Validación en tiempo real** con JavaScript (campos requeridos y formato de email)
- **Botón de envío dinámico** (se habilita solo cuando todos los campos son válidos)
- **Procesamiento del backend** con Django y validación del servidor
- **Mensajes de éxito** usando el framework de mensajes de Django
- **Redirección automática** a la página de inicio después del envío exitoso

### **🎨 Diseño y UX**
- **Diseño responsivo** con Bootstrap
- **Tema oscuro** con contraste accesible
- **Botón flotante de WhatsApp** para consultas rápidas
- **SnackBar de mensajes** de éxito al finalizar operaciones
- **Página 404 personalizada** con animación de [Lottie](https://app.lottiefiles.com/)

## 🛠️ Configuración de Archivos Estáticos

Este proyecto usa archivos estáticos (CSS, JS, imágenes) ubicados en `AppCoder/static/AppCoder/`.

### Para desarrollo (`DEBUG = True`):
Los archivos estáticos se sirven automáticamente por Django.

### Para producción (`DEBUG = False`):
1. **Ejecutar el comando de recolección:**
   ```bash
   python manage.py collectstatic
   ```

2. **Configurar servidor web:**
   - Los archivos se recopilan en la carpeta `staticfiles/`
   - En producción, usar Nginx o Apache para servir `/static/`

### ⚠️ Nota importante:
El servidor de desarrollo de Django (`python manage.py runserver`) **no está pensado para servir archivos estáticos con `DEBUG = False`**. Si el CSS no se carga correctamente en este modo, es un comportamiento esperado.

## 🛡️ Seguridad

- **Autenticación requerida** para operaciones de administración
- **Validación de formularios** tanto en frontend como backend
- **Tokens CSRF** para protección contra ataques
- **Validación de datos** en todas las operaciones

## 📱 Tecnologías Utilizadas

- **Backend:** Django 5.2.3
- **Frontend:** HTML5, CSS3, JavaScript
- **Framework CSS:** Bootstrap 5
- **Base de datos:** SQLite
- **APIs externas:** Start Bootstrap Forms, UI Avatars, Lottie

## 🤝 Contribución

Este es un proyecto educativo desarrollado como parte del curso de Python en Coder House.

## 📄 Licencia

Este proyecto es de uso educativo.

## 👨‍💻 Autor

Desarrollado como parte de la materia de Python de la Diplomatura de Data Science en [Coder House](https://www.coderhouse.com/).

## 👋 About Me

¡Hola! Soy **Vanesa Mizrahi**, desarrolladora mobile iOS y apasionada por los datos y el aprendizaje continuo.

### 🔗 Conecta conmigo
- **LinkedIn:** [Vanesa Mizrahi](https://www.linkedin.com/in/vanesamizrahi/)

### 💡 Sobre este proyecto
Este proyecto fue desarrollado como parte de mi formación en **Data Science** en Coder House, donde aprendí a crear aplicaciones web completas con Django, desde la concepción hasta el despliegue.

¡Gracias por revisar mi trabajo! 🚀