# tools/sqlite_tools.py
import sqlite3
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "utils/company_mcp.db")

# Crear instancia de FastMCP
mcp = FastMCP()

# --- EMPLEADOS ---

@mcp.tool()
def get_employees() -> list:
    """Devuelve la lista de empleados."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age, department FROM employees")
        return cursor.fetchall()

@mcp.tool()
def add_employee(name: str, age: int, department: str) -> str:
    """Agrega un empleado."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO employees (name, age, department) VALUES (?, ?, ?)",
            (name, age, department),
        )
        conn.commit()
    return f"Empleado '{name}' agregado correctamente."

@mcp.tool()
def update_employee(id: int, name: str, age: int, department: str) -> str:
    """Actualiza los datos de un empleado."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE employees SET name = ?, age = ?, department = ? WHERE id = ?",
            (name, age, department, id),
        )
        conn.commit()
    return f"Empleado con ID {id} actualizado correctamente."

@mcp.tool()
def delete_employee(id: int) -> str:
    """Elimina un empleado por ID."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE id = ?", (id,))
        conn.commit()
    return f"Empleado con ID {id} eliminado correctamente."

# --- PRODUCTOS ---

@mcp.tool()
def get_products() -> list:
    """Devuelve la lista de productos."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, price, stock FROM products")
        return cursor.fetchall()

@mcp.tool()
def add_product(name: str, price: float, stock: int) -> str:
    """Agrega un producto."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
            (name, price, stock),
        )
        conn.commit()
    return f"Producto '{name}' agregado correctamente."

@mcp.tool()
def update_product(id: int, name: str, price: float, stock: int) -> str:
    """Actualiza los datos de un producto."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE products SET name = ?, price = ?, stock = ? WHERE id = ?",
            (name, price, stock, id),
        )
        conn.commit()
    return f"Producto con ID {id} actualizado correctamente."

@mcp.tool()
def delete_product(id: int) -> str:
    """Elimina un producto por ID."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (id,))
        conn.commit()
    return f"Producto con ID {id} eliminado correctamente."

# --- TABLAS ---

@mcp.tool()
def create_table(schema_sql: str) -> str:
    """Crea una nueva tabla usando una sentencia SQL CREATE TABLE."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(schema_sql)
        conn.commit()
    return "Tabla creada correctamente."

@mcp.tool()
def drop_table(table_name: str) -> str:
    """Elimina una tabla si existe."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        conn.commit()
    return f"Tabla '{table_name}' eliminada correctamente."

@mcp.tool()
def list_tables() -> list:
    """Devuelve la lista de tablas en la base de datos."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return [row[0] for row in cursor.fetchall()]
