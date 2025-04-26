import sqlite3
import bcrypt

# Função para gerar hash com bcrypt
def gerar_bcrypt_hash(senha):
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Conexão com o banco
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()

# Apaga a tabela se já existir
cursor.execute('DROP TABLE IF EXISTS pessoas')

# Cria a tabela com a estrutura necessária
cursor.execute('''
    CREATE TABLE pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        profissao TEXT NOT NULL,
        salario REAL NOT NULL,
        senha TEXT NOT NULL
    )
''')

# Dados com senha já criptografada (bcrypt)
dados = [
    ("Alice", "Engenheira", 8500.00, gerar_bcrypt_hash("senha123")),
    ("Bruno", "Médico", 12000.00, gerar_bcrypt_hash("senha456")),
    ("Carla", "Designer", 6500.00, gerar_bcrypt_hash("senha789"))
]

# Inserção dos dados no banco
cursor.executemany(
    'INSERT INTO pessoas (nome, profissao, salario, senha) VALUES (?, ?, ?, ?)',
    dados
)

# Commit e encerramento
conn.commit()
conn.close()

print("Banco de dados recriado com senhas criptografadas usando bcrypt.")
