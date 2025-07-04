# validate_sqlite_mcp.py
import os
import subprocess
import sys
import shutil
from dotenv import load_dotenv

print("🔍 Validando configuración del proyecto sqlite-crud...\n")

# Cargar variables del entorno
load_dotenv()

def check_env_file():
    return os.path.isfile(".env") and os.getenv("DB_PATH") is not None

def check_db_file():
    db_path = os.getenv("DB_PATH", "utils/company_mcp.db")
    return os.path.exists(db_path)

def check_uvx():
    return shutil.which("uvx") is not None

def check_tools_file():
    return os.path.isfile("tools/sqlite_tools.py")

def check_stdio_communication():
    try:
        result = subprocess.run(
            ["uv", "--directory", ".", "run", "sqlite_crud.py"],
            input="{}",
            capture_output=True,
            text=True,
            timeout=5
        )
        return "Iniciando servidor MCP" in result.stderr
    except Exception as e:
        print(f"❌ Error ejecutando servidor MCP: {e}")
        return False

# Resultados
print("📦 Archivo .env:", "✔️ Encontrado con DB_PATH" if check_env_file() else "❌ No encontrado o DB_PATH faltante")
print("🗃️ Base de datos (utils\\company_mcp.db):", "✔️ Existe" if check_db_file() else "❌ No encontrada")
print("🔧 uvx instalado:", "✔️ Sí" if check_uvx() else "❌ No encontrado")
print("🛠️ Archivo de herramientas MCP:", "✔️ tools/sqlite_tools.py OK" if check_tools_file() else "❌ No encontrado")
print("📡 Comunicación por stdio:", "✔️ OK" if check_stdio_communication() else "❌ Falló")
