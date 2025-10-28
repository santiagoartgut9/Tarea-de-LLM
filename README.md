
Profesor: Luis Daniel Benavides Navarro
Fecha: 22 de octubre de 2025

Este documento reúne las Guías 1 y 2 del curso, así como un anexo de seguridad y control de versiones, que describe en detalle el proceso completo para crear, configurar y asegurar un entorno funcional de inteligencia artificial con Python y la API de OpenAI.

📘 Guía 1 — Hello World AI con Python y la API de OpenAI
🎯 Objetivo

Introducir los conceptos esenciales para conectarse a un modelo de lenguaje de OpenAI desde Python.
Al finalizar, el estudiante podrá construir un entorno funcional, comprender la estructura básica de la API y ejecutar un ejemplo tipo “Hello World AI”.

🧩 1. Requisitos previos

Antes de comenzar, asegúrese de contar con:

✅ Python 3.10 o superior instalado.

✅ Cuenta activa en OpenAI
.

✅ Conexión a Internet estable.

✅ Editor de código, como Visual Studio Code o Jupyter Notebook.

🏗️ 2. Creación del entorno virtual

Crear un entorno virtual aísla las dependencias y mantiene tu proyecto limpio.

# Crear carpeta de trabajo
```bash
mkdir hello_ai
cd hello_ai
```
# Crear entorno virtual
```bash
python -m venv venv
```


# Instalar dependencias necesarias
```bash
pip install openai python-dotenv
```
🔐 3. Configuración de la clave API

La API de OpenAI requiere autenticación mediante una clave personal.

Crea un archivo llamado .env en la raíz del proyecto.

Agrega la línea siguiente:

OPENAI_API_KEY=tu_clave_aqui


⚠️ Advertencia: Nunca subas este archivo a GitHub.
Añádelo siempre a tu .gitignore.

Puedes generar una nueva clave en:
🔗 https://platform.openai.com/account/api-keys

💻 4. Primer script: Hello World AI

Crea un archivo hello_ai.py con el siguiente contenido:

import os
from openai import OpenAI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Inicializar cliente con la clave API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Solicitud al modelo
prompt = "Escribe un saludo tipo 'Hello World' con un toque creativo de IA."
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.6
)

# Mostrar respuesta
print("Respuesta del modelo:")
print(response.choices[0].message.content)

🧠 5. Explicación del código

Importaciones: Se usan os, dotenv y openai para manejar la clave API.

load_dotenv(): Carga las variables definidas en .env.

Inicialización del cliente: Establece conexión segura con la API.

prompt: Es la instrucción enviada al modelo.

temperature: Controla la creatividad de la respuesta (0.1 = precisa, 1.0 = creativa).

Salida del modelo: Se obtiene con response.choices[0].message.content.

▶️ 6. Ejecución del programa

Ejecuta el script:

python hello_ai.py


Ejemplo de salida:

Respuesta del modelo:
¡Hola mundo! Hoy la inteligencia artificial también quiere saludarte.

🧩 7. Conclusión

Ha completado su primera conexión con la API de OpenAI.
En la siguiente guía se abordará cómo usar Jupyter Notebook dentro de VS Code y cómo estructurar salidas más complejas.

<img width="855" height="452" alt="image" src="https://github.com/user-attachments/assets/d6f52b54-ff94-4f89-954e-a808d2a15bee" />
<img width="921" height="219" alt="image" src="https://github.com/user-attachments/assets/5fdd8bde-6fa6-496e-a5c4-15456b8f6a20" />




📗 Guía 2 — Hello World AI en Jupyter Notebook (VS Code)
🎯 Objetivo

Crear un proyecto de IA directamente desde Visual Studio Code, utilizando Jupyter Notebook para interactuar con la API de OpenAI de forma visual e interactiva.

🧩 1. Requisitos previos

Visual Studio Code versión 1.85 o superior.

Extensiones instaladas:

🐍 Python (Microsoft)

📓 Jupyter (Microsoft)

