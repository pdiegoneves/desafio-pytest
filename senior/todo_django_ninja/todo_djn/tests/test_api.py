import pytest

from tasks.models import Task


# Fixture que cria uma tarefa no banco de dados para ser usada nos testes
@pytest.fixture
def task():
    return Task.objects.create(title="New task", completed=False)


# Teste para verificar se o endpoint /api/hello retorna código 200 (OK)
@pytest.mark.django_db  # Marca que este teste precisa de acesso ao banco de dados
def test_endpoint_hello_status_code_200(client):
    response = client.get("/api/hello")
    assert response.status_code == 200  # Verifica se a resposta é bem-sucedida


# Teste para verificar o conteúdo retornado pelo endpoint /api/hello
def test_endpoint_hello_content_hello_world(client):
    response = client.get("/api/hello")
    assert (
        response.content.decode("utf-8") == '"Hello world"'
    )  # Verifica o conteúdo exato da resposta


# Teste para verificar se o endpoint GET /api/tasks retorna código 200
@pytest.mark.django_db
def test_endpoint_get_status_code_200(client, task):
    payload = {
        "title": task.title,
        "completed": task.completed,
    }  # Este payload não é usado no teste
    response = client.get("/api/tasks")
    assert response.status_code == 200  # Verifica se a listagem de tarefas funciona


# Teste mais completo da listagem de tarefas, verificando o conteúdo retornado
@pytest.mark.django_db
def test_endpoint_get_task_list(client, task):
    payload = {"title": task.title, "completed": task.completed}
    # Cria uma tarefa adicional via API
    response = client.post("/api/tasks", payload, content_type="application/json")
    tasks = Task.objects.all()  # Esta linha não é usada no teste
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert (
        response.json()[0]["title"] == "New task"
    )  # Verifica se o título está correto
    assert (
        response.json()[0]["completed"] == False
    )  # Verifica se o status completed está correto


# Teste da criação de tarefa através do endpoint POST /api/tasks
@pytest.mark.django_db
def test_endpoint_create_task(client):
    payload = {"title": "New task", "completed": False}
    response = client.post("/api/tasks", payload, content_type="application/json")
    assert response.status_code == 200  # Verifica se a requisição foi bem-sucedida
    assert (
        response.json()["title"] == "New task"
    )  # Verifica se o título foi salvo corretamente


# Teste que verifica se a tarefa foi realmente salva no banco de dados
@pytest.mark.django_db
def test_endpoint_task_created(client, task):
    payload = {"title": task.title, "completed": task.completed}  # Payload não usado
    # Verifica se a tarefa criada pela fixture está no banco
    assert Task.objects.count() == 1  # Verifica se existe exatamente uma tarefa
    assert (
        Task.objects.first().title == "New task"
    )  # Verifica o título da tarefa no banco


# Teste da atualização de tarefa via PATCH
@pytest.mark.django_db
def test_endpoint_task_update(client, task):
    # Primeiro cria uma tarefa para depois atualizá-la
    payload = {"title": task.title, "completed": task.completed}
    response = client.post("/api/tasks", payload, content_type="application/json")
    assert response.status_code == 200
    assert response.json()["title"] == "New task"
    assert response.json()["completed"] == False

    # Teste de atualização do status completed
    task_id = response.json()["id"]  # Captura o ID retornado pela API
    response = client.patch(
        f"/api/tasks/{task_id}",
        {"title": "New task", "completed": True},  # Atualiza apenas o completed
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json()["title"] == "New task"  # Título permanece igual
    assert response.json()["completed"] == True  # Completed foi atualizado

    # Teste de atualização do título
    response = client.patch(
        f"/api/tasks/{task_id}",
        {"title": "New task 2", "completed": True},  # Atualiza apenas o título
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json()["title"] == "New task 2"  # Título foi atualizado
    assert response.json()["completed"] == True  # Completed permanece igual


# Teste da exclusão de tarefa
@pytest.mark.django_db
def test_endpoint_task_delete(client, task):
    task_id = task.id  # Usa o ID da tarefa criada pela fixture
    response = client.delete(f"/api/tasks/{task_id}")
    assert (
        response.status_code == 204
    )  # 204 = No Content, resposta padrão para deleção bem-sucedida
    # Aqui seria bom adicionar uma verificação se a tarefa realmente foi removida do banco
