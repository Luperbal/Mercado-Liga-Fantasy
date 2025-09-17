import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

def web_scrape_to_json(url):
    """
    Realiza web scraping en una URL dada para extraer tablas y otros datos,
    y los guarda en un archivo JSON.
    
    Args:
        url (str): La URL de la página web a scrapear.
        
    Returns:
        bool: True si la operación fue exitosa, False en caso contrario.
    """
    
    # 1. Realizar la solicitud HTTP
    try:
        response = requests.get(url, timeout=10)
        # Lanzar una excepción si la respuesta no es 200 OK
        response.raise_for_status()  
        print(f"✅ Conexión exitosa a: {url}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al acceder a la URL: {e}")
        return False
        
    # 2. Parsear el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Diccionario para almacenar todos los datos
    scraped_data = {}
    
    # 3. Extraer el título de la página
    title = soup.find('title')
    scraped_data['titulo_pagina'] = title.text.strip() if title else 'No se encontró el título'
    
    # 4. Encontrar y procesar todas las tablas
    tables = soup.find_all('table')
    print(f"🔎 Se encontraron {len(tables)} tabla(s) en la página.")
    
    # Iterar sobre cada tabla encontrada
    for i, table in enumerate(tables):
        
        # Encontrar las cabeceras (<th>)
        headers = [header.text.strip() for header in table.find_all('th')]
        
        # Encontrar las filas de datos (<tr>)
        rows = table.find_all('tr')
        
        table_data = []
        for row in rows:
            # Encontrar las celdas de datos (<td>)
            cells = row.find_all('td')
            # Extraer el texto de cada celda y limpiar espacios
            row_data = [cell.text.strip() for cell in cells]
            
            # Asegurarse de que los datos de la fila no estén vacíos
            if row_data:
                table_data.append(row_data)

        scraped_data[f'tabla_{i+1}'] = {
            'headers': headers,
            'data': table_data
        }
    
    # 5. Opcional: Extraer enlaces
    # links = [link.get('href') for link in soup.find_all('a')]
    # scraped_data['links'] = links
    
    # 6. Guardar los datos en un archivo JSON
    try:
        with open('scraped_data.json', 'w', encoding='utf-8') as f:
            json.dump(scraped_data, f, ensure_ascii=False, indent=4)
        print("💾 Datos guardados en 'scraped_data.json'")
        return True
    except IOError as e:
        print(f"❌ Error al guardar el archivo: {e}")
        return False

# --- Ejemplo de uso ---
# Reemplaza esta URL con la página que quieras scrapear.
# La URL de FutbolFantasy que me diste anteriormente es un buen ejemplo.
# url_to_scrape = 'https://www.futbolfantasy.com/analytics/laliga-fantasy'
# web_scrape_to_json(url_to_scrape)

# Puedes usar cualquier URL con tablas

url_to_scrape = 'https://www.futbolfantasy.com/analytics/laliga-fantasy/mercado'
web_scrape_to_json(url_to_scrape)