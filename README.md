# Projecto 2 - Bases de Datos 2

## ¿Cómo inicializar el projecto?

1. [Crea un fork de este repositorio](https://github.com/dialvarezs/db2-api-project/fork)
2. Clona el repositorio forkeado desde Visual Studio Code

   ![Clonar](docs/vscode_clone1.png)
3. Instala las dependencias del proyecto con PDM
   ```shell
   pdm install
   ```
4. Crea el archivo `.env` en la raíz del proyecto desde el ejemplo `env.example`
   ```shell
   cp env.example .env
   ```
   Configura la variable `DATABASE_URL` con la URL de la base de datos que desees utilizar (recordar que debe conservar
   el formato `postgresql+psycopg:///<mi_bd>`).
5. Crea la base de datos en postgresql.
   ```shell
   createdb <mi_bd>
   ```
   **NOTA:** En WSL podría ser necesario iniciar antes el servicio de postgres con `sudo service postgresql start`.
6. Ejecuta las migraciones
   ```shell
   pdm shell
   alembic upgrade head
   ```
7. Ejecuta el servidor de desarrollo
   ```shell
   pdm start
   ```

## ¿Cómo trabajar en el proyecto?

Por regla general el prodedimiento para realizar modificaciones a partir desde el modelo de datos es el siguiente:

1. Crear modificaciones en los modelos (`app/models.py`).
2. Crear una nueva migración con alembic
   ```shell
   pdm shell
   alembic revision --autogenerate -m "Descripción de la modificación"
   ```
3. Revisar la migración creada en `migrations/versions` y verificar que sea correcta.
   Se puede revisar también el código SQL de la migración ejecutando:
    ```shell
    alembic upgrade --sql head
    ```
4. Ejecutar la migración
   ```shell
   alembic upgrade head
   ``` 
5. Crear al menos una DTO para lectura en `app/dtos.py`.
6. Crear un repositorio para el nuevo modelo en `app/repositories.py`.
7. Crear un nuevo controlador en `app/controllers.py`.