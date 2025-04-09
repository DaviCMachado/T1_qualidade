from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consulta', methods=['POST'])
def consulta():
    termo = request.form.get('termo')
    conn = sqlite3.connect('banco.db')
    c = conn.cursor()

    # Aqui é propositalmente vulnerável (sem proteção contra SQL Injection)
    query = f"SELECT nome, profissao, salario FROM pessoas WHERE nome LIKE '%{termo}%'"
    try:
        c.execute(query)
        resultados = c.fetchall()
    except Exception as e:
        resultados = [("Erro", str(e), "")]
    
    conn.close()
    return render_template('index.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)
