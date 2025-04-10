import pytest

from tasks.models import Task


@pytest.mark.django_db
def test_endpoint_hello_status_code_200(client):
    response = client.get("/api/hello")
    assert response.status_code == 200


def test_endpoint_hello_content_hello_world(client):
    response = client.get("/api/hello")
    assert response.content.decode("utf-8") == '"Hello world"'


@pytest.mark.django_db
def test_endpoint_get_status_code_200(client):
    payload = {"title": "New task"}
    response = client.get("/api/tasks")
    assert response.status_code == 200


@pytest.mark.django_db
def test_endpoint_get_task_list(client):
    payload = {"title": "New task", "completed": False}
    response = client.post("/api/tasks", payload, content_type="application/json")
    tasks = Task.objects.all()
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert response.json()[0]["title"] == "New task"
    assert response.json()[0]["completed"] == False


@pytest.mark.django_db
def test_endpoint_create_task(client):
    payload = {"title": "New task", "completed": False}
    response = client.post("/api/tasks", payload, content_type="application/json")
    assert response.status_code == 200
    assert response.json()["title"] == "New task"


@pytest.mark.django_db
def test_endpoint_task_created(client):
    payload = {"title": "New task", "completed": False}
    response = client.post("/api/tasks", payload, content_type="application/json")
    # Verificar se foi criado no banco de dado
    assert Task.objects.count() == 1
    assert Task.objects.first().title == "New task"


@pytest.mark.django_db
def test_endpoint_task_update(client):
    # Criar a task no banco primeiro
    task = Task.objects.create(title="New task")

    # Cria um payload limpo, sem as merdas internas do Django
    payload = {"title": task.title, "completed": task.completed}

    # Manda o POST com esse payload limpo
    response = client.post("/api/tasks", payload, content_type="application/json")
    assert response.status_code == 200
    assert response.json()["title"] == "New task"
    assert response.json()["completed"] == False

    # Agora vamos testar o PATCH - descomentar quando estiver pronto
    task_id = response.json()["id"]  # Pega o ID que veio na resposta

    response = client.patch(
        f"/api/tasks/{task_id}",
        {"title": "New task", "completed": True},
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json()["title"] == "New task"
    assert response.json()["completed"] == True

    response = client.patch(
        f"/api/tasks/{task_id}",
        {"title": "New task 2", "completed": True},
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json()["title"] == "New task 2"
    assert response.json()["completed"] == True


@pytest.mark.django_db
def test_endpoint_task_delete(client):
    task = Task.objects.create(title="New task")
    task_id = task.id
    response = client.delete(f"/api/tasks/{task_id}")
    assert response.status_code == 204
