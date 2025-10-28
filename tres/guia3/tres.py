import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Lee el archivo .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print("Cliente inicializado. Modelo listo para consultas.")

# 5) Primera consulta: respuesta libre
prompt = "Explica en dos frases qué es la inteligencia artificial en la educación."
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7  # más creativo que 0.2, menos que 1.0
)
print(response.choices[0].message.content)