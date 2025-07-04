# Proyecto SQLite-CRUD MCP

Este proyecto implementa un servidor MCP (Model Context Protocol) para realizar operaciones CRUD sobre una base de datos SQLite.

## ¿Qué es MCP?
MCP (Model Context Protocol) es un protocolo que facilita la integración de modelos de IA y herramientas externas de forma segura y estructurada.

## ¿Para qué sirve este proyecto?
Permite gestionar empleados y productos en una base de datos SQLite mediante comandos MCP, integrándose con asistentes y otras aplicaciones compatibles.

## ¿Cómo configurarlo?
1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python 3.9+ instalado.
3. (Opcional) Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   # En Linux/Mac:
   source .venv/bin/activate
   ```
4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   # O si usas poetry o pipenv, sigue el gestor definido en pyproject.toml
   ```
5. Configura las variables de entorno en el archivo `.env` si es necesario (por ejemplo, la ruta de la base de datos con `DB_PATH`).
6. Asegúrate de tener la base de datos SQLite creada o ejecuta el script de migración si existe.
7. Ejecuta el servidor MCP con el comando configurado en tu entorno (por ejemplo, usando uv o el gestor que prefieras):
   ```bash
   uv run --directory . sqlite_crud.py
   ```
8. Verifica que el servidor esté corriendo y accesible desde tu entorno MCP.

## Documentación oficial MCP
[https://modelcontextprotocol.org/docs](https://modelcontextprotocol.org/docs)
