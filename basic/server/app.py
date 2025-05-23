from flask import Flask, request, render_template, redirect

import sqlite3

app = Flask(__name__)

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
        c.execute("SELECT * FROM pessoas WHERE nome = ? AND senha = ?", (nome, senha))
        usuario = c.fetchone()
        conn.close()

        if usuario:
            mensagem = f"Bem-vindo(a), {nome}!"
            return render_template('login.html', mensagem=mensagem, sucesso=True)
        else:
            mensagem = "Credenciais inválidas. Tente novamente."
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
    except Exception as e:
        resultados = [("Erro", str(e), "")]
    conn.close()
    return render_template('index.html', resultados=resultados)

@app.route('/inserir', methods=['POST'])
def inserir():
    nome = request.form.get('nome')
    profissao = request.form.get('profissao')
    salario = request.form.get('salario')
    senha = request.form.get('senha')

    conn = sqlite3.connect('banco.db')
    c = conn.cursor()
    c.execute("INSERT INTO pessoas (nome, profissao, salario, senha) VALUES (?, ?, ?, ?)", (nome, profissao, salario, senha))
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/logout')
def logout():
    return redirect('/login')  # redirecionamento

if __name__ == '__main__':
    app.run(debug=True)
