import sqlite3

conn = sqlite3.connect("loja_select.db")
cursor = conn.cursor()

print("=== 1. LISTAR TODOS OS CLIENTES ===")
cursor.execute("SELECT * FROM cliente")
for cliente in cursor.fetchall():
    print(cliente)

print("\n=== 2. LISTAR TODOS OS PRODUTOS ===")
cursor.execute("SELECT * FROM produto")
for produto in cursor.fetchall():
    print(produto)

print("\n=== 3. NOME E PREÇO DOS PRODUTOS ===")
cursor.execute("SELECT nome, preco FROM produto")
for nome, preco in cursor.fetchall():
    print(f"{nome}: R$ {preco:.2f}")

print("\n=== 4. PRODUTOS COM PREÇO > 100 ===")
cursor.execute("SELECT * FROM produto WHERE preco > 100")
for p in cursor.fetchall():
    print(p)

print("\n=== 5. PRODUTOS COM PREÇO < 500 ===")
cursor.execute("SELECT * FROM produto WHERE preco < 500")
for p in cursor.fetchall():
    print(p)

print("\n=== 6. CLIENTES DE MACAPÁ ===")
cursor.execute("SELECT * FROM cliente WHERE cidade = 'Macapá'")
for c in cursor.fetchall():
    print(c)

print("\n=== 7. PRODUTOS COM ESTOQUE > 10 ===")
cursor.execute("SELECT * FROM produto WHERE estoque > 10")
for p in cursor.fetchall():
    print(p)

print("\n=== 8. PREÇO > 100 E ESTOQUE > 5 ===")
cursor.execute("SELECT * FROM produto WHERE preco > 100 AND estoque > 5")
for p in cursor.fetchall():
    print(p)

print("\n=== 9. PREÇO < 50 OU ESTOQUE > 20 ===")
cursor.execute("SELECT * FROM produto WHERE preco < 50 OR estoque > 20")
for p in cursor.fetchall():
    print(p)

print("\n=== 10. CLIENTES COM NOME INICIANDO COM 'A' ===")
cursor.execute("SELECT * FROM cliente WHERE nome LIKE 'A%'")
for c in cursor.fetchall():
    print(c)

print("\n=== 11. PRODUTOS COM 'NOTE' NO NOME ===")
cursor.execute("SELECT * FROM produto WHERE LOWER(nome) LIKE '%note%'")
for p in cursor.fetchall():
    print(p)

print("\n=== 12. PRODUTOS COM PREÇO ENTRE 100 E 500 ===")
cursor.execute("SELECT * FROM produto WHERE preco BETWEEN 100 AND 500")
for p in cursor.fetchall():
    print(p)

print("\n=== 13. PRODUTOS ORDENADOS POR PREÇO CRESCENTE ===")
cursor.execute("SELECT * FROM produto ORDER BY preco ASC")
for p in cursor.fetchall():
    print(p)

print("\n=== 14. PRODUTOS ORDENADOS POR PREÇO DECRESCENTE ===")
cursor.execute("SELECT * FROM produto ORDER BY preco DESC")
for p in cursor.fetchall():
    print(p)

print("\n=== 15. CLIENTES ORDENADOS POR NOME ===")
cursor.execute("SELECT * FROM cliente ORDER BY nome ASC")
for c in cursor.fetchall():
    print(c)

print("\n=== 16. PRODUTOS ORDENADOS POR PREÇO DESC E NOME ASC ===")
cursor.execute("SELECT * FROM produto ORDER BY preco DESC, nome ASC")
for p in cursor.fetchall():
    print(p)

conn.close()