# sqlite_crud.py
from tools.sqlite_tools import mcp
import sys

if __name__ == "__main__":
    print("🚀 Iniciando servidor MCP para SQLite CRUD...", file=sys.stderr)
    try:
        mcp.run(transport="stdio")
    except Exception as e:
        print(f"💥 Error al iniciar MCP: {e}", file=sys.stderr)
        raise
