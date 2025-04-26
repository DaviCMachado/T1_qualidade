from flask import Flask, request, render_template, redirect
import html
import sqlite3
import secrets
import bcrypt
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
csrf = CSRFProtect(app)

@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'"
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Cache-Control'] = 'no-store'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

def gerar_bcrypt_hash(senha):
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verificar_bcrypt_hash(senha, senha_hash):
    return bcrypt.checkpw(senha.encode('utf-8'), senha_hash.encode('utf-8'))

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
        c.execute("SELECT * FROM pessoas WHERE nome = ?", (nome,))
        usuario = c.fetchone()
        conn.close()

        if usuario and verificar_bcrypt_hash(senha, usuario[4]):  # senha está na coluna 4
            mensagem = f"Bem-vindo(a), {nome}!"
            return render_template('login.html', mensagem=mensagem, sucesso=True)
        else:
            mensagem = "Credenciais inválidas. Tente novamente."
            return render_template('login.html', mensagem=mensagem, sucesso=False)

    return render_template('login.html')

@app.route('/consulta', methods=['POST'])
def consulta():
    termo = request.form.get('termo', '').strip()

    if not termo:
        return render_template('index.html', resultados=[("Erro", "Campo de busca vazio.", "")])
    if len(termo) > 100:
        return render_template('index.html', resultados=[("Erro", "Texto muito longo.", "")])

    termo_sanitizado = html.escape(termo)

    conn = sqlite3.connect('banco.db')
    c = conn.cursor()
    try:
        c.execute("SELECT nome, profissao, salario FROM pessoas WHERE nome LIKE ?", ('%' + termo + '%',))
        resultados = c.fetchall()
    except Exception as e:
        resultados = [("Erro", str(e), "")]
    conn.close()

    return render_template('index.html', resultados=resultados, termo=termo_sanitizado)

@app.route('/inserir', methods=['POST'])
def inserir():
    nome = request.form.get('nome')
    profissao = request.form.get('profissao')
    salario = request.form.get('salario')
    senha = request.form.get('senha')

    # Verifica se a senha está vazia
    if not senha or senha.strip() == '':
        return render_template('index.html', mensagem="Senha é obrigatória e não pode ser vazia.", sucesso=False)

    senha_hash = gerar_bcrypt_hash(senha)

    conn = sqlite3.connect('banco.db')
    c = conn.cursor()
    c.execute("INSERT INTO pessoas (nome, profissao, salario, senha) VALUES (?, ?, ?, ?)",
              (nome, profissao, salario, senha_hash))
    conn.commit()
    conn.close()

    return redirect('/')


@app.route('/logout')
def logout():
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)

# rodar com  gunicorn app:app --bind 127.0.0.1:5000