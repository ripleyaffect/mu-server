from flask_graphql import GraphQLView

from .schema import schema

view_func = GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True
)
