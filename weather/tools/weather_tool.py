from mcp.server.fastmcp import FastMCP
from utils.weather_utils import (
    make_nws_request, format_alert, fetch_weather, format_weather
)
import sys

mcp = FastMCP("weather")

NWS_API_BASE = "https://api.weather.gov"

@mcp.tool()
async def get_alerts(state: str) -> str:
    print(f"🌐 Buscando alertas para el estado: {state}", file=sys.stderr)
    try:
        url = f"{NWS_API_BASE}/alerts/active/area/{state}"
        data = await make_nws_request(url)

        if not data or "features" not in data:
            return "Unable to retrieve alerts at this time or no alerts found."
        if not data["features"]:
            return "There are no active alerts for this state."

        alerts = [format_alert(feature) for feature in data["features"]]
        return "\n---\n".join(alerts)
    except Exception as e:
        print(f"💥 Error en get_alerts: {e}", file=sys.stderr)
        return "Error procesando las alertas."

@mcp.tool()
async def get_forecast(city: str) -> str:
    print(f"📡 Obteniendo pronóstico para: {city}", file=sys.stderr)
    try:
        data = await fetch_weather(city)
        if not data or data.get("cod") != 200:
            print(f"⚠️ Respuesta inesperada: {data}", file=sys.stderr)
            return f"No se pudo obtener el clima para {city}."
        return format_weather(data)
    except Exception as e:
        print(f"💥 Error en get_forecast: {e}", file=sys.stderr)
        return f"Error procesando el clima para {city}."
