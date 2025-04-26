import logging
from flask import Flask, request, render_template, redirect
import sqlite3
import bcrypt

# Configuração do logger
logging.basicConfig(
    filename='app.log',  # Nome do arquivo de log
    level=logging.INFO,  # Nível de log (INFO, WARNING, ERROR, etc.)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato do log
)

app = Flask(__name__)
app.config['SECRET_KEY'] = '181369b4a106a6478ebdb64ba2c5e009'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form.get('username')
        senha = request.form.get('password')

        conn = sqlite3.connect('banco.db')
        c = conn.cursor()
        c.execute("SELECT senha FROM pessoas WHERE nome = ?", (nome,))
        usuario = c.fetchone()
        conn.close()

        if usuario and bcrypt.checkpw(senha.encode('utf-8'), usuario[0]):
            mensagem = f"Bem-vindo(a), {nome}!"
            logging.info(f"Login bem-sucedido para o usuário: {nome}")
            return render_template('login.html', mensagem=mensagem, sucesso=True)
        else:
            mensagem = "Credenciais inválidas. Tente novamente."
            logging.warning(f"Tentativa de login falhou para o usuário: {nome}")
            return render_template('login.html', mensagem=mensagem, sucesso=False)
    return render_template('login.html')

@app.route('/consulta', methods=['POST'])
def consulta():
    termo = request.form.get('termo')
    conn = sqlite3.connect('banco.db')
    c = conn.cursor()
    query = f"SELECT nome, profissao, salario FROM pessoas WHERE nome LIKE '%{termo}%'"
    try:
        c.execute(query)
        resultados = c.fetchall()
        logging.info(f"Consulta realizada com o termo: {termo}")
    except Exception as e:
        resultados = [("Erro", str(e), "")]
        logging.error(f"Erro na consulta com o termo: {termo} - {e}")
    conn.close()
    return render_template('index.html', resultados=resultados)

@app.route('/inserir', methods=['POST'])
def inserir():
    nome = request.form.get('nome')
    profissao = request.form.get('profissao')
    salario = request.form.get('salario')
    senha = request.form.get('senha')

    # Hash da senha antes de armazenar
    hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    conn = sqlite3.connect('banco.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO pessoas (nome, profissao, salario, senha) VALUES (?, ?, ?, ?)", (nome, profissao, salario, hashed_senha))
        conn.commit()
        logging.info(f"Novo usuário inserido: {nome}, profissão: {profissao}, salário: {salario}")
    except Exception as e:
        logging.error(f"Erro ao inserir usuário: {nome} - {e}")
    finally:
        conn.close()

    return redirect('/')

@app.route('/logout')
def logout():
    logging.info("Usuário deslogado.")
    return redirect('/login')  # redirecionamento

if __name__ == '__main__':
    app.run(debug=True)
