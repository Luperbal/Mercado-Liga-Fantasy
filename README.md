# Mercado-Liga-Fantasy - Fantasy Market Analytics 🚀⚽

Este proyecto tiene como objetivo crear una herramienta para **monitorizar y recibir automáticamente los jugadores con mayor subida de valor en LaLiga Fantasy**.

La motivación es sencilla: cada día el mercado fantasy cambia, y resulta útil recibir un listado de los **jugadores con mayor subida de valor en la última actualización** para tenerlos presentes y tomar decisiones en el juego.

## 🌟 Funcionalidades previstas

1. **Web Scraping (Feature 1)** ✅  
   - Obtiene los datos del mercado directamente desde [futbolfantasy.com](https://www.futbolfantasy.com/analytics/laliga-fantasy/mercado).  
   - Extrae nombre, valor actual, y diferencia.  
   - Ordena de mayor a menor subida.  
   - Guarda en un archivo JSON para uso posterior.

2. **Procesamiento con LLM (en desarrollo)** 🔄  
   - El JSON con los jugadores se pasará a un **modelo de lenguaje (LLM)**.  
   - El LLM generará un listado de jugadores clave (top 10, 15 o 20 según se configure).  
   - El listado será más legible y “humano”.

3. **Notificaciones (pendiente de implementación)** 🔜  
   - El listado final se enviará automáticamente a través de **WhatsApp** u otro canal de mensajería.  
   - Posible integración con la API de WhatsApp o servicios alternativos.

## 📂 Estructura del proyecto

- `feature1-webscrapping/` → Rama con el scraper funcional en Python.
- `main/` → Rama principal con visión general e integración futura de todas las partes.
- Futuras ramas → nuevas funcionalidades (LLM, envío de mensajes, automatización, etc.).

## 🔧 Requisitos

- Python 3.9+
- Librerías:  
  ```bash
  pip install requests beautifulsoup4
