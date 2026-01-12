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
    status_filtro = request.args.get('status')

    if status_filtro:
        tarefas_filtradas = [t for t in tarefas if t['status'] == status_filtro]
    else:
        tarefas_filtradas = tarefas

    return render_template('index.html', tarefas=tarefas_filtradas)


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


# A linha abaixo cria uma rota para editar tarefas
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_tarefa(id):
    tarefa = next((t for t in tarefas if t['id'] == id), None)

    if not tarefa:
        return redirect(url_for('index'))

    if request.method == 'POST':
        tarefa['titulo'] = request.form['titulo']
        tarefa['descricao'] = request.form['descricao']
        tarefa['prioridade'] = request.form['prioridade']
        tarefa['status'] = request.form['status']

        return redirect(url_for('index'))

    return render_template('editar.html', tarefa=tarefa)


# A linha abaixo cria uma rota excluir tarefas
@app.route('/excluir/<int:id>')
def excluir_tarefa(id):
    global tarefas
    tarefas = [t for t in tarefas if t['id'] != id]
    return redirect(url_for('index'))


# A linha abaixo mantem a aplicação executando 
if __name__ == '__main__':
    app.run(debug=True)