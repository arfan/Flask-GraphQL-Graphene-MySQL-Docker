from config import Config

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
from app.schema import schema

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    
    # Allows you to get configurations
    # from the config file with the exact environment
    # that you require
    app.config.from_object((get_environment_config()))

    db.init_app(app)

    @app.before_first_request
    def initialize_database():
        """ Create all tables """
        db.create_all()

    @app.route("/")
    def hello_world():
        return "Hello World!"

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True  # for having the GraphiQL interface
        )
    )

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    return app

def get_environment_config():
    if Config.ENV == "PRODUCTION":
        return "config.ProductionConfig"
    elif Config.ENV == "DEVELOPMENT":
        return "config.DevelopmentConfig"