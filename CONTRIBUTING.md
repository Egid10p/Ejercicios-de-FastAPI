# Guía para Contribuir al Repositorio de Soluciones de FastAPI

¡Gracias por tu interés en contribuir a este repositorio! Aquí encontrarás los pasos para subir tus soluciones correctamente.

## 📌 Requisitos Previos

-   Tener una cuenta en [GitHub](https://github.com/).
-   Tener Git instalado en tu computadora.
-   Conocimientos básicos de FastAPI y Python.

## 🚀 Pasos para Contribuir

### 1️⃣ Haz un Fork del Repositorio

1. Ve al repositorio original en GitHub.
2. Haz clic en el botón **Fork** en la esquina superior derecha.
3. Esto creará una copia del repositorio en tu cuenta.

### 2️⃣ Clona tu Fork en tu PC

1. Copia la URL de tu fork.
2. Abre una terminal y ejecuta:
    ```bash
    git clone https://github.com/TU-USUARIO/REPO-NOMBRE.git
    ```
3. Entra en la carpeta del proyecto:
    ```bash
    cd REPO-NOMBRE
    ```

### 3️⃣ Crea una Rama para Tu Solución

1. Crea una nueva rama con tu nombre o un identificador único:
    ```bash
    git checkout -b mi-solucion
    ```

### 4️⃣ Agrega Tu Solución en la Carpeta Correspondiente

Cada ejercicio tiene su propia carpeta (por ejemplo, `Ejercicio-01`). Debes:

1. Ir a la carpeta del ejercicio.
2. Crear una nueva carpeta con tu nombre de usuario de GitHub.
    ```bash
    mkdir Ejercicio-01/TU-USUARIO
    ```
3. Colocar los archivos de tu solución dentro de esa carpeta.

### 5️⃣ Evita Subir el Entorno Virtual

Si creaste un entorno virtual, **no lo subas al repositorio**. Asegúrate de que el archivo `.gitignore` tenga la siguiente línea:

```
venv/
```

O usa el siguiente comando antes de hacer commit:

```bash
git rm -r --cached venv/
```

### 6️⃣ Confirma y Sube los Cambios

1. Agrega los archivos nuevos:
    ```bash
    git add .
    ```
2. Realiza un commit con un mensaje descriptivo:
    ```bash
    git commit -m "Agregada solución al Ejercicio-01 por @TU-USUARIO"
    ```
3. Sube los cambios a tu fork:
    ```bash
    git push origin mi-solucion
    ```

### 7️⃣ Crea un Pull Request (PR)

1. Ve a tu fork en GitHub.
2. Haz clic en **Contribute** > **Open pull request**.
3. Explica qué hiciste en el mensaje.
4. Envía el PR y espera la revisión.

---

## 🎯 Notas Finales

✔️ **No subas el entorno virtual (`venv`)**.
✔️ **Cada solución debe estar en una subcarpeta con tu usuario de GitHub**.
✔️ **Mantén el código limpio y organizado**.
✔️ **Sigue buenas prácticas de Python y FastAPI**.
✔️ **Si tienes dudas, pregunta en la sección de Issues**.

¡Gracias por contribuir! 🚀
