from graphene import ObjectType, relay, Schema
from graphene_sqlalchemy import SQLAlchemyConnectionField

from .task import TaskConnection
from .user import UserConnection


# Create the Query type
class Query(ObjectType):
    node = relay.Node.Field()
    all_tasks = SQLAlchemyConnectionField(TaskConnection)
    all_users = SQLAlchemyConnectionField(UserConnection)


schema = Schema(query=Query)
