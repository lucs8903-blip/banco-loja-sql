import sqlite3
conn = sqlite3.connect("loja_select.db")
cursor = conn.cursor()
# Remover tabelas antigas, caso existam
cursor.execute("DROP TABLE IF EXISTS venda")
cursor.execute("DROP TABLE IF EXISTS produto")
cursor.execute("DROP TABLE IF EXISTS cliente")
# Criar tabela cliente
cursor.execute("""
CREATE TABLE cliente (
id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
cidade TEXT NOT NULL
)
""")
# Criar tabela produto
cursor.execute("""
CREATE TABLE produto (
id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
preco REAL NOT NULL,
estoque INTEGER NOT NULL
)
""")
# Criar tabela venda
cursor.execute("""
CREATE TABLE venda (
id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
id_cliente INTEGER NOT NULL,
valor REAL NOT NULL,
data_venda TEXT NOT NULL,
FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
)
""")
# Inserir clientes
clientes = [
("Ana Silva", "Macapá"),
("Bruno Costa", "Santana"),
("Carlos Almeida", "Macapá"),
("Mariana Souza", "Belém"),
("João Silva", "Santana"),
("Fernanda Lima", "Macapá"),
("Amanda Rocha", "Belém"),
("Pedro Martins", "Oiapoque"),
("Lucas Ferreira", "Macapá"),
("Aline Santos", "Santana")
]
cursor.executemany("""
INSERT INTO cliente (nome, cidade)
VALUES (?, ?)
""", clientes)
# Inserir produtos
produtos = [
("Notebook Dell", 3500.00, 8),
("Mouse Gamer", 120.00, 25),
("Teclado Mecânico", 280.00, 15),
("Monitor 24 Polegadas", 900.00, 6),
("Cabo HDMI", 35.00, 50),
("Headset Bluetooth", 180.00, 12),
("Mousepad Grande", 45.00, 30),
("Memória RAM 8GB", 250.00, 10),
("SSD 480GB", 320.00, 4),
("Webcam Full HD", 210.00, 7),
("Microfone USB", 450.00, 3),
("Carregador Universal", 85.00, 18)
]
cursor.executemany("""
INSERT INTO produto (nome, preco, estoque)
VALUES (?, ?, ?)
""", produtos)
# Inserir vendas
vendas = [
(1, 3500.00, "2026-05-01"),
(2, 120.00, "2026-05-02"),
(3, 900.00, "2026-05-03"),
(1, 280.00, "2026-05-04"),
(5, 35.00, "2026-05-05"),
(6, 180.00, "2026-05-06"),
(7, 320.00, "2026-05-07"),
(8, 450.00, "2026-05-08")
]
cursor.executemany("""
INSERT INTO venda (id_cliente, valor, data_venda)
VALUES (?, ?, ?)
""", vendas)
conn.commit()
print("Banco de dados criado e populado com sucesso!")
print("Arquivo gerado: loja_select.db")
conn.close()