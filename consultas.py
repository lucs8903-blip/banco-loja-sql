import sqlite3

conn = sqlite3.connect("loja_select.db")
cursor = conn.cursor()

print("=== LISTA DE CLIENTES ===")
cursor.execute("SELECT * FROM cliente")
clientes = cursor.fetchall()

for cliente in clientes:
    print(f"ID: {cliente[0]}  / nome: {cliente[1]} / cidade: {cliente[2]}")
    
    conn.close()