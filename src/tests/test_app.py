import pytest
import src.main as main
from src.main import app, tarefas


@pytest.fixture(autouse=True)
def limpar_dados():
    tarefas.clear()
    main.proximo_id = 1


def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Lista de Tarefas" in response.data


def test_editar_tarefa():
    client = app.test_client()

    # cria uma tarefa para teste
    client.post("/criar", data={
        "titulo": "Original",
        "descricao": "Desc",
        "prioridade": "Baixa",
        "status": "To Do"
    })

    # edita a tarefa criada
    response = client.post("/editar/1", data={
        "titulo": "Editado",
        "descricao": "Nova desc",
        "prioridade": "Média",
        "status": "In Progress"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Editado" in response.data


def test_excluir_tarefa():
    client = app.test_client()

    client.post("/criar", data={
        "titulo": "Excluir",
        "descricao": "",
        "prioridade": "Alta",
        "status": "Done"
    })

    response = client.get("/excluir/1", follow_redirects=True)

    assert response.status_code == 200
    assert b"Excluir" not in response.data
