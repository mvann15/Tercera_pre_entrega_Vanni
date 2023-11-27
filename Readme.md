Nombre del Proyecto

AppEscuelita (es una aplicación desarrollada para una academia deportiva y permite la gestión de los cursos, sus materias y profesores así como también los eventos que se desarrollen en ella)

_Tabla de Contenidos.

1-Instalación

2-Uso

3-Licencia




1- Instalación

Para instalar la App será necesario contar con un terminal Bash para clonar el siguente link https://github.com/mvann15/Tercera_pre_entrega_Vanni.git. En el terminal Bash ejecutar el comando 'cd' para moverse a la ruta donde se guardará la App. Una vez elegida la ruta ejecutar 'git clone https://github.com/mvann15/Tercera_pre_entrega_Vanni.git', esto descargará la App para ser instalada.
Ya descargada será necesario contar con un ID como Pycharm, ya en el ID seleccionar Open dentro del menú y moverse hasta la ruta donde fue descargada la App. Hacer click en Ok. Una vez abierto es recomendable agregar un nuevo entorno virtual. Si este es el caso se deberá instalar Django en dicho entorno, para esto, en el terminal del Id ejecutar el comando 'pip install django', y ejecutar las migraciones con el comando 'python manage.py migrate' (si se realizan cambios en los modelos ejecutar 'python manage.py makemigrations' para que los mismos se  guarden y volver a ejecutar 'python manage.py migrate'). A continuación cofigurar manage (seleccionar la opción módulo-runserver) y generar un usuario para acceder al panel admin de la App ejecutando el comando 'python manage.py createsuperuser'. Ya es posible ejecutar la App desde manage (cuando lo hagas, haz click en la url que aparecerá en el terminal, para que la App abra en tu navegador).

2-Uso

La App consta de 3 modelos, Deporte, Profesor y Materia, y al ejecutarla se podrá acceder al inicio de la página desde cualquiera de estas urls (http://127.0.0.1:8000/app/show, http://127.0.0.1:8000/app/deportes, http://127.0.0.1:8000/app/profesores, http://127.0.0.1:8000/app/materias).Una vez que accedas, podrás navegar por los botones Deportes, Profeores y Materias (si quieres que se carguen los formularios de búsqueda), o por los botones Crear_Deporte, Crear_Profesor y Crear_Materia si lo que deseas es agregar nuevos datos mediante los formularios de carga.

3-Licencia

La App no se encuentra registrada y puedes hacer uso indiscriminado de ella hasta que me de cuenta. Enjoy.

