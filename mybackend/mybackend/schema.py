import graphene
import todos.mutations
import todos.queries
from graphene_django.debug import DjangoDebug


class Query(todos.queries.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(todos.mutations.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
