import json
from huggingface_hub import InferenceClient

# --- Aquí pones tu token directamente ---
HF_TOKEN = "xxx"

# --- Crear cliente Hugging Face con Groq ---
client = InferenceClient(
    provider="groq",
    api_key=HF_TOKEN,
)

# --- Cargar JSON de jugadores ---
with open("jugadores_laliga_fantasy.json", "r", encoding="utf-8") as f:
    jugadores = json.load(f)

# Ordenar por mayor subida
jugadores_ordenados = sorted(jugadores, key=lambda x: x["cambio_valor"], reverse=True)

# Crear la lista para el prompt
lista_jugadores = "\n".join([
    f"{j['nombre'].title()}: +{j['cambio_valor']:,}€".replace(",", ".")
    for j in jugadores_ordenados[:10]  # Top 10
])

# Prompt para el modelo
prompt = f"""
Genera un mensaje claro y conciso en español con el siguiente formato:

Mayores subidas en la actualización del mercado
{lista_jugadores}
"""

# --- Llamada al modelo ---
completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",  # Modelo disponible vía Groq
    messages=[
        {"role": "user", "content": prompt}
    ],
)

# --- Mostrar resultado ---
mensaje = completion.choices[0].message["content"]
print(mensaje)
