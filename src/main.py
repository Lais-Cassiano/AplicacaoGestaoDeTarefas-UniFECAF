# A linha abaixo importa a biblioteca flask para criação de aplicação web
from flask import Flask, render_template, request, redirect, url_for

# A linha abaixo instancia a variavel de aplicação
app = Flask(__name__)

# Lista que armazena as tarefas em memória
tarefas = []

# Variável para controle do ID das tarefas
proximo_id = 1

# --------- ROTAS ---------

# A linha abaixo cria uma rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)


# A linha abaixo cria uma rota para criar tarefas
@app.route('/criar', methods=['GET', 'POST'])
def criar_tarefa():
    global proximo_id

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        prioridade = request.form['prioridade']
        status = request.form['status']

        tarefa = {
            "id": proximo_id,
            "titulo": titulo,
            "descricao": descricao,
            "prioridade": prioridade,
            "status": status
        }

        tarefas.append(tarefa)
        proximo_id += 1

        return redirect(url_for('index'))

    return render_template('criar.html')


# A linha abaixo mantem a aplicação executando 
if __name__ == '__main__':
    app.run(debug=True)