# comision-78130
Repositorio de la comisión 78130 Python Flex
comision-78130_TPFinal_Calarame -->  AppGym
ultimo modificado --> 06/11/25 19 hs

// pendientes para prox version

FALTA - Uso de mínimo un mixin en una CBV y un decorador en una view común.
FALTA - Tener una app (accounts/cuentas/etc) para el manejo de todas las vistas relacionadas al usuario/autenticación.
FALTA - Desarrollar las vistas para un login, un logout y un registro para usuarios. En este último se debe solicitar: username, email, password.
FALTA Crear una vista de perfil donde se muestran los datos del usuario:
FALTA Desde el perfil, crear un acceso a una vista de edición de estos datos. Agregar el cambio de password.

FALTA - Video de máximo 10 min que muestre la página y sus funcionalidades (con o sin audio)


-------------------- crear repositorio Git
En GitHub, crear repositorio, agregar nombre y descripcion, luego readme on, publico, ignore file = Phyton
https://github.com/caldatjp/TuPrimeraPagina_Calarame.git
crear carpeta del proyecto
sobre la misma abrir git bash
y escribir git clone https://github.com/caldatjp/TuPrimeraPagina_Calarame.git .
abrir visual studio code desde esa ubicacion

-------------------- crear entorno virtual
desde vsc, escribir en proyecto: python -m venv entorno_virtual
Importante: si tira error, activar la directiva de seguridad desde powershell como administrador
	Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
activar entorno: entorno_virtual/Scripts/activate
en el file gitignore, agregar al final entorno_virtual
pip freeze > requirements.txt

-------------------- instalacion django
instalar django --> pip install django
para verificar instalacion y version ejecutar : django-admin --version

-------------------- instalar base de datos sqllite viewer
buscar en extensiones --> SQLLite Viewer --> instalar
instalar DB Browser SQLite para adm la BD --> https://sqlitebrowser.org/

-------------------- creacion de proyecto y apps
django-admin startproject proyecto_gymcoder .
django startapp appgym
ir a proyecto_coder, file settings, agregar "proyecto_gymcoder" en seccion "Installed Apps"
crear en app appgym, el file urls.py
crear en app appgym, la carpeta template, y dentro de esta carpeta appgym
crear en template/coder --> file index.html
setear en urls.py de proyecto_coder --> urlpatterns

-------------------- levantar servidor
ejecutar en la raiz del proyecto comando --> python manage.py runserver
verificar en http://127.0.0.1:8000/

--------------------- levantar estructuras de base de datos 
una vez creada la estructura de tabla
ejecutar
python manage.py makemigrations
python manage.py migrate

--------------------- seteo de admin // usuario y pass
python manage.py createsuperuser
user: caldatjp
email: caldatjp@gmail.com
pass: admin123
http://127.0.0.1:8000/admin/


------------------- actualizacion de proyecto en GitHub
verificar el repositorio al que esta apuntando
git remote -v
origin  https://github.com/caldatjp/comision-78130_TPFinal_GymCoder.git (fetch)
origin  https://github.com/caldatjp/comision-78130_TPFinal_GymCoder.git (push)

forzar la actualizacion completa a git
git status
git add .
git commit -m "Subida TPFinal AppGym // version completa sin accounts"
git push -u origin main
git push origin main --force


-------------------- manejo bloque accounts
agregado de pillow
pip install Pillow


-------------------- estructura del sitio
/mi_proyecto/
│
├─ manage.py
├─ mi_proyecto/
│   ├─ __init__.py
│   ├─ settings.py
│   ├─ urls.py
│   ├─ wsgi.py
│   └─ asgi.py
│
├─ appgym/
│   ├─ migrations/
│   │    └─ __init__.py
│   ├─ __init__.py
│   ├─ admin.py
│   ├─ apps.py
│   ├─ forms.py
│   ├─ models.py
│   ├─ tests.py
│   ├─ urls.py
│   ├─ views.py
│   └─ templates/
│        └─ appgym/
│             ├─ index.html
│             ├─ socio_list.html
│             ├─ socio_form.html
│             ├─ socio_visualizar.html
│             ├─ instructor_list.html
│             ├─ instructor_form.html
│             ├─ instructor_visualizar.html
│             ├─ clase_list.html
│             ├─ clase_form.html
│             ├─ clase_visualizar.html
│             └─ …otros
│
├─ equipamiento/
│   ├─ migrations/
│   │    └─ __init__.py
│   ├─ __init__.py
│   ├─ admin.py
│   ├─ apps.py
│   ├─ forms.py
│   ├─ models.py
│   ├─ tests.py
│   ├─ urls.py
│   ├─ views.py
│   └─ templates/
│        └─ equipamiento/
│             ├─ equipamiento_list.html
│             ├─ equipamiento_form.html
│             ├─ equipamiento_detail.html
│             └─ …otros

------------- modelo de datos (UML)

+---------------------------+
| Socio                    |
+---------------------------+
| socio_id : Integer PK     |
| socio_nombre : Char       |
| socio_apellido : Char     |
| socio_docnro : Char       |
| socio_fecnacimiento : Date|
| socio_fecalta : Date      |
| socio_fecbaja : Date      |
+---------------------------+

+---------------------------+
| Instructor               |
+---------------------------+
| inst_id : Integer PK      |
| inst_nombre : Char        |
| inst_apellido : Char      |
| inst_sexo : Char (o Enum) |
| inst_especialidad : Char  |
| inst_turno : Char         |
+---------------------------+

+---------------------------+
| Clase                    |
+---------------------------+
| clase_id : Integer PK     |
| clase_nombre : Char       |
| clase_tema : Char         |
| clase_horario : Char      |
| clase_cupo : Integer      |
+---------------------------+

+---------------------------+
| Equipamiento             |
+---------------------------+
| codigo : Char PK          |
| nombre_ref : Char         |
| categoria : FK (?)        |
| marca : Char              |
| peso : Decimal/Float      |
| nro_serie : Char          |
| estado : Char/Enum        |
| fecha_alta : Date         |
| fecha_baja : DateTime     |
+---------------------------+
