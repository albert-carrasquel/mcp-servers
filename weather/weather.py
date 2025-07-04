from tools.weather_tool import mcp
import sys

if __name__ == "__main__":
    print("🚀 Iniciando servidor MCP...", file=sys.stderr)
    try:
        mcp.run(transport="stdio")
    except Exception as e:
        print(f"💥 Error general al ejecutar el servidor MCP: {e}", file=sys.stderr)
        raise
