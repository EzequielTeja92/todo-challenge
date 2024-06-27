# Task Management API

Esta es una API que proporciona información sobre tareas y etiquetas. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en los registros de tareas y etiquetas.

## Requisitos
- Python 3.9 o superior (Se recomienda Python 3.9 o superior)
- Pipenv
- Servidor de base de datos PostgreSQL (instalado localmente o usando Docker)

## Configuración del Entorno

1. Clonar el repositorio:

   ```shell
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. Instalar las dependencias usando Pipenv. Esto creará un entorno virtual e instalará las dependencias especificadas en el Pipfile:

  ```shell
  pipenv install
  ```
**Nota**
Si Pipenv usa la versión incorrecta de Python, asegúrate de tener la versión adecuada de Python instalada y configurada en tu sistema antes de ejecutar el comando pipenv install.

3. Activar el entorno virtual:

shell
   ```shell
  pipenv shell
  ```

4. Configurar la base de datos PostgreSQL:

  ### Si tienes un servidor PostgreSQL local:
    Crea una base de datos con el nombre todochallenge (o cualquier nombre de tu elección).

Actualiza la configuración de la base de datos en el archivo .env con tus credenciales de PostgreSQL:

  ```python
  DB_USER=tu-usuario-postgres
  DB_PASSWORD=tu-contraseña-postgres
  DB_NAME=todochallenge
  DB_HOST=localhost
  DB_PORT=5432
  ```

  ### Si prefieres usar Docker para ejecutar el proyecto:
  Asegúrate de tener Docker instalado y en ejecución en tu sistema, luego ejecuta el comando:
  ```docker
  docker-compose up -d --build
  ```

5. Ejecutar las migraciones de la base de datos:

```shell
python manage.py migrate
``` 
Iniciar el servidor:

```shell
python manage.py runserver
```
## Endpoints

### Obtener token de acceso:

* POST /api/token/

```json
body:
{
  "username": "your_username",
  "password": "your_password"
}
```
### Refrescar token de acceso:

*POST /api/token/refresh/

```json
Body:
{
  "refresh": "your_refresh_token"
}
```

### Listar y crear tareas:

* GET /api/tasks/
* POST /api/tasks/

### Obtener, actualizar y eliminar una tarea específica:

* GET /api/tasks/{id}/
* PUT /api/tasks/{id}/
* DELETE /api/tasks/{id}/

### Listar y crear etiquetas:

* GET /api/labels/
* POST /api/labels/

### btener, actualizar y eliminar una etiqueta específica:

* GET /api/labels/{id}/
* PUT /api/labels/{id}/
* DELETE /api/labels/{id}/


# Credenciales de BackOffice:
```shell
usuario: admin
contraseña: admin
```