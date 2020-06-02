import graphene

from .models import Todo
from .types import TodoType


class Query(graphene.ObjectType):
    todos = graphene.List(TodoType, completed=graphene.Boolean(),)

    todo = graphene.Field(TodoType, id=graphene.ID(),)

    @staticmethod
    def resolve_todos(root, info, completed=None):
        todos = Todo.objects.order_by("-created")

        if completed is not None:
            todos = todos.filter(completed=completed)
        return todos

    @staticmethod
    def resolve_todo(root, info, id):
        return Todo.objects.get(pk=id)
