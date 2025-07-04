from mcp.server.fastmcp import FastMCP
from tools.sqlite_tools import *  # Importa todas las tools

mcp = FastMCP("sqlite-crud")  # Nombre del servidor

if __name__ == "__main__":
    mcp.run(transport="stdio")