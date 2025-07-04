# Proyecto Weather MCP

Este proyecto es un servidor MCP (Model Context Protocol) para obtener información meteorológica.

## ¿Qué es MCP?
MCP (Model Context Protocol) es un protocolo que permite la integración de modelos de IA y herramientas externas de manera segura y estructurada.

## ¿Para qué sirve este proyecto?
Permite consultar el clima de diferentes ciudades y países a través de comandos MCP, integrándose fácilmente con asistentes y otras aplicaciones compatibles.

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
   # O usa el gestor definido en pyproject.toml si corresponde
   ```
5. Configura las variables de entorno en el archivo `.env` según tus necesidades (por ejemplo, claves de API para servicios meteorológicos).
6. Ejecuta el servidor con el comando configurado en tu entorno MCP (por ejemplo, usando uv):
   ```bash
   uv run --directory . weather.py
   ```
7. Verifica que el servidor esté corriendo y accesible desde tu entorno MCP.

## Documentación oficial MCP
[https://modelcontextprotocol.org/docs](https://modelcontextprotocol.org/docs)
