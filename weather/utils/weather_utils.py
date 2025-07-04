from typing import Any
import httpx
import os
import sys
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("OPENWEATHER_API_KEY")
print(f"🔑 API Key leída desde .env: {API_KEY}", file=sys.stderr)

async def make_nws_request(url: str) -> dict[str, Any] | None:
    headers = {
        "User-Agent": "weather-app/1.0",
        "Accept": "application/geo+json"
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"❌ Error en make_nws_request: {e}", file=sys.stderr)
        return None

async def fetch_weather(city: str) -> dict[str, Any] | None:
    if not API_KEY:
        print("❌ API_KEY no definida", file=sys.stderr)
        return None

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(OPENWEATHER_API, params=params)
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"❌ Error en fetch_weather: {e}", file=sys.stderr)
        return None

def format_alert(feature: dict) -> str:
    props = feature["properties"]
    return f"""
📢 Evento: {props.get('event', 'Desconocido')}
📍 Área: {props.get('areaDesc', 'Desconocida')}
🔴 Severidad: {props.get('severity', 'Desconocida')}
📄 Descripción: {props.get('description', 'No disponible')}
📌 Instrucciones: {props.get('instruction', 'No disponible')}
"""

def format_weather(data: dict[str, Any]) -> str:
    return f"""
📍 Ciudad: {data['name']}
🌡️ Temperatura: {data['main']['temp']}°C
💧 Humedad: {data['main']['humidity']}%
💨 Viento: {data['wind']['speed']} m/s
🌤️ Descripción: {data['weather'][0]['description'].capitalize()}
"""
