from django.http import HttpResponse
from ninja import NinjaAPI, Schema

from tasks.models import Task


class TaskSchema(Schema):
    title: str
    completed: bool


api = NinjaAPI()


@api.get("/hello")
def hello(request):
    return "Hello world"


@api.get("/tasks")
def tasks(request):
    tasks = Task.objects.all()
    return [
        {"id": task.id, "title": task.title, "completed": task.completed}
        for task in tasks
    ]


@api.post("/tasks")
def create_task(request, payload: TaskSchema):
    task = Task.objects.create(title=payload.title, completed=payload.completed)
    return {"id": task.id, "title": task.title, "completed": task.completed}


@api.patch("/tasks/{task_id}")
def update_task(request, task_id: int, payload: TaskSchema):
    task = Task.objects.get(id=task_id)
    task.title = payload.title
    task.completed = payload.completed
    task.save()
    return {"id": task.id, "title": task.title, "completed": task.completed}


@api.delete("/tasks/{task_id}")
def delete_task(request, task_id: int):
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponse(status=204)
