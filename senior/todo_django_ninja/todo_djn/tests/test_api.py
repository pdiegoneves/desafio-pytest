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
def test_endpoint_task_get_status_code_200(client):
    response = client.get("/api/tasks")
    assert response.status_code == 200


@pytest.mark.django_db
def test_endpoint_task_task_create_task(client):
    payload = {"title": "New task"}
    response = client.post("/api/tasks", payload, content_type="application/json")
    assert response.status_code == 200
    assert response.json()["title"] == "New task"

    # Verificar se foi criado no banco de dados
    assert Task.objects.count() == 1
    assert Task.objects.first().title == "New task"
