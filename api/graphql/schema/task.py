from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from model import Task


class TaskType(SQLAlchemyObjectType):
    class Meta:
        model = Task
        interfaces = (
            relay.Node,
        )


class TaskConnection(relay.Connection):
    class Meta:
        node = TaskType
