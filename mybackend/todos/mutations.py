import graphene

from .models import Todo
from .types import TodoType


class UpdateTodo(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        text = graphene.String()
        completed = graphene.Boolean()

    todo = graphene.Field(TodoType)

    @staticmethod
    def mutate(root, info, id, **kwargs):
        todo = Todo.objects.get(pk=id)
        for key, val in kwargs.items():
            setattr(todo, key, val)
        todo.save()

        return UpdateTodo(todo)


class DeleteTodo(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    id = graphene.ID()

    @staticmethod
    def mutate(root, info, id):
        todo = Todo.objects.get(pk=id)
        todo.delete()

        return DeleteTodo(id)


class CreateTodo(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)
        completed = graphene.Boolean(required=True)

    todo = graphene.Field(TodoType)

    @staticmethod
    def mutate(root, info, **kwargs):
        todo = Todo(**kwargs)
        todo.save()

        return CreateTodo(todo)


class Mutation(graphene.ObjectType):
    create_todo = CreateTodo.Field()
    update_todo = UpdateTodo.Field()
    delete_todo = DeleteTodo.Field()
