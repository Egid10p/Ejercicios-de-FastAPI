# Ejercicio 01 - API CRUD de Tareas con FastAPI

## Descripción

Este ejercicio te guiará en la creación de una API RESTful completa utilizando el framework FastAPI de Python. El objetivo es construir un sistema para gestionar una lista de tareas, implementando las operaciones CRUD (Crear, Leer, Actualizar y Eliminar). Puedes optar por utilizar una base de datos SQL para persistencia de datos o, para simplificar, comenzar con un array en memoria para almacenar las tareas.

## Objetivo

Familiarizarse con el desarrollo de APIs RESTful utilizando FastAPI.
Aprender a definir modelos de datos con Pydantic.
Implementar las operaciones CRUD básicas.
Practicar el manejo de rutas y parámetros en FastAPI.
Explorar la documentación automática de FastAPI.

## Requisitos

Instalación de FastAPI y Uvicorn:

Asegúrate de tener Python 3.7+ instalado.
Ejecuta el siguiente comando para instalar FastAPI y las dependencias necesarias:
Bash

`pip install fastapi[standard] uvicorn`
FastAPI es el framework web, y uvicorn es el servidor ASGI que se utilizará.

## Definición del Modelo de Datos:

Utiliza Pydantic para definir la estructura de una tarea. Deberás incluir campos como id, titulo, descripcion y completada.
Ejemplo:

```Python
from pydantic import BaseModel

class Tarea(BaseModel):
id: int
titulo: str
descripcion: str
completada: bool = False
```

## Implementación de las Operaciones CRUD:

-   Crear (POST): Define una ruta para crear nuevas tareas.
-   Leer (GET): Implementa rutas para obtener la lista completa de tareas y para obtener una tarea específica por su id.
-   Actualizar (PUT): Crea una ruta para actualizar los detalles de una tarea existente.
-   Eliminar (DELETE): Define una ruta para eliminar una tarea por su id.
-   Maneja los casos de error, como tareas no encontradas, utilizando HTTPException.

## Ejecución de la API:

Ejecuta el servidor Uvicorn con el siguiente comando:
Bash

`uvicorn main:app --reload`
Accede a la documentación automática de la API en http://127.0.0.1:8000/docs.