Python 3.10 o superior.

Cuenta y clave API de OpenAI.

Conexión a Internet.

🗂️ 2. Crear carpeta del proyecto

Abra VS Code.

Seleccione File > Open Folder...

Cree una carpeta llamada hello_ai_vscode y ábrala.

⚙️ 3. Crear y activar entorno virtual

Presione Ctrl + Shift + P → escriba Python: Create Environment.

Elija tipo Venv y el intérprete Python adecuado.

Espere a que se cree y active el entorno.

VS Code mostrará una notificación indicando el entorno activo en la esquina inferior derecha.

📦 4. Instalar dependencias

Desde el terminal integrado (Ctrl + Ñ):

pip install openai python-dotenv jupyter ipykernel
python -m ipykernel install --user --name hello_ai_vscode

🧾 5. Configurar la clave API (.env)

Cree un archivo .env en la raíz del proyecto.

Agregue su clave API:

OPENAI_API_KEY=tu_clave_aqui


Guarde el archivo.

Añada .env a su archivo .gitignore para evitar subirlo a GitHub.

💡 6. Crear el Notebook principal

Ctrl + Shift + P → Jupyter: Create New Jupyter Notebook.

Guárdelo como hello_ai.ipynb.

Seleccione el kernel hello_ai_vscode.

🧱 7. Celdas principales

Celda 1 — Configuración

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print("Cliente OpenAI inicializado correctamente.")


Celda 2 — Ejemplo Hello World AI

prompt = "Escribe un saludo tipo 'Hello World' con un toque creativo de IA."
resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.6
)
print(resp.choices[0].message.content)

⚙️ 8. Parámetros importantes de la API
Parámetro	Descripción
model	Modelo a utilizar, e.g. gpt-4o-mini
messages	Lista de mensajes (roles: system, user, assistant)
temperature	Controla creatividad (0.1–0.3 = precisa; 0.7–1.0 = creativa)
max_tokens	Límite de tokens generados
top_p	Alternativa probabilística a temperature
🧪 9. Ejercicio adicional
for t in [0.1, 0.5, 0.9]:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Describe brevemente qué es la IA."}],
        temperature=t,
        max_tokens=50
    )
    print(f"--- temperature={t} ---")
    print(response.choices[0].message.content)


Observe cómo cambia el tono de las respuestas con diferentes valores de temperature.

🏁 10. Cierre

El entorno Jupyter dentro de VS Code le permite ejecutar código de IA de forma interactiva, visual y segura.
En próximas guías aprenderá a generar salidas estructuradas en JSON y crear asistentes docentes personalizados.

🔒 Anexo — Seguridad, .env y limpieza del historial Git

Durante el desarrollo, se detectó una clave API expuesta accidentalmente en el historial de GitHub.
Para corregirlo y asegurar el repositorio, se aplicó un proceso completo de sanitización y reescritura del historial.

🔍 Problema

GitHub bloqueó el push con el mensaje:

GH013: Push cannot contain secrets — OpenAI API Key detected

🧹 Solución aplicada

Revocar inmediatamente la API key comprometida.

Eliminarla del historial con git-filter-repo:

python -m pip install git-filter-repo
git filter-repo --invert-paths --paths uno/.env


Verificar eliminación:

git log --all --pretty=format:%H --name-only | findstr uno/.env


Forzar push al nuevo repositorio:

git push --force origin main


Actualizar .gitignore:

echo ".env" >> .gitignore
git add .gitignore
git commit -m "Update .gitignore to ignore .env files"
git push

🧠 Buenas prácticas de seguridad

Nunca subas .env ni archivos con claves o tokens.

Usa variables de entorno o secretos en GitHub Actions si automatizas.

Revoca y regenera claves comprometidas.

Añade reglas de .gitignore globales:

*.env
.env
.env.*

🧾 Créditos y referencias

Documentación oficial de OpenAI API

Python-dotenv

VS Code + Jupyter Notebooks

GitHub Secret Scanning
