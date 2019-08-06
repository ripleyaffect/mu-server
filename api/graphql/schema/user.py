from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from model import User


class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (
            relay.Node,
        )


class UserConnection(relay.Connection):
    class Meta:
        node = UserType
