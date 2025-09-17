import requests
from bs4 import BeautifulSoup
import json
import sys

URL = "https://www.futbolfantasy.com/analytics/laliga-fantasy/mercado"

def fetch_players(url: str):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error en la petición: {e}")
        sys.exit(1)

    soup = BeautifulSoup(response.text, "html.parser")

    jugadores = []
    elementos = soup.select("div.elemento_jugador")

    if not elementos:
        print("No se encontraron jugadores. ¿Cambió la estructura HTML?")
        return jugadores

    for el in elementos:
        try:
            nombre = el.get("data-nombre")
            valor_actual = el.get("data-valor1")
            cambio_valor = el.get("data-diferencia1")

            jugador = {
                "nombre": nombre,
                "valor_actual": int(valor_actual) if valor_actual else None,
                "cambio_valor": int(cambio_valor) if cambio_valor else None,
            }
            jugadores.append(jugador)
        except Exception as e:
            print(f"Error procesando jugador: {e}")
            
	# Ordenar por cambio_valor (descendente)
    jugadores = sorted(
        jugadores,
        key=lambda x: x["cambio_valor"] if x["cambio_valor"] is not None else 0,
        reverse=True,
    )

    return jugadores

def save_to_file(data, filename="jugadores_laliga_fantasy.json"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Archivo guardado en {filename}")
    except IOError as e:
        print(f"Error guardando archivo: {e}")

def main():
    print("Extrayendo datos de jugadores...")
    jugadores = fetch_players(URL)
    if jugadores:
        # Ejemplo: solo los top 50 (opcional)
        # jugadores = jugadores[:50]
        save_to_file(jugadores[:50])
    else:
        print("No se pudo extraer información.")

if __name__ == "__main__":
    main()
