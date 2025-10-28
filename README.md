# Guías de Implementación - IA con Python y OpenAI
Profesor: Luis Daniel Benavides Navarro
Fecha: 22 de octubre de 2025

# Guía 1 - Hello World AI con Python y API de OpenAI
Objetivo
Introducir los conceptos esenciales para conectarse a un modelo de lenguaje de OpenAI desde Python.

Requisitos previos
Python 3.10 o superior instalado

Cuenta activa en OpenAI

Conexión a Internet estable

Editor de código (VS Code, Jupyter Notebook, etc.)

1. Creación del entorno virtual
bash


# Instalar dependencias necesarias
pip install openai python-dotenv
2. Configuración de la clave API
Crear archivo .env en la raíz del proyecto:

text
OPENAI_API_KEY=tu_clave_aqui
Advertencia: Nunca subas este archivo a GitHub. Añádelo siempre a tu .gitignore.

3. Primer script: Hello World AI
Crear archivo hello_ai.py:

python
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
4. Ejecución del programa
bash
python hello_ai.py
5. Explicación del código
Importaciones: Se usan os, dotenv y openai para manejar la clave API

load_dotenv(): Carga las variables definidas en .env

Inicialización del cliente: Establece conexión segura con la API

prompt: Instrucción enviada al modelo

temperature: Controla la creatividad (0.1 = precisa, 1.0 = creativa)

Salida del modelo: Se obtiene con response.choices[0].message.content

<img width="855" height="452" alt="image" src="https://github.com/user-attachments/assets/d6f52b54-ff94-4f89-954e-a808d2a15bee" />
<img width="921" height="219" alt="image" src="https://github.com/user-attachments/assets/5fdd8bde-6fa6-496e-a5c4-15456b8f6a20" />


# Guía 2 - Hello World AI en Jupyter Notebook (VS Code)
Objetivo
Crear un proyecto de IA desde Visual Studio Code usando Jupyter Notebook.

Requisitos previos
Visual Studio Code versión 1.85 o superior

Extensiones: Python y Jupyter

Python 3.10 o superior

Cuenta y clave API de OpenAI

1. Configuración del entorno
bash
# Instalar dependencias
pip install openai python-dotenv jupyter ipykernel

# Crear kernel personalizado
python -m ipykernel install --user --name hello_ai_vscode
2. Configurar clave API
Crear archivo .env con:

text
OPENAI_API_KEY=tu_clave_aqui
3. Celdas del Notebook
Celda 1 - Configuración:

python
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print("Cliente OpenAI inicializado correctamente.")
Celda 2 - Ejemplo Hello World AI:

python
prompt = "Escribe un saludo tipo 'Hello World' con un toque creativo de IA."
resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.6
)
print(resp.choices[0].message.content)
4. Parámetros importantes de la API
Parámetro	Descripción
model	Modelo a utilizar (gpt-4o-mini)
messages	Lista de mensajes (system, user, assistant)
temperature	Controla creatividad (0.1-0.3 = precisa; 0.7-1.0 = creativa)
max_tokens	Límite de tokens generados
top_p	Alternativa probabilística a temperature
5. Ejercicio adicional
python
for t in [0.1, 0.5, 0.9]:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Describe brevemente qué es la IA."}],
        temperature=t,
        max_tokens=50
    )
    print(f"--- temperature={t} ---")
    print(response.choices[0].message.content)


<img width="754" height="541" alt="image" src="https://github.com/user-attachments/assets/0c0127a7-f6f1-4ed2-a36c-fc0404a08c4e" />
<img width="1170" height="555" alt="image" src="https://github.com/user-attachments/assets/ee485dfd-39a9-4851-aa83-278f7331fc93" />

<img width="587" height="83" alt="image" src="https://github.com/user-attachments/assets/48e1a952-e19f-49bb-86f9-5abb9333b89a" />

<img width="504" height="170" alt="image" src="https://github.com/user-attachments/assets/cc1f5402-703d-400e-a80b-4249fde269d8" />



