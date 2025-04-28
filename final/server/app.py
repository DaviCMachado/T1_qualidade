import logging
from flask import Flask, request, session, render_template, redirect
import html
import sqlite3
import secrets
import bcrypt
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import time

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)  # Gera uma chave secreta segura
limiter = Limiter(get_remote_address, app=app)
csrf = CSRFProtect(app)

# Configuração do logger
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configurações de segurança para cookies
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = True

@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self'; "
        "font-src 'self'; "
        "img-src 'self' data:; "
        "connect-src 'self'; "
        "frame-ancestors 'none'; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "form-action 'self';"
    )
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
@limiter.limit("5 per minute")
def login():
    if request.method == 'POST':
        nome = request.form.get('username')
        senha = request.form.get('password')

        if 'tentativas_falhas' not in session:
            session['tentativas_falhas'] = 0

        if session['tentativas_falhas'] >= 3:
            logging.warning(f"Usuário {nome} bloqueado temporariamente por excesso de tentativas.")
            return render_template('login.html', mensagem="Você foi bloqueado por 5 minutos devido a tentativas falhas repetidas.", sucesso=False)

        with sqlite3.connect('banco.db') as conn:
            c = conn.cursor()
            c.execute("SELECT nome, senha FROM pessoas WHERE nome = ?", (nome,))
            usuario = c.fetchone()

        if usuario and bcrypt.checkpw(senha.encode('utf-8'), usuario[1].encode('utf-8')):
            session['usuario'] = nome
            session['tentativas_falhas'] = 0
            logging.info(f"Login bem-sucedido para o usuário: {nome}")
            return render_template('login.html', mensagem="Login bem-sucedido!", sucesso=True)
        else:
            session['tentativas_falhas'] += 1
            logging.warning(f"Tentativa de login falhou para o usuário: {nome} (tentativas: {session['tentativas_falhas']})")
            if session['tentativas_falhas'] >= 3:
                session['bloqueio'] = time.time() + 300
            return render_template('login.html', mensagem="Credenciais inválidas. Tente novamente.", sucesso=False)

    if 'bloqueio' in session and time.time() < session['bloqueio']:
        return render_template('login.html', mensagem="Você foi bloqueado por 5 minutos devido a tentativas falhas repetidas.", sucesso=False)

    return render_template('login.html')

@app.route('/consulta', methods=['POST'])
def consulta():
    termo = request.form.get('termo', '').strip()

    if not termo:
        return render_template('index.html', resultados=[("Erro", "Campo de busca vazio.", "")])
    if len(termo) > 100:
        return render_template('index.html', resultados=[("Erro", "Texto muito longo.", "")])

    termo_sanitizado = html.escape(termo)

    with sqlite3.connect('banco.db') as conn:
        c = conn.cursor()
        try:
            c.execute("SELECT nome, profissao, salario FROM pessoas WHERE nome LIKE '%' || ? || '%'", (termo,))
            resultados = c.fetchall()
            logging.info(f"Consulta realizada com o termo: '{termo}' ({len(resultados)} resultados encontrados)")
        except Exception as e:
            resultados = [("Erro", str(e), "")]
            logging.error(f"Erro na consulta usando termo '{termo}': {e}")

    return render_template('index.html', resultados=resultados, termo=termo_sanitizado)

@app.route('/inserir', methods=['POST'])
def inserir():
    nome = request.form.get('nome')
    profissao = request.form.get('profissao')
    salario = request.form.get('salario')
    senha = request.form.get('senha')

    if not senha or senha.strip() == '':
        return render_template('index.html', mensagem="Senha é obrigatória e não pode ser vazia.", sucesso=False)

    senha_hash = gerar_bcrypt_hash(senha)

    with sqlite3.connect('banco.db') as conn:
        c = conn.cursor()
        try:
            c.execute("INSERT INTO pessoas (nome, profissao, salario, senha) VALUES (?, ?, ?, ?)",
                      (nome, profissao, salario, senha_hash))
            conn.commit()
            user_id = c.lastrowid
            logging.info(f"Novo usuário inserido: {nome} (ID: {user_id}), profissão: {profissao}, salário: {salario}")
        except Exception as e:
            logging.error(f"Erro ao inserir usuário {nome}: {e}")

    return redirect('/')

@app.route('/logout')
def logout():
    usuario = session.get('usuario', 'desconhecido')
    session.clear()
    logging.info(f"Usuário {usuario} deslogou.")
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)

# rodar com gunicorn
# gunicorn app:app --bind 127.0.0.1:5000