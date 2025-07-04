# utils/sqlite_utils.py
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()
DB_PATH = os.getenv("DB_PATH", "utils/company_mcp.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            department TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')

    # Datos iniciales solo si las tablas están vacías
    cursor.execute("SELECT COUNT(*) FROM employees")
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''
            INSERT INTO employees (name, age, department) VALUES (?, ?, ?)
        ''', [
            ('Alice', 30, 'Engineering'),
            ('Bob', 45, 'HR'),
            ('Charlie', 28, 'Marketing')
        ])

    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''
            INSERT INTO products (name, price, stock) VALUES (?, ?, ?)
        ''', [
            ('Laptop', 1200.00, 10),
            ('Mouse', 25.50, 100),
            ('Keyboard', 45.00, 50)
        ])

    conn.commit()
    conn.close()
