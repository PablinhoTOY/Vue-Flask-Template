## Boilerplate VITE VUE + FLASK

## Configuracion de FLASK

Estos son los pasos y comandos que debes correr al momento de clonar el proyecto

Sobre la carpeta /be
- Crear un virtual Enviorement en la raiz de la ruta con el comando **py -m venv nombre_del_venv**
- Situarse sobre la ruta del Virtual Enviorement con el comando **venv/Scripts/activate**
- Instalar las dependencias del proyecto Flask con el comando **pip install -r req.txt**
- Correr el comando **py app.py** para iniciar el proyecto Flask
  
Ya se debería tener el Flask corriendo  (normalmente por el puerto 5000 => http://localhost:5000).

## Configuracion de FLASK
Sobre la carpeta /be y con el venv activo
- De ser necesario, borrar la carpeta migrations (solo si no te corre la migracion bien)
- Correr el comando **flask db init** para preparar la migracion.
- Correr el comando **flask db migrate** para correr la migracion
- Correr el comando **flask db upgrade** para actualizacion los datos migrados.

## Configuracion del Front (vue js)

Estos son los pasos y comandos que debes correr al momento de clonar el proyecto

Sobre la carpeta /fe
- Correr el comando **npm i** para instalar todas las dependencias node modules.
- Correr el comando **npm run dev** para preparar los componentes vue js y permanecer escuchando los cambios sobre los componentes vue js

Ya se debería tener el vue JS configurado y ejecutando (normalmente por el puerto 8080 => http://localhost:8080).


## Licencia

MIT

### Problemas comunes
- No se puede ejecutar python en powershell.
- <img width="655" alt="Captura de pantalla 2023-08-02 a la(s) 1 45 52 p  m" src="https://github.com/Departamento-Web-y-Multimedia-UTP/CarnetUTP/assets/36899684/ccc10703-4a6a-4883-8463-3a4c04c16cb5">

  Si no puedes activar el Enviorement del Python debes ejecutar lo siguiente en el Powershell, Después de usar esos dos comandos solo debes utilizar en la terminal de visual code lo siguiente:
    ./actívate
