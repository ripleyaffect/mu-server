from flask import Blueprint

from .graphql import view_func as graphql_view_func


# Create the api blueprint
api_blueprint = Blueprint('api', __name__, url_prefix='/api')


# Register the graphql view function
api_blueprint.add_url_rule(
    '/graphql',
    view_func=graphql_view_func
)
