import sqlite3

conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        profissao TEXT,
        salario REAL
    )
''')

dados = [
    ("Alice", "Engenheira", 8500.00),
    ("Bruno", "Médico", 12000.00),
    ("Carla", "Designer", 6500.00)
]

cursor.executemany('INSERT INTO pessoas (nome, profissao, salario) VALUES (?, ?, ?)', dados)

conn.commit()
conn.close()

print("Banco de dados criado com sucesso.")
