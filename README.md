# Mercado-Liga-Fantasy - Web Scraping Mercado LaLiga Fantasy 

Este módulo implementa un **web scraping** de la página de [Futbol Fantasy - Mercado LaLiga](https://www.futbolfantasy.com/analytics/laliga-fantasy/mercado) para obtener los datos de los jugadores y sus variaciones de valor de mercado.

## 🔧 Funcionalidad

- Extrae la información de cada jugador de los atributos `data-*`.
- Genera un listado en formato JSON con los campos:
  - `nombre`
  - `valor_actual`
  - `cambio_valor`
- Ordena los jugadores de **mayor a menor subida de valor**.
- Guarda los datos en un archivo `jugadores_laliga_fantasy.json`.

## 🚀 Ejecución

Instala las dependencias necesarias:

```bash
pip install requests beautifulsoup4
