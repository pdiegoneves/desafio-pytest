from ninja import NinjaAPI, Schema

from tasks.models import Task


class TaskSchema(Schema):
    title: str


api = NinjaAPI()


@api.get("/hello")
def hello(request):
    return "Hello world"


@api.get("/tasks")
def tasks(request):
    return {"tasks": []}


@api.post("/tasks")
def create_task(request, payload: TaskSchema):
    task = Task.objects.create(title=payload.title)
    return {"id": task.id, "title": task.title}
