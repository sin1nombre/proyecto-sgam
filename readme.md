# SGAM – Sistema de Gestión de Atención Médica

Proyecto Django con base de datos **SQLite** para la gestión de citas, pacientes y profesionales.

---
## 1. Requisitos previos
>[!NOTE]
>Asegúrate de tener instalado:
>- Python 3.10+
>- pip
>- Git

SQLite viene integrado en Python, no requiere instalación adicional.


## 2. Clonar el proyecto
```bash
git clone https://github.com/sin1nombre/proyecto-sgam.git
```
En VSC:

- archivo
- abrir carpeta
- Seleccionar (proyecto sgam)

## 3. Configuración de la base de datos (SQLite)

La base se genera automáticamente al aplicar migraciones.

Para cambiar el nombre, edita settings.py:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'sgam_bd.sqlite3',
    }
}
```
## 4. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

## 5. Crear superusuario (falta)
python manage.py createsuperuser

## 6. Ejecutar el servidor
python manage.py runserver


Abrir en:

http://127.0.0.1:8000/


Panel de administración:

http://127.0.0.1:8000/admin/

## 7. Estructura del proyecto
```bash
proyecto_sgam/
│ manage.py
│ sgam_bd.sqlite3
│ README.md
│ requirements.txt
│
├── proyecto_sgam/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── pacientes/
├── profesionales/
├── citas/
└── agenda/
```
## 8. Flujo de trabajo con Git

Crear rama:
```bash
git checkout -b feature/nueva-funcion
```

Confirmar cambios:
```bash
git add .
git commit -m "Descripción del cambio"
```

Subir rama:
```bash
git push origin feature/nueva-funcion
```